#!/usr/bin/env python3
"""Build the final CVs: a designed PDF and an ATS-first PDF per track, plus the data for the DOCX build.

Usage:
    python3 output/final-cvs/src/build.py             # all tracks, both layouts
    python3 output/final-cvs/src/build.py ai --png    # one track, with PNG previews in build/

Content: data/*.yml (verified facts only). Design: template.html.j2 + styles.css.
Rendering: headless Chromium -> A4 PDF with real, selectable text and clickable links.
The original CVs in resumes/ are never read or written by this script.
"""

from __future__ import annotations

import base64
import glob
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from pypdf import PdfWriter

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
BUILD = SRC / "build"
TRACKS = ["backend", "fullstack", "ai"]
MODES = {"designed": "", "ats": "_ATS"}


def find_chrome() -> str:
    for c in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", shutil.which("chromium") or "",
              shutil.which("google-chrome") or ""]:
        if c and Path(c).exists():
            return c
    hits = sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome"))
    if hits:
        return hits[0]
    sys.exit("No Chromium binary found.")


def load(track: str) -> tuple[dict, dict]:
    me = yaml.safe_load((SRC / "data" / "common.yml").read_text(encoding="utf-8"))
    cv = yaml.safe_load((SRC / "data" / f"{track}.yml").read_text(encoding="utf-8"))
    return me, cv


def render(track: str, mode: str) -> str:
    me, cv = load(track)
    env = Environment(loader=FileSystemLoader(str(SRC)), undefined=StrictUndefined,
                      autoescape=True, trim_blocks=True, lstrip_blocks=True)
    env.filters["urlquote"] = lambda u: quote(u, safe=":/?#[]@!$&'()*+,;=~")
    photo = (SRC / me["photo"]).resolve()
    return env.get_template("template.html.j2").render(
        me=me, cv=cv, mode=mode, css=(SRC / "styles.css").read_text(encoding="utf-8"),
        photo="data:image/jpeg;base64," + base64.b64encode(photo.read_bytes()).decode(),
    )


def chrome_run(chrome: str, tmp: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
                           "--virtual-time-budget=4000", f"--user-data-dir={tmp}/p", *args],
                          capture_output=True, text=True)


def build_pdf(html: str, pdf: Path) -> str:
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "cv.html"
        page.write_text(html, encoding="utf-8")
        dom = chrome_run(chrome, tmp, "--dump-dom", page.as_uri()).stdout
        chrome_run(chrome, tmp, "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                   f"--print-to-pdf={pdf}", page.as_uri())
    if not pdf.exists():
        sys.exit(f"Chromium failed to write {pdf}")
    m = re.search(r'data-fit="(\d+):(-?\d+)"', dom)
    return f"{m.group(1)} sheet(s), {int(m.group(2)) / 96 * 25.4:.0f}mm free" if m else "fit unknown"


def set_metadata(pdf: Path, me: dict, cv: dict) -> None:
    keywords = [cv["title"]] + [i for g in cv["skills"] for i in g["items"]]
    writer = PdfWriter(clone_from=str(pdf))
    writer.add_metadata({
        "/Title": f"{me['name']} - {cv['title']} ({cv['subtitle']}) CV",
        "/Author": me["name"],
        "/Subject": cv["stack"].replace(" · ", ", "),
        "/Keywords": ", ".join(dict.fromkeys(keywords)),
        "/Creator": "output/final-cvs/src/build.py",
    })
    with open(pdf, "wb") as fh:
        writer.write(fh)


def pages(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def main() -> None:
    tracks = [a for a in sys.argv[1:] if not a.startswith("-")] or TRACKS
    BUILD.mkdir(exist_ok=True)
    docx_data = {}
    for track in tracks:
        me, cv = load(track)
        docx_data[track] = {"me": me, "cv": cv}
        for mode, suffix in MODES.items():
            pdf = OUT / f"{cv['file_stem']}{suffix}.pdf"
            fit = build_pdf(render(track, mode), pdf)
            set_metadata(pdf, me, cv)
            n = pages(pdf)
            print(f"{'OK ' if n == 1 else '!! '}{pdf.name:38s} {n}p  {fit}")
            if "--png" in sys.argv:
                for old in BUILD.glob(f"{pdf.stem}-*.png"):
                    old.unlink()
                subprocess.run(["pdftoppm", "-png", "-r", "110", str(pdf), str(BUILD / pdf.stem)], check=False)
    (BUILD / "cv-data.json").write_text(json.dumps(docx_data, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
