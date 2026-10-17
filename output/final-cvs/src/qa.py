#!/usr/bin/env python3
"""Final QA on the delivered CV files (not on the sources).

Usage: python3 output/final-cvs/src/qa.py   -> prints a report and exits non-zero on any failure.

Checks per PDF: one A4 page, stream-order text keeps bullets under their job, no ligature code points,
smallest text >= 9pt (ATS-first) or >= 8pt for labels in the designed version, expected links,
no retired/unsupported claims, required verified facts present.
Checks per DOCX: renders to one page with LibreOffice, same claims rules as the PDFs.
Also checks that resumes/ and the repository root hold exactly the designed PDFs built here.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pypdf
import yaml

OUT = Path(__file__).resolve().parent.parent
ROOT = OUT.parent.parent
TRACKS = {"Backend": "backend", "FullStack": "fullstack", "AI": "ai"}

# Claims removed because the public repos do not support them, or outdated wording.
FORBIDDEN = [r"\b1,000\b", r"\b120 (synthetic )?schema", r"\b720\b", r"10 (FastAPI )?HTTP", r"\b8 synthetic",
             r"Conversational", r"0931467024", r"\bcertif", r"Vietnamese \(native\)", r"→", r"PII masking"]
# Verified facts every version of a track must state.
REQUIRED = {
    "backend": ["Con Cung", "Nov 2023 – Present", "Sep 2023 – Nov 2023", "42 xUnit", "202 replay, 409 conflict",
                "7 subscription benefit calculations", "Keycloak", "10 ASP.NET Core routes", "22 API and cache tests",
                "AI-assisted lab", "Graduated 2026", "basic spoken"],
    "fullstack": ["Con Cung", "Nov 2023 – Present", "Sep 2023 – Nov 2023", "Angular 19", "NgRx SignalStore",
                  "7 subscription benefit calculations", "controller, repository, view and script", "42 xUnit",
                  "10 ASP.NET Core routes", "AI-assisted", "Graduated 2026", "basic spoken"],
    "ai": ["Con Cung", "Nov 2023 – Present", "Sep 2023 – Nov 2023", "16-question synthetic eval", "29 tests",
           "7 tests and a 5-case rules-baseline eval", "Qdrant", "LangChain", "22 tests on real Redis",
           "AI-assisted lab", "Graduated 2026", "basic spoken"],
}
LINKS = {"https://github.com/tvt987", "mailto:tinhkun102@gmail.com",
         "https://github.com/tvt987/partner-integration-bff", "https://github.com/tvt987/Layout-Store",
         "https://github.com/tvt987/Ecommerce-Admin", "https://github.com/tvt987/retail-rag-assistant",
         "https://github.com/tvt987/support-ticket-ai-triage"}

failures: list[str] = []


def check(ok: bool, label: str) -> str:
    if not ok:
        failures.append(label)
    return "PASS" if ok else "FAIL"


def claims(text: str, track: str, name: str) -> list[str]:
    flat = " ".join(text.split())
    rows = []
    bad = [p for p in FORBIDDEN if re.search(p, flat, re.I)]
    rows.append(f"  forbidden claims absent      {check(not bad, f'{name}: forbidden {bad}')} {bad or ''}")
    missing = [r for r in REQUIRED[track] if r.lower() not in flat.lower()]  # designed labels are CSS upper-case
    rows.append(f"  required facts present       {check(not missing, f'{name}: missing {missing}')} {missing or ''}")
    return rows


def first_bullet(track: str) -> str:
    cv = yaml.safe_load((OUT / "src" / "data" / f"{track}.yml").read_text(encoding="utf-8"))
    return cv["experience"][0]["bullets"][0][:40]


def pdf_report(pdf: Path, track: str) -> list[str]:
    r = pypdf.PdfReader(pdf)
    page = r.pages[0]
    text = page.extract_text()
    w, h = float(page.mediabox.width), float(page.mediabox.height)
    sizes: set[float] = set()
    page.extract_text(visitor_text=lambda t, cm, tm, fd, fs: t.strip() and sizes.add(round(fs * tm[0] * 72 / 96, 1)))
    links = {a.get_object()["/A"].get("/URI") for a in page.get("/Annots", [])}
    flat = " ".join(text.split())
    i, j = flat.find("Con Cung"), flat.find("Frontend Intern")
    k = flat.find(" ".join(first_bullet(track).split()))
    designed = not pdf.stem.endswith("_ATS")
    floor = 8 if designed else 9
    rows = [f"{pdf.name}",
            f"  one A4 page                  {check(len(r.pages) == 1 and abs(w - 595) < 2 and abs(h - 842) < 2, pdf.name + ': page')}",
            f"  bullets in reading order     {check(0 <= i < k < j, pdf.name + ': order')}",
            f"  no ligature code points      {check(not re.search('[ﬀ-ﬆ]', text), pdf.name + ': ligatures')}",
            f"  smallest text >= {floor}pt         {check(min(sizes) >= floor, pdf.name + ': font')} ({min(sizes)}pt)",
            f"  links ok                     {check(LINKS <= links and any('linkedin.com/in/' in (u or '') for u in links), pdf.name + ': links')} ({len(links)})"]
    photo = bool(page.images)
    rows.append(f"  photo only on designed       {check(photo == designed, pdf.name + ': photo')}")
    return rows + claims(text, track, pdf.name)


def docx_report(docx: Path, track: str, tmp: Path) -> list[str]:
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(docx)],
                   capture_output=True)
    rendered = tmp / f"{docx.stem}.pdf"
    pages = len(pypdf.PdfReader(rendered).pages) if rendered.exists() else 0
    text = subprocess.run(["pandoc", "-t", "plain", str(docx)], capture_output=True, text=True).stdout
    rows = [f"{docx.name}",
            f"  one page when rendered       {check(pages == 1, docx.name + ': pages')} ({pages})",
            f"  no ligature code points      {check(not re.search('[ﬀ-ﬆ]', text), docx.name + ': ligatures')}"]
    return rows + claims(text, track, docx.name)


def main() -> int:
    lines = []
    with tempfile.TemporaryDirectory() as tmp:
        for stem, track in TRACKS.items():
            base = f"CV_{stem}_TruongVanTinh"
            lines += pdf_report(OUT / f"{base}.pdf", track)
            lines += pdf_report(OUT / f"{base}_ATS.pdf", track)
            lines += docx_report(OUT / f"{base}.docx", track, Path(tmp))
    for stem in TRACKS:
        name = f"CV_{stem}_TruongVanTinh.pdf"
        built = (OUT / name).read_bytes()
        same = all((d / name).read_bytes() == built for d in (ROOT / "resumes", ROOT))
        lines.append(f"resumes/ and root copies of {name:31s} {check(same, name + ': copies out of sync')}")
    print("\n".join(lines))
    print(f"\n{'ALL CHECKS PASSED' if not failures else f'{len(failures)} FAILURE(S): ' + '; '.join(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
