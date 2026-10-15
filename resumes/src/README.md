# CV source — build pipeline

The three PDFs in `resumes/` are generated from this folder, so content and design
stay consistent across all tracks and can be regenerated at any time.

```text
resumes/src/
├── build.py            # YAML + template -> A4 PDF (headless Chromium)
├── template.html.j2    # page structure (Jinja2)
├── styles.css          # the design system: themes, spacing, decoration
├── assets/headshot.jpg # photo used in the header band
└── data/
    ├── common.yml      # verified personal facts + availability line (all three CVs)
    ├── backend.yml     # Backend Developer track   (navy theme)
    ├── fullstack.yml   # Full Stack Developer track (violet theme)
    └── ai.yml          # AI Application Engineer track (teal theme)
```

## Rebuild

```bash
python3 resumes/src/build.py            # all three CVs
python3 resumes/src/build.py backend    # one track
python3 resumes/src/build.py --png      # also write PNG previews to resumes/src/build/
```

Each run writes `resumes/CV_*.pdf`, copies the same file to the repository root
(the two locations are kept identical), and prints a fit report:

```text
OK CV_Backend_TruongVanTinh.pdf    267 KB  1p  slack p1 +6mm
```

* `1p` — page count; it must match the number of entries under `pages:` in the YAML.
* `slack` — vertical space left between the last block of a sheet and its footer.
  A negative value means the sheet overflows and content is being clipped: trim
  copy (a bullet that wraps to a second line costs ~4 mm) until it is positive.
  Keep a few millimetres in hand.

Add `--debug` to see the height of every section, which makes it obvious where
the millimetres go:

```text
sheet 1: HEADER=38 Professional=21 facts=11 Work=58 Projects=59 Skills=54 cards=14
```

## Editing rules

1. **Content lives in `data/*.yml` only.** Every claim must be traceable to
   `APPLICANT_CONTEXT.md`. Never add employment history, certifications, metrics
   or years of experience that are not verified there.
   **Never drop keywords to win space.** The skill groups are at least as complete
   as the original CVs (git `5e8e9db`) — recruiters and ATS filters match on them.
   When a page overflows, tighten spacing or shorten a sentence instead; the
   `--debug` heights show where the room actually is.
2. **Design lives in `styles.css`.** Each track picks a theme (`navy`, `violet`,
   `teal`) and a density (`compact`, `relaxed`, `comfortable`) so the two sheets
   stay evenly filled.
3. **Page layout** is controlled by `pages:` — a list of sheets, each a list of
   sections (`summary`, `facts`, `highlights`, `experience`, `projects`,
   `skills`, `footerinfo`). All three CVs currently use **one sheet**:

   ```yaml
   pages:
     - [summary, facts, experience, projects, skills, footerinfo]
   ```

   A single sheet switches the stylesheet into **one-page mode**
   (`body.one-page`): tighter header band, no page counter, projects on one
   head line, skills as comma lists instead of chips, and education plus
   languages collapsed into one strip.

   If a CV ever needs two sheets again, add a second list; a section can also be
   split across sheets:

   ```yaml
   pages:
     - [summary, highlights, experience, {section: projects, take: 1}]
     - [{section: projects, skip: 1, continued: true}, skills, footerinfo]
   ```

## Why these choices

* **Carlito** (metric-compatible with Calibri) embeds as CID TrueType, so the PDF
  text stays selectable and ATS-parsable — verify with `pdftotext file.pdf -`.
* **Single-column body**: colour and decoration come from the header band, the
  key-facts strip and accent rails rather than from a sidebar, which ATS parsers
  often read out of order.
* **One A4 page** per track: everything a recruiter screens on is above the fold,
  and `slack` keeps the layout honest while content is edited.
* **Chromium print-to-PDF** keeps real text (no rasterised images of text) and
  renders background colours because the stylesheet sets `print-color-adjust: exact`.

## Requirements

Python 3 with `pyyaml`, `jinja2` and `pypdf`; `poppler-utils` for `pdfinfo` /
`pdftoppm`; a Chromium or Chrome binary (auto-detected by `build.py`).
