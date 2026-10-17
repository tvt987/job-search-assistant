# CV review report

Candidate: Truong Van Tinh, Ho Chi Minh City. Prepared 2026-10-17.

Related files:
- Scores: `cv-scorecard.md`
- Evidence: `verified-facts-and-gaps.md`
- Market: `market-research.md`
- Next steps: `next-improvements.md`

## Deliverables (`final-cvs/`)

| Track | Designed PDF (photo) | ATS-first PDF | Editable DOCX |
|---|---|---|---|
| Backend .NET | `CV_Backend_TruongVanTinh.pdf` | `CV_Backend_TruongVanTinh_ATS.pdf` | `CV_Backend_TruongVanTinh.docx` |
| Full Stack .NET + Angular | `CV_FullStack_TruongVanTinh.pdf` | `CV_FullStack_TruongVanTinh_ATS.pdf` | `CV_FullStack_TruongVanTinh.docx` |
| AI Application Engineer | `CV_AI_TruongVanTinh.pdf` | `CV_AI_TruongVanTinh_ATS.pdf` | `CV_AI_TruongVanTinh.docx` |

**Which file to send:**
- **Designed PDF** for Vietnamese employers and recruiters who read the CV themselves.
- **ATS-first PDF** for portals and multinational ATS uploads (LinkedIn, Greenhouse, Workday and similar).
- **DOCX** when a recruiter asks for Word or wants to edit the CV.

All nine files are one A4 page, with body text at 10pt and nothing smaller than 9.5pt. Rebuild with:
```
python3 output/final-cvs/src/build.py
node output/final-cvs/src/build_docx.js
python3 output/final-cvs/src/qa.py
```

The original CVs in `resumes/` were not modified.

## Positioning

| Track | Positioning statement | Evidence that carries it |
|---|---|---|
| Backend | Backend .NET developer with three years of hands-on software work. Builds ASP.NET Core APIs on SQL Server, Dapper and stored procedures with Keycloak security in retail. Shows integration design (idempotency, messaging, resilience) backed by tests. | Con Cung voucher and subscription work, Keycloak, ERP mappings. Partner Integration BFF: 202/409 idempotency, RabbitMQ, Polly, 42 xUnit tests including concurrency. |
| Full Stack | Ships features end to end in AngularJS + .NET in production retail, and builds modern Angular 19 (standalone components, RxJS, NgRx SignalStore, Native Federation). | Con Cung voucher workflows and template tool. Ecommerce-Admin and Layout-Store repos. BFF as backend depth. |
| AI | Software engineer who applies AI in retail work and builds GenAI services that are evaluated, fail closed and cite their sources, in Python/FastAPI. A junior AI application engineer with real backend depth. | Con Cung vector semantic search, n8n market-intelligence pipelines, Claude + MCP loop. Retail RAG Assistant: Qdrant, LangChain, abstention, evaluation that gates CI, 29 tests. Support Ticket triage: validated LLM output, masking, human review. |

## Main improvements over the originals

1. **Truthfulness.**
   - Removed claims the public repos contradict: the Support Ticket "10 HTTP scenarios / 120 / 720 / 1,000 decisions", and the outdated "8 queries / 2 documents".
   - Corrected "English: Conversational" to the confirmed level: good reading and writing, basic spoken.
   - Labelled the take-home and the AI-assisted lab with no repo as exactly that.
   - Said exactly what each evaluation covers.
   - Factual accuracy rose from about 78–89% to about 98–99%.
2. **Stronger verified evidence.**
   - Added the Partner Integration BFF (42 xUnit tests including a concurrency test, idempotency, RabbitMQ, Polly, Docker Compose).
   - Brought the RAG project up to date (parsing, Qdrant, LangChain, groundedness evaluation that gates CI).
   - Added the confirmed AI and retail-data work at Con Cung.
   - Added the employer context ("Vietnam's mother-and-baby retail chain").
3. **Targeting.** Each track now has:
   - a role headline;
   - a keyword line drawn from the market research;
   - a summary that explains the "3+ years" (FPT internship from Sep 2023, Con Cung since Nov 2023);
   - evidence ordered by relevance to that role.
4. **ATS.**
   - Single column with standard headings.
   - International phone format and LinkedIn link.
   - No ligatures; bullets in correct reading order.
   - Exact keyword forms (".NET Core", "RESTful API Design", "Retrieval-Augmented Generation").
   - The employer name is kept separate from its description.
5. **Design.**
   - Removed the random bold fragments, faded colours and icons.
   - Added a clear hierarchy (name, role, keyword line, sections) with one accent colour per track and high contrast.
   - The photo appears only in the designed version.
6. **Nothing dropped.** Every skill and experience item in the original CVs appears in the new ones. Projects not featured on a track are kept in an "Other projects" line, and the remaining skills are regrouped (for example "Other stacks", "Practices").

## Remaining weaknesses (honest)

- **No business-impact figures.** All numbers are counts of work items (7 calculations, 4 templates, 10 routes, 42 tests). This is the main reason the scores stop at 86–88.
- **Duplicate description.** The Con Cung retail-data bullet and the Layout-Store project describe related work. The Angular 19 work sits under projects, so "modern Angular" is not shown as professional experience.
- **Shared codebases.** Ecommerce-Admin and Layout-Store are single "push all" commits of Con Cung codebases (`CCI.*` namespaces). A hiring manager may ask about authorship and confidentiality.
- **Evidence gaps.**
  - The Retail Reliability Lab has no public repo.
  - The BFF has no CI.
  - The RAG evaluation never scores a real LLM.
- **LinkedIn address.** The URL contains Vietnamese diacritics. The link is encoded correctly, but the displayed text can be garbled by some portals.
- **GitHub profile.** The profile README at github.com/tvt987 still shows different dates and education unless the corrected README (`github-profile/README.md`) is published.
- **Dense skills blocks.** These are a consequence of keeping every original skill on one page.
- **English.** Basic spoken English will filter out some multinational roles. This is stated truthfully, not hidden.

## Market findings (summary)

From `market-research.md`, which used search summaries because the job boards were blocked:
- 18 Backend, 14 Full Stack and 12 AI postings.

**Backend.**
- C# / ASP.NET Core Web API and SQL Server appear almost everywhere.
- EF Core, microservices or message queues, unit testing, Docker or CI/CD, and Azure or AWS (as a plus) are frequent.
- Typical experience asked: 2–4 years.

**Full Stack.**
- ASP.NET Core + Angular + TypeScript + SQL Server, often with stored procedures and query tuning, and REST design.
- RxJS is named explicitly in some postings. NgRx is mostly asked at senior level.
- Typical experience asked: 2–3+ years.

**AI.**
- Python + LLM integration and RAG are near-universal; FastAPI, vector databases, agents and prompt engineering are common.
- Evaluation (groundedness, retrieval metrics) is the differentiator for junior and middle candidates.
- Production cloud LLM and MLOps appear at senior level.

## External tools

None were reachable. Resume Worded, Jobscan, Enhancv, TopCV and ITviec all failed DNS under this environment's network policy. **No external score exists or is claimed.** See `final-cvs/external-tools.md` for how to get real scores.

## Final QA

All checks passed on the delivered files (`final-cvs/qa-results.txt`):
- one A4 page;
- bullets in reading order;
- no ligatures;
- minimum font 9.5pt;
- all 8 links present;
- photo only on the designed version;
- no retired claims;
- required verified facts present;
- each DOCX renders to one page;
- `resumes/` unchanged.
