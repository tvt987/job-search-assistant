// Editable Word versions of the ATS-first CVs, from build/cv-data.json (written by build.py).
// Usage: node output/final-cvs/src/build_docx.js
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ExternalHyperlink, AlignmentType, BorderStyle,
  LevelFormat, TabStopType,
} = require("docx");

const SRC = __dirname;
const OUT = path.dirname(SRC);
const data = JSON.parse(fs.readFileSync(path.join(SRC, "build", "cv-data.json"), "utf8"));

const FONT = "Calibri";           // Carlito, used for the PDFs, is metric-compatible with Calibri
const BODY = 20;                  // half-points: 10pt
const SMALL = 19;                 // 9.5pt
const PAGE_W = 11906, MARGIN_X = 737, MARGIN_TOP = 567, MARGIN_BOTTOM = 510;  // A4, 13mm / 10mm / 9mm
const RIGHT = PAGE_W - 2 * MARGIN_X;

const run = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || BODY, bold: o.bold, italics: o.italics });
const link = (text, url, size = BODY) => new ExternalHyperlink({
  link: url, children: [new TextRun({ text, font: FONT, size, style: "Hyperlink" })],
});
const para = (children, o = {}) => new Paragraph({ children, spacing: { before: o.before || 0, after: 0, line: 252 }, ...o.extra });

function heading(text) {
  return new Paragraph({
    children: [run(text.toUpperCase(), { bold: true, size: 21 })],
    spacing: { before: 110, after: 50 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "9CA3AF", space: 1 } },
  });
}

// Title line on the left, date or link right-aligned on the same line.
function itemHead(left, right, before = 50) {
  return new Paragraph({
    children: [...left, ...(right ? [new TextRun({ text: "\t", font: FONT }), right] : [])],
    tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
    spacing: { before, after: 0, line: 252 },
  });
}

const bullet = (text) => new Paragraph({
  children: [run(text)], numbering: { reference: "bullets", level: 0 }, spacing: { before: 4, after: 0, line: 252 },
});

function cvDoc(me, cv) {
  const c = [];
  c.push(para([run(me.name, { bold: true, size: 44 })]));
  c.push(para([run(cv.title, { bold: true, size: 25 }), run(` | ${cv.subtitle}`, { size: 25 })], { before: 20 }));
  c.push(para([run(cv.stack, { bold: true })], { before: 10 }));
  c.push(para([
    run(`${me.phone} | `, { size: SMALL }), link(me.email, `mailto:${me.email}`, SMALL),
    run(` | ${me.location} (${me.work_mode})`, { size: SMALL }),
  ], { before: 20 }));
  c.push(para([
    link(me.github, me.github_url, SMALL), run(" | ", { size: SMALL }),
    link(me.linkedin, encodeURI(me.linkedin_url), SMALL),
  ]));

  c.push(heading("Summary"));
  c.push(para([run(cv.summary.trim())]));

  c.push(heading("Work Experience"));
  cv.experience.forEach((job, i) => {
    const left = [run(job.role, { bold: true }), run(` | ${job.company}`)];
    c.push(itemHead(left, run(job.period, { size: SMALL }), i ? 70 : 0));
    if (job.stack) c.push(para([run(`${job.context ? me.con_cung_context + ". " : ""}Tech: ${job.stack}`, { italics: true, size: SMALL })]));
    job.bullets.forEach((b) => c.push(bullet(b)));
  });

  c.push(heading("Projects"));
  cv.projects.forEach((p, i) => {
    const ref = me.project_catalogue[p.key];
    const left = [run(ref.name, { bold: true }), run(` | ${p.role} | ${p.stack}`)];
    c.push(itemHead(left, ref.link ? link(ref.link, `https://${ref.link}`, SMALL) : null, i ? 70 : 0));
    p.bullets.forEach((b) => c.push(bullet(b)));
  });
  const others = [run("Other projects: ", { bold: true, size: SMALL })];
  cv.other_projects.forEach((o, i) => {
    const ref = me.project_catalogue[typeof o === "string" ? o : o.key];
    const short = typeof o === "string" ? ref.short : o.text;
    others.push(ref.link ? link(ref.name, `https://${ref.link}`, SMALL) : run(ref.name, { size: SMALL }));
    others.push(run(` (${short})${i < cv.other_projects.length - 1 ? "; " : "."}`, { size: SMALL }));
  });
  c.push(para(others, { before: 60 }));

  c.push(heading("Technical Skills"));
  cv.skills.forEach((g) => c.push(para([run(`${g.label}: `, { bold: true, size: SMALL }), run(g.items.join(", "), { size: SMALL })], { before: 10 })));

  c.push(heading("Education"));
  const e = me.education;
  c.push(para([run(e.school, { bold: true }), run(` | ${e.degree} | ${e.period}`)]));
  c.push(para([run("Languages: ", { bold: true }), run(me.languages.map((l) => `${l.name} (${l.level})`).join("; "))]));

  return new Document({
    creator: me.name,
    title: `${me.name} - ${cv.title} (${cv.subtitle}) CV`,
    subject: cv.stack.replaceAll(" · ", ", "),
    keywords: [cv.title, ...cv.skills.flatMap((g) => g.items)].join(", "),
    styles: { default: { document: { run: { font: FONT, size: BODY } } } },
    numbering: {
      config: [{
        reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
                   style: { paragraph: { indent: { left: 200, hanging: 190 } } } }],
      }],
    },
    sections: [{
      properties: { page: { size: { width: PAGE_W, height: 16838 },
                            margin: { top: MARGIN_TOP, bottom: MARGIN_BOTTOM, left: MARGIN_X, right: MARGIN_X } } },
      children: c,
    }],
  });
}

(async () => {
  for (const [track, { me, cv }] of Object.entries(data)) {
    const out = path.join(OUT, `${cv.file_stem}.docx`);
    fs.writeFileSync(out, await Packer.toBuffer(cvDoc(me, cv)));
    console.log(`wrote ${path.basename(out)}`);
  }
})();
