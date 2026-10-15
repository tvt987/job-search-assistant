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
    ├── common.yml      # verified personal facts (shared by all three CVs)
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
OK CV_Backend_TruongVanTinh.pdf    367 KB  2p  slack p1 +4mm / p2 +4mm
```

* `2p` — page count; it must match the number of entries under `pages:` in the YAML.
* `slack` — vertical space left between the last block of a sheet and its footer.
  A negative value means the sheet overflows and content is being clipped: move a
  section to the next page, or trim copy, until every value is positive.

## Editing rules

1. **Content lives in `data/*.yml` only.** Every claim must be traceable to
   `APPLICANT_CONTEXT.md`. Never add employment history, certifications, metrics
   or years of experience that are not verified there.
2. **Design lives in `styles.css`.** Each track picks a theme (`navy`, `violet`,
   `teal`) and a density (`compact`, `relaxed`, `comfortable`) so the two sheets
   stay evenly filled.
3. **Page layout** is controlled by `pages:` — a list of sheets, each a list of
   sections (`summary`, `highlights`, `experience`, `projects`, `skills`,
   `footerinfo`). A section can be split across sheets:

   ```yaml
   pages:
     - [summary, highlights, experience, {section: projects, take: 1}]
     - [{section: projects, skip: 1, continued: true}, skills, footerinfo]
   ```

## Why these choices

* **Carlito** (metric-compatible with Calibri) embeds as CID TrueType, so the PDF
  text stays selectable and ATS-parsable — verify with `pdftotext file.pdf -`.
* **Single-column body**: colour and decoration come from the header band, cards
  and chips rather than from a sidebar, which ATS parsers often read out of order.
* **Chromium print-to-PDF** keeps real text (no rasterised images of text) and
  renders background colours because the stylesheet sets `print-color-adjust: exact`.

## Requirements

Python 3 with `pyyaml`, `jinja2` and `pypdf`; `poppler-utils` for `pdfinfo` /
`pdftoppm`; a Chromium or Chrome binary (auto-detected by `build.py`).
