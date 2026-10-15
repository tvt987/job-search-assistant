# Job Search & Application Assistant

An automated, safety-first job-search and application tracking assistant powered by **Claude Code / Claude Cloud**.

---

## 📁 Repository Structure

```text
├── CLAUDE.md                    # Core operational prompt & behavioral guidelines for Claude
├── APPLICANT_CONTEXT.md          # Single source of truth for candidate profile, projects, and rules
├── job-tracker.csv               # Application tracking ledger (status, URLs, matches, dates)
├── resumes/                      # The 3 specialized PDF resumes
│   ├── CV_Backend_TruongVanTinh.pdf     # Backend .NET / C# track
│   ├── CV_FullStack_TruongVanTinh.pdf   # Full Stack .NET + Angular track
│   ├── CV_AI_TruongVanTinh.pdf          # AI Application Engineer / GenAI track
│   └── src/                             # Source of the 3 PDFs (YAML content + HTML/CSS design)
│       ├── build.py                     # Rebuild: python3 resumes/src/build.py
│       ├── template.html.j2 / styles.css
│       └── data/*.yml                   # Per-track content, traceable to APPLICANT_CONTEXT.md
├── application-templates/        # Standard cover letters, outreach messages, and Q&A references
│   ├── cover_letter_backend.md
│   ├── cover_letter_fullstack.md
│   ├── cover_letter_ai.md
│   ├── recruiter_outreach_messages.md
│   └── screening_qa.md
├── .gitignore                    # Protection against committing credentials, tokens, or sessions
└── README.md                     # Documentation & usage guide
```

---

## 🎯 Target Role Tracks & Resume Matching

| Track | Primary Stack | Resume File |
| :--- | :--- | :--- |
| **Backend Developer** | C#, .NET 8, ASP.NET Core, SQL Server, Dapper, Keycloak, REST APIs | `resumes/CV_Backend_TruongVanTinh.pdf` |
| **Full Stack Developer** | .NET Core + Angular 19 / AngularJS, TypeScript, RxJS, NgRx, PostgreSQL | `resumes/CV_FullStack_TruongVanTinh.pdf` |
| **AI Application Engineer** | Python, FastAPI, RAG, TF-IDF / Embeddings, LLM Validation, Human-in-the-loop | `resumes/CV_AI_TruongVanTinh.pdf` |

---

## 🚀 How to Run with Claude Code / Claude Cloud

### Option 1: Claude Code CLI
1. Open this repository directory in your terminal.
2. Launch Claude Code:
   ```bash
   claude
   ```
3. Claude automatically reads `CLAUDE.md` and initializes the workflow. You can prompt:
   ```text
   Read APPLICANT_CONTEXT.md and initialize Phase 1. Search for open Backend .NET and AI Application roles in HCMC, rank them, and update job-tracker.csv.
   ```

### Option 2: Claude Cloud / Desktop with Browser Use
- Attach this repository (or copy `CLAUDE.md` and `APPLICANT_CONTEXT.md`).
- Ensure browser automation tools are enabled.
- Always check active authenticated sessions before initiating searches or form-filling.

---

## 📄 Rebuilding the resumes

The PDFs are generated, not hand-edited. Change the content in `resumes/src/data/*.yml`
or the design in `resumes/src/styles.css`, then run:

```bash
python3 resumes/src/build.py          # rebuilds all three PDFs (resumes/ + repo root)
python3 resumes/src/build.py --png    # also writes page previews to resumes/src/build/
```

Each CV is a single A4 page. The build prints a fit report per CV
(`1p  slack p1 +6mm`); a negative slack value means the page overflows and the copy
has to be trimmed before shipping. See `resumes/src/README.md` for details.

---

## 🔒 Security & Privacy Directives
- **Zero Credential Storage:** Never commit passwords, session tokens, cookies, or OTPs.
- **Strict Verification:** Unverified fields (salary, notice period, legal waivers) must be marked `NEEDS_USER_INPUT` for explicit candidate confirmation.
- **No Hallucinated Experience:** All claims must strictly trace back to verified facts in `APPLICANT_CONTEXT.md`.
