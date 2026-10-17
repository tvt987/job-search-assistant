# Verified facts, gaps and inconsistencies

Fact inventory built on 2026-10-17 before any rewrite. Sources: `APPLICANT_CONTEXT.md` (candidate-confirmed source of truth), the three original CVs (git `5e8e9db`), and the candidate's public GitHub repositories, cloned read-only and inspected file by file.

Status legend: **Verified-repo** = visible in public code; **Verified-candidate** = confirmed by the candidate, no public artefact; **Unsupported** = claimed somewhere but contradicted or not found in the linked evidence.

## A. Identity, education, languages

| Fact | Status | Source |
|---|---|---|
| Truong Van Tinh, Ho Chi Minh City, +84 931 467 024, tinhkun102@gmail.com | Verified-candidate | APPLICANT_CONTEXT §2 |
| github.com/tvt987, linkedin.com/in/trương-văn-tình-651b12289 | Verified-candidate | APPLICANT_CONTEXT §2, candidate message |
| University of Information Technology (UIT), VNU-HCM, Information Technology, graduated 2026 | Verified-candidate | APPLICANT_CONTEXT §2; candidate confirmed CV is correct over GitHub README |
| English: good reading and writing, basic spoken, no certificate | Verified-candidate | APPLICANT_CONTEXT §2 |
| Certifications: none | Verified-candidate | APPLICANT_CONTEXT §2 |
| 3+ years of software development since 09/2023 **including** the FPT frontend internship; .NET work since 11/2023 (just under 3 years) | Verified-candidate | APPLICANT_CONTEXT §2 |

## B. Employment

### Con Cung — Full Stack Developer, Nov 2023 – Present (Verified-candidate)
Vietnam's mother-and-baby retail chain (public information).

| Responsibility / result | Evidence |
|---|---|
| .NET voucher APIs: search, create, update; permission checks, promotion validation, Excel preview before batch creation | candidate |
| 7 subscription benefit calculations for 3-, 6- and 12-month plans, side-by-side comparison | candidate |
| SQL Server + Dapper + stored procedures; fixed retrieval defects; verified ERP API request/response mappings | candidate |
| Keycloak JWT / OAuth 2.0 / OIDC authentication, role-based authorization | candidate |
| Supported Docker and IIS deployment | candidate |
| Preview/copy tool for 4 generated template types (controller, repository, view, script) | candidate |
| Retail data structures for shelves, facings, display groups (store-layout optimization) | candidate; **corroborated** by Layout-Store code (`LayoutShelfBracketsController`, `InstanceDisplayGroupsController`) |
| Vector semantic search in a commerce portal | candidate; **corroborated** by Ecommerce-Admin features (`personalized-search`, `search-playground`, `synonyms`, `stopwords`) |
| n8n pipelines for competitor scraping and market intelligence | candidate |
| AI-assisted delivery: Custom GPTs, prompt engineering; autonomous debug/test loop with Claude, Agent Skills, MCP | candidate |

### FPT — Frontend Intern, Sep 2023 – Nov 2023 (Verified-candidate)
Angular / JavaScript components, e-commerce REST API integration, mobile UI defect fixes.

## C. Projects

| Project | What the public repository actually shows | Status |
|---|---|---|
| **Partner Integration BFF** (take-home), `4005e30` | .NET 8 (3 projects + tests), API-key auth with constant-time compare, FluentValidation, idempotency on partnerId + transactionReference (202 replay / 409 conflict), RabbitMQ or in-memory queue, Polly retry + timeout around a dummy verifier that times out ~30%, ProblemDetails mapping, `/health`, Docker Compose. **42 xUnit tests** (`[Fact]`/`[Theory]`, 17 `InlineData` cases) including `ProcessAsync_WhenConcurrentSamePayload_PublishesOnce` and `WebApplicationFactory` endpoint tests. No CI workflow. | Verified-repo |
| **Retail RAG Assistant**, `fea7f83` on `main` | Markdown/TXT/HTML/PDF parsing and preprocessing; TF-IDF or SentenceTransformers retrieval; Qdrant vector store (sparse TF-IDF or dense); LangChain LCEL pipeline with citation check; FastAPI `/ask`, `/health`, `/documents`; abstention and extractive fallback; evaluation of 16 questions over 3 documents (hit rate, MRR, abstention, fact recall, groundedness); 29 tests; two CI jobs green on `main` (run 38710004715). | Verified-repo |
| **Support Ticket AI Triage**, `4573d6d` | 4 categories + `other` (5 labels); rules baseline; optional OpenAI-compatible LLM call whose output is schema-validated (category, priority, sentiment, confidence); urgent-keyword safety gate forces high priority and human review; email/phone redaction before the model; token-protected review API; SQLite queue that stores decisions without the message text; duplicate ticket → 409 / `IntegrityError` without overwriting; **7 tests**; 5-case synthetic evaluation; CI green. | Verified-repo |
| **Ecommerce-Admin**, `3cc8cbc` | Angular 19.2 standalone components, `@ngrx/signals` SignalStore (27 API stores), RxJS, Tailwind, Native Federation (micro-frontend), .NET 8 host project. Feature areas: keywords, synonyms, stopwords, personalized search, search playground, keyword-sponsor campaigns, category rankings, landing pages, products, product-description editor, sync jobs. Single commit, no README at root, no per-author history. | Verified-repo (codebase); personal scope = "built admin screens" per candidate |
| **Layout-Store**, `d3fce2d` | ASP.NET Core API (.NET 6) + Angular 19 front end; PostgreSQL via Npgsql + Dapper; stored procedures; planogram domain (shelf brackets, display groups, products, categories); ~200 HTTP route attributes across the codebase. Single commit. | Verified-repo (codebase); personal scope "10 routes" = candidate statement, not separable in history |
| **Retail Reliability Lab** | No public repository found among the candidate's repos. | Verified-candidate only (unlinked) |

