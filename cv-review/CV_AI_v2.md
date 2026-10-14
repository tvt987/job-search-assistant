# CV_AI — BẢN v2

Track: AI Application Engineer / Applied GenAI / Python & FastAPI.
Mọi dòng đều truy vết được về code (xem `EVIDENCE.md`). **Đã xoá cả 4 con số không có cơ sở.**

---

```
Truong Van Tinh
AI Application Engineer | Python & FastAPI
+84 931 467 024 | tinhkun102@gmail.com
Ho Chi Minh City, Vietnam · Open to hybrid/remote | github.com/tvt987 | linkedin.com/in/<SLUG>
```
> ⚠️ Thay `<SLUG>` sau khi chốt LinkedIn custom URL.

## Professional Summary

```
Software Engineer with 3+ years of development experience, currently building enterprise .NET retail
workflows at Con Cung. Builds Python/FastAPI LLM applications that are designed to fail safely:
retrieval with inline citations, answers rejected when they are not grounded in a cited source,
rule-based overrides the model cannot bypass, and PII masked before any text leaves the service.
```

**Vì sao mạnh hơn bản cũ:** bản cũ liệt kê tính năng (*"RAG document question-answering and ticket-triage
automation with citations, validated outputs, fallbacks"*). Bản này nêu **nguyên tắc thiết kế** —
*"designed to fail safely"* — rồi chứng minh bằng 4 cơ chế cụ thể. Đây là ngôn ngữ của người đã nghĩ về
độ tin cậy, không phải người mới ghép thư viện.

## Projects

### Retail RAG Assistant — Python, FastAPI, TF-IDF, SentenceTransformers, Docker
```
• Implemented TF-IDF retrieval from scratch on the standard library alone — smoothed IDF, sublinear term
  frequency and L2-normalised cosine similarity — with no NumPy, scikit-learn or HTTP dependency in the
  core path.
• Enforced grounding at the response layer: an LLM answer that cites no retrieved source ID is discarded
  and replaced with the extractive passages, so an ungrounded generation is never returned as an answer.
• Hardened the prompt against injection by instructing the model to treat retrieved excerpts as data and
  never as instructions, and pinned temperature to 0 for reproducible output.
• Made retrieval swappable behind one interface: TF-IDF by default, optional SentenceTransformers
  embeddings enabled by environment variable, each with its own score threshold for abstention.
• Gated quality in CI: a held-out evaluation of 8 questions across 2 documents returns 6 correct top-3
  matches and 2 correct abstentions, and the build fails on any regression.
```

### Support Ticket AI Triage — Python, FastAPI, LLM Integration, SQLite, Docker
```
• Automated triage across 5 ticket categories with validated priority and sentiment, falling back to
  deterministic rules whenever the model's response fails schema validation.
• Gave security rules authority over the model: a security ticket escalates even when the LLM classifies
  it as normal, so model error cannot downgrade a risk decision.
• Masked emails and phone numbers before any ticket text reaches the model provider, and kept raw
  customer messages out of storage entirely — only the resulting decision is persisted.
• Made persistence idempotent with ticket ID as the primary key, so a replayed submission cannot
  overwrite a decision already recorded, and protected human-review endpoints with a token.
• Covered the flow with unit, API and end-to-end tests against mocked LLM responses, running in
  GitHub Actions CI.
```

### Retail Reliability Lab — FastAPI, Redis, SQLite
```
• Validated a Redis cache-aside pattern with a 60-second TTL, explicit invalidation and fallback to the
  source of truth during a simulated cache outage, covered by 22 local API and cache tests against a
  real Redis instance.
• Reduced median local SQLite lookup from 3.63 ms to 0.005 ms over 200 queries on 100,000 synthetic rows.
```
> ⚠️ **Hai cảnh báo về project này:**
> 1. Đã **xoá** `Azure` khỏi tech stack và **xoá** câu *"Authored undeployed templates"* (R-3).
> 2. Project này **không có repo công khai** → không kiểm chứng được. Nếu bạn còn code, hãy đẩy lên một
>    repo (sau khi chắc không chứa gì của Con Cung). Nếu không còn, **cân nhắc bỏ hẳn** khỏi CV —
>    một project không thể kiểm chứng đứng cạnh hai project có link là điểm yếu, không phải điểm mạnh.

## Work Experience

### Full Stack Developer | Con Cung | Nov 2023 – Present
```
• Delivered voucher workflows end to end on .NET and AngularJS — search, creation and bulk update — with
  role-based permission checks, promotion-rule validation, and an Excel preview that surfaces errors
  before a batch is committed.
• Implemented 7 subscription benefit calculations across 3-, 6- and 12-month plans with side-by-side
  comparison between plan lengths.
• Integrated Keycloak authentication (JWT, OAuth 2.0, OpenID Connect) with role-based authorization on
  application actions; supported Docker and IIS deployment.
• Diagnosed and fixed SQL Server/Dapper retrieval defects and verified ERP API request/response mappings
  between systems.
```
> ⚠️ **R-6** — mục này còn thiếu quy mô. Xem `QUESTIONS.md` câu Q1–Q4.

### Frontend Intern | FPT Software | Sep 2023 – Nov 2023
```
• Built Angular/JavaScript components, integrated REST APIs for an e-commerce system and fixed mobile
  UI defects across devices.
```

## Skills and Technologies
```
AI Applications: RAG, Document Retrieval, TF-IDF, Semantic Embeddings, LLM Integration, Prompt
  Engineering, Output Validation, Grounding & Citation Enforcement, Human-in-the-loop Workflows, Evaluation
Python and APIs: Python, FastAPI, REST APIs, Pydantic, SQLite, Input Validation, Data Pipelines
Backend and Data: C#, .NET, ASP.NET Core, Dapper, SQL Server, PostgreSQL, Database Design, Query Optimization
Security and Privacy: Keycloak, JWT, OAuth 2.0, OpenID Connect, RBAC, PII Masking
Testing and DevOps: Unit Testing, Integration Testing, Docker, CI/CD, GitHub Actions, Git, Logging, Observability
Frontend: Angular, AngularJS, TypeScript, JavaScript, RxJS
AI-assisted development: Claude, Cursor, GitHub Copilot, MCP
Practices: Agile/Scrum, Code Review, Technical Documentation, Cross-team Collaboration
```
**Đã bỏ:** `Redis, Azure, AWS` khỏi dòng Infrastructure riêng (Redis chuyển vào mô tả lab; Azure/AWS không
đủ cơ sở) · `ChatGPT, n8n` · `NLP (text retrieval)` (trùng với Document Retrieval).
**Đã thêm:** `Grounding & Citation Enforcement`, `Output Validation`, `PII Masking`, `Pydantic` — đều có thật
trong code và đều là từ khoá JD AI đang tìm.

## Education
```
University of Information Technology (UIT), VNU-HCM | Information Technology | Graduated June 2026
Worked full-time at Con Cung while completing the degree.
```

## Languages
```
English: Conversational (professional reading and written communication) | Vietnamese: Native
```
