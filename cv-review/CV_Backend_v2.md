# CV_Backend — BẢN v2

Track: Backend Developer / .NET / C# / API Engineer.
**Đã sửa:** 2 con số không có cơ sở (R-1), claim sai về Ecommerce-Admin (R-2), "undeployed templates" (R-3).

---

```
Truong Van Tinh
Backend Developer | C# / .NET
+84 931 467 024 | tinhkun102@gmail.com
Ho Chi Minh City, Vietnam · Open to hybrid/remote | github.com/tvt987 | linkedin.com/in/<SLUG>
```

## Professional Summary

```
Backend Developer with 3+ years of software development experience building enterprise .NET services at
Con Cung: Web APIs over SQL Server with Dapper and stored procedures, ERP system integration, and
Keycloak-based authentication with role-based authorization. Comfortable owning a feature from database
access through to the API contract, and tracing defects across both.
```

**Vì sao mạnh hơn:** bản cũ là 3 câu rời rạc (*"Builds .NET web applications... Portfolio API development
covers 10 routes..."*). Bản này gom thành một năng lực liền mạch và kết bằng điều backend recruiter thực sự
quan tâm: **làm được end-to-end và debug xuyên tầng**.

## Work Experience

### Full Stack Developer | Con Cung | Nov 2023 – Present
```
• Built .NET voucher APIs for search, creation and bulk update, with promotion-rule validation and an
  Excel preview step that surfaces errors before a batch is committed.
• Implemented typed Dapper mappings over SQL Server stored-procedure results for 3-, 6- and 12-month
  subscription plans, covering 7 benefit calculations.
• Integrated Keycloak authentication (JWT, OAuth 2.0, OpenID Connect) with role-based authorization on
  application actions.
• Diagnosed and fixed SQL Server/Dapper retrieval defects, and verified ERP API request/response mappings
  between systems.
• Supported Docker and IIS deployment, and built an internal tool that previews and copies 4 generated
  code-template types: controller, repository, view and script.
```
> ⚠️ **R-6** — thiếu quy mô. Xem `QUESTIONS.md` Q1–Q4. Đây là điểm nâng CV này từ 8.0 lên 9.0.

> 📌 **Giữ job title `Full Stack Developer`** — đúng sự thật trên cả 3 CV. Định vị backend đã nằm ở
> headline và thứ tự bullet, không cần (và không được) đổi title.

### Frontend Intern | FPT Software | Sep 2023 – Nov 2023
```
• Built Angular/JavaScript components, integrated REST APIs for an e-commerce system and fixed mobile
  UI defects across devices.
```

## Projects

### Layout-Store — C#, ASP.NET Core, Dapper, PostgreSQL | Contributor
```
• Contributed 10 ASP.NET Core / PostgreSQL routes covering search, CRUD, approval and Excel import.
• Connected HTTP handlers to stored-procedure data access through async interfaces and dependency injection.
```
> 🔴 **CHƯA ĐƯỢC GẮN LINK REPO.** Repo này đang public và chứa source code Con Cung
> (`CCI.*`, `nexus.ingress.concung.io`). Xem **D-7** trong `platform-profiles/VERIFICATION_AND_GAPS.md`.
> Mô tả phần việc của bạn thì giữ được; link thì chờ xử lý D-7.

### Support Ticket AI Triage — Python, FastAPI, SQLite, Docker | Personal project
```
• Built FastAPI triage for 5 ticket categories with schema-validated model output and a deterministic
  rules fallback when validation fails.
• Made persistence idempotent with ticket ID as the primary key, so a replayed submission cannot
  overwrite a decision already recorded; protected human-review endpoints with a token.
• Masked emails and phone numbers before any ticket text reached the model provider, and kept raw
  customer messages out of storage.
• Covered the flow with unit, API and end-to-end tests against mocked LLM responses in GitHub Actions CI.
```
**Đã xoá:** ~~"Tested 10 HTTP scenarios"~~ và ~~"Validated 1,000 synthetic SQLite review decisions"~~ (R-1).
Cơ chế chống trùng ID là **thật** nên giữ lại — chỉ bỏ con số 1.000 không có cơ sở.

### Retail RAG Assistant — Python, FastAPI, TF-IDF | Personal project
```
• Implemented TF-IDF retrieval from scratch on the standard library alone — smoothed IDF, sublinear term
  frequency, L2-normalised cosine similarity — with no NumPy or scikit-learn in the core path.
• Discarded any LLM answer that cites no retrieved source, returning the extractive passages instead, so
  an ungrounded generation is never served.
• Gated quality in CI with a held-out evaluation: 8 questions over 2 documents, 6 correct top-3 matches
  and 2 correct abstentions, build failing on regression.
```
**Thay cho Ecommerce-Admin (R-2).** Bản cũ đưa `Ecommerce-Admin | C#, Angular, PostgreSQL, REST APIs` vào
CV backend, nhưng repo đó có **0 file `.cs`, 0 file `.sql`** — nó thuần frontend, không phải bằng chứng
backend. Thay bằng RAG Assistant vừa đúng sự thật, vừa là bằng chứng Python/API mạnh hơn.

### Retail Reliability Lab — FastAPI, Redis, SQLite
```
• Validated a Redis cache-aside pattern with a 60-second TTL, explicit invalidation and fallback to the
  source of truth during a simulated outage; 22 local API and cache tests against a real Redis instance.
• Reduced median local SQLite lookup from 3.63 ms to 0.005 ms over 200 queries on 100,000 synthetic rows.
```
> ⚠️ Đã bỏ `Azure` và câu *"Authored undeployed templates"* (R-3). Project không có repo công khai →
> cân nhắc bỏ nếu muốn CV gọn hơn (xem ghi chú trong `CV_AI_v2.md`).

## Skills and Technologies
```
Backend: C#, .NET, ASP.NET Core, ASP.NET MVC, Web API, REST API Design, Entity Framework / EF Core,
  Dapper, LINQ
Data: SQL Server, PostgreSQL, MySQL, Redis, Database Design, Stored Procedures, Query Optimization, Indexing
Security: Keycloak, JWT, OAuth 2.0, OpenID Connect, Claims, RBAC
Engineering: OOP, SOLID, Design Patterns, Dependency Injection, Repository Pattern, Clean Architecture,
  Microservices, Debugging, Performance Optimization
Testing and DevOps: Unit Testing, Integration Testing, Logging, Observability, Docker, CI/CD,
  GitHub Actions, IIS, Git, Git Flow, Swagger/OpenAPI, Azure, AWS
Python: Python, FastAPI, Pydantic, SQLite
Frontend Integration: Angular, AngularJS, TypeScript, JavaScript, RxJS
AI-assisted development: Claude, Cursor, GitHub Copilot, MCP
Practices: Agile/Scrum, Code Review, Problem Solving, Technical Documentation, Cross-team Collaboration
```
**Đã bỏ (R-7):** `Message Queues` · `Node.js, Java Spring Boot` · `Vector Databases` ·
`LLMs, Custom GPTs, AI Agents, n8n, OpenClaw, Agent Skills` · `React, HTML5, CSS3, Tailwind CSS`
(không liên quan CV backend) · `Communication` (đã có trong Practices).
**Đã chuyển:** `Azure, AWS` xuống cuối dòng DevOps, **không còn đứng riêng** (R-3).
**Đã thêm:** `Python, FastAPI, Pydantic, SQLite` thành nhóm riêng — nhiều JD backend .NET hiện có cả Python.

## Education
```
University of Information Technology (UIT), VNU-HCM | Information Technology | Graduated June 2026
Worked full-time at Con Cung while completing the degree.
```

## Languages
```
English: Conversational (professional reading and written communication) | Vietnamese: Native
```
