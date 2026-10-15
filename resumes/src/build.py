#!/usr/bin/env python3
"""Build the three specialised CVs (PDF) from YAML content + one HTML/CSS design.

Usage:
    python3 resumes/src/build.py                 # build all three CVs
    python3 resumes/src/build.py backend ai      # build selected variants
    python3 resumes/src/build.py --png           # also write PNG previews to build/

Content lives in data/*.yml and must stay traceable to APPLICANT_CONTEXT.md.
Design lives in template.html.j2 + styles.css.
Rendering: headless Chromium -> A4 PDF (real text, selectable and ATS-parsable).
"""

from __future__ import annotations

import base64
import glob
import mimetypes
import re
import shutil
from urllib.parse import quote
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

SRC = Path(__file__).resolve().parent
RESUMES = SRC.parent
ROOT = RESUMES.parent
BUILD = SRC / "build"

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
    shutil.which("google-chrome") or "",
]


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if c and Path(c).exists():
            return c
    hits = sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome"))
    if hits:
        return hits[0]
    sys.exit("No Chromium/Chrome binary found - cannot render PDF.")


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def normalise(entry, cv: dict) -> dict:
    """Page entries may be a plain section name or {section, take, skip, continued}."""
    sec = {"section": entry} if isinstance(entry, str) else dict(entry)
    sec.setdefault("skip", 0)
    sec.setdefault("continued", False)
    total = len(cv.get(sec["section"], []) or [])
    sec.setdefault("take", max(total - sec["skip"], 0) or total)
    return sec


def load(variant: str) -> tuple[dict, dict]:
    me = yaml.safe_load((SRC / "data" / "common.yml").read_text(encoding="utf-8"))
    cv = yaml.safe_load((SRC / "data" / f"{variant}.yml").read_text(encoding="utf-8"))
    return me, cv


def render_html(variant: str) -> tuple[str, str]:
    me, cv = load(variant)

    env = Environment(
        loader=FileSystemLoader(str(SRC)),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    cv["pages"] = [[normalise(s, cv) for s in page] for page in cv["pages"]]

    env.filters["urlquote"] = lambda u: quote(u, safe=":/?#[]@!$&'()*+,;=~")

    tpl = env.get_template("template.html.j2")
    html = tpl.render(
        me=me,
        cv=cv,
        css=(SRC / "styles.css").read_text(encoding="utf-8"),
        photo=data_uri(SRC / me["photo"]),
    )
    return html, cv["output"]


def measure(chrome: str, page: Path, tmp: str) -> str:
    """Vertical slack (mm) left on each sheet; negative means the sheet overflows."""
    res = subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--virtual-time-budget=4000",
         f"--user-data-dir={tmp}/profile-dom", "--dump-dom", page.as_uri()],
        capture_output=True, text=True,
    )
    if "--debug" in sys.argv:
        for i, sec in enumerate(re.findall(r'data-sections="([^"]*)"', res.stdout), 1):
            print(f"   sheet {i}: {sec}")
    m = re.search(r'data-fit="([^"]*)"', res.stdout)
    if not m:
        return "fit: unknown"
    parts = []
    for item in m.group(1).split(","):
        n, px = item.split(":")
        parts.append(f"p{n} {float(px) / 96 * 25.4:+.0f}mm")
    return "slack " + " / ".join(parts)


def to_pdf(html: str, out_pdf: Path, png: bool = False) -> str:
    chrome = find_chrome()
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "cv.html"
        page.write_text(html, encoding="utf-8")
        fit = measure(chrome, page, tmp)
        cmd = [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=4000",
            f"--user-data-dir={tmp}/profile",
            f"--print-to-pdf={out_pdf}",
            page.as_uri(),
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if not out_pdf.exists():
            sys.exit(f"Chromium failed to produce {out_pdf}\n{res.stderr}")
    if png:
        BUILD.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "110", str(out_pdf), str(BUILD / out_pdf.stem)],
            check=False,
        )
    return fit


def set_metadata(pdf: Path, me: dict, cv: dict) -> None:
    """Document properties recruiters and ATS tools read from the file itself."""
    from pypdf import PdfWriter

    keywords = [cv["role"]]
    for group in cv["skills"]:
        keywords += list(group["items"])
    writer = PdfWriter(clone_from=str(pdf))
    writer.add_metadata({
        "/Title": f"{me['name']} - {cv['role']} CV",
        "/Author": me["name"],
        "/Subject": f"{cv['role']} CV - {cv['tagline']}",
        "/Keywords": ", ".join(dict.fromkeys(keywords)),
        "/Creator": "resumes/src/build.py",
    })
    with open(pdf, "wb") as fh:
        writer.write(fh)


def page_count(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return -1


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    png = "--png" in sys.argv
    variants = args or ["backend", "fullstack", "ai"]

    for variant in variants:
        html, out_name = render_html(variant)
        pdf = RESUMES / out_name
        fit = to_pdf(html, pdf, png=png)
        me, cv = load(variant)
        set_metadata(pdf, me, cv)
        # Keep the repository-root copies in sync with resumes/.
        shutil.copyfile(pdf, ROOT / out_name)
        expected = len(cv["pages"])
        pages = page_count(pdf)
        flag = "OK " if pages == expected and "-" not in fit else "!! "
        print(f"{flag}{out_name:34s} {pdf.stat().st_size // 1024:4d} KB  {pages}p  {fit}")
        if pages != expected:
            print("   -> content overflows the sheet; trim data or adjust spacing.")


if __name__ == "__main__":
    main()