## D. Claims that need evidence

| Claim (where it appears) | Finding | Decision in final CVs |
|---|---|---|
| Support Ticket: "10 HTTP scenarios with mocked LLM responses", "120 synthetic schema combinations", "720 urgent-rule cases", "1,000 synthetic SQLite review decisions" (original AI and Backend CVs, APPLICANT_CONTEXT) | **Not present** in any commit of the linked repo; the repo has 7 tests and a 5-case evaluation. A hiring manager who clicks the link would see the mismatch. | Removed. Replaced with what the repo shows. Restore only after committing the scripts that produce these numbers. |
| Retail Reliability Lab: 22 tests on real Redis, median 3.63 ms → 0.005 ms over 200 queries on 100,000 synthetic rows | No public artefact; not contradicted. | Kept, labelled "AI-assisted lab", no link. Flagged as unverifiable to an external reader. |
| Layout-Store "10 routes" | Codebase is shared; individual contribution cannot be shown from a single commit. | Kept as stated by the candidate ("contributed"). |
| Azure, AWS | Only "authored undeployed Docker Compose and Azure templates" (lab). No deployment evidence. | Listed as familiarity in skills, never as delivered infrastructure. |
| Microservices | BFF is a two-service system with a queue; no production microservices evidence. | Listed in skills; bullets describe the BFF concretely instead of claiming microservices experience. |
| ASP.NET MVC, MySQL, Node.js, Java Spring Boot, React, OpenClaw | Listed in original skills; no project evidence in repos. | Kept in a lower-priority "also used" line on the tracks where they add nothing; not used as headline keywords. |
| Business impact at Con Cung (users, volume, time saved) | Not available; candidate chose not to estimate. | No impact numbers invented. Strong qualitative statements only. |

## E. Inconsistencies found

| Inconsistency | Status |
|---|---|
| GitHub profile README: Con Cung from 07/2024, 2+ years, Galaxy Industrial and VNPT internships, UIT 2024–2025, FPT Polytechnic | Candidate confirmed the CV is correct. Corrected README prepared at `github-profile/README.md`; **must be pasted into `tvt987/tvt987` before applying** — a recruiter comparing the two will see different dates. |
| Original CVs: phone `0931467024` vs `+84 931 467 024`; title "Software Engineer" in the AI summary vs "AI Application Engineer" header | Normalised in rewrite. |
| Original CVs said "3+ years" next to ".NET" in places; .NET experience is just under 3 years | Final CVs say "3+ years of software development" only. |
| Backend CV lists Ecommerce-Admin as "C#, Angular, PostgreSQL, REST APIs"; repo is an Angular front end with a .NET 8 host | Final backend CV describes it accurately or omits it. |
| Layout-Store and Ecommerce-Admin are Con Cung codebases (`CCI.*` namespaces, "E-Commerce Mẹ & Bé" README) published as personal repos | Risk noted (an employer reading them may question confidentiality). Candidate decided no action; CVs keep them as projects with neutral wording. |

## F. Missing information that would strengthen the CVs

1. Any real scale or impact figure from Con Cung (vouchers per month, users of the admin, time saved by the template tool, defects resolved).
2. Team size and the candidate's role in it (owner of a module, reviewer, on-call).
3. GPA or graduation classification; thesis topic.
4. A public repo for Retail Reliability Lab, or the scripts behind the Support Ticket validation numbers.
5. CI for Partner Integration BFF (42 tests exist but nothing runs them publicly).
6. Linux usage (frequent in AI job ads; not claimed because not confirmed).
