# CV_FullStack — BẢN v2

Track: Full Stack Developer / .NET + Angular.
**Đây là bản mạnh nhất trong ba bản ngay từ đầu** — không chứa con số bịa nào. Thay đổi ở đây chủ yếu là
làm sắc thêm, không phải sửa lỗi.

---

```
Truong Van Tinh
Full Stack Developer | .NET & Angular
+84 931 467 024 | tinhkun102@gmail.com
Ho Chi Minh City, Vietnam · Open to hybrid/remote | github.com/tvt987 | linkedin.com/in/<SLUG>
```

## Professional Summary

```
Full Stack Developer with 3+ years of software development experience delivering .NET and AngularJS
voucher and subscription workflows at Con Cung, over SQL Server with Dapper, ERP integration and
Keycloak authentication. Portfolio work covers modern Angular 19 with RxJS and NgRx SignalStore, and
Python/FastAPI services. Comfortable owning a feature from the database through the API to the screen.
```

**Thay đổi:** bản cũ kết ở *"Angular 19 portfolio work integrates authenticated APIs with RxJS and NgRx
SignalStore"* — đúng nhưng thiếu kết luận. Câu cuối mới nói thẳng giá trị của một full-stack: **làm trọn
một feature xuyên ba tầng**. Đây là câu recruiter full-stack tìm.

## Work Experience

### Full Stack Developer | Con Cung | Nov 2023 – Present
```
• Delivered voucher search, creation and bulk-update workflows across an AngularJS front end and .NET
  Web APIs, with role-based permission checks, promotion-rule validation, and an Excel preview that
  surfaces errors before a batch is committed.
• Implemented 7 subscription benefit calculations across 3-, 6- and 12-month plans, with side-by-side
  comparison between plan lengths.
• Integrated Keycloak authentication (JWT, OAuth 2.0, OpenID Connect) with role-based authorization on
  application actions; supported Docker and IIS deployment.
• Diagnosed and fixed SQL Server/Dapper retrieval defects, and verified ERP API request/response mappings
  between systems.
• Built an AngularJS tool that previews and copies 4 generated code-template types — controller,
  repository, view and script — removing a repeated manual step from the team's workflow.
```
> ⚠️ **R-6** — thiếu quy mô. Xem `QUESTIONS.md` Q1–Q4.

> 📌 Bullet cuối đã thêm *"removing a repeated manual step from the team's workflow"* — đây là
> **suy luận hợp lý** từ bản chất một tool preview/copy template. Nếu bạn thấy không đúng thực tế thì
> cắt nửa sau câu.

### Frontend Intern | FPT Software | Sep 2023 – Nov 2023
```
• Built Angular/JavaScript components, integrated REST APIs for an e-commerce system and fixed mobile
  UI defects across devices.
```

## Projects

### Ecommerce-Admin — Angular 19, TypeScript, RxJS, NgRx SignalStore | Frontend development
```
• Built responsive Angular 19 admin screens and integrated authenticated REST APIs for search, creation
  and updates.
• Managed loading, success and error states across admin workflows with RxJS and NgRx SignalStore,
  keeping async state handling consistent between screens.
```
> 🔴 **CHƯA ĐƯỢC GẮN LINK REPO** — repo public này chứa branding/hạ tầng Con Cung
> (`cdn1.concung.com`, `123test.concung.com`). Xem **D-7**.
> ✅ Claim kỹ thuật đã verify: `@angular/core 19.2.14`, `@ngrx/signals 19.2.1`, `signalStore` trong 29 file.

### Layout-Store — C#, ASP.NET Core, Dapper, PostgreSQL, Angular | Contributor
```
• Contributed 10 ASP.NET Core / PostgreSQL routes for search, CRUD, approval and Excel import, wiring
  HTTP handlers to stored-procedure access through async interfaces and dependency injection.
• Contributed Angular workflows and PostgreSQL data structures for store layouts and product placement.
```
> 🔴 **CHƯA ĐƯỢC GẮN LINK REPO** — xem **D-7**.
> ✅ Đã verify repo có **cả** backend (Npgsql 25 file, Dapper 33 file, 21 file `.sql`) **và** frontend
> (Angular 21, 29 component, 92 service) → **cả hai bullet đều đúng**. Bản CV cũ chỉ ghi bullet Angular;
> gộp cả hai vào thì mạnh hơn hẳn cho vị trí full-stack.

### Retail RAG Assistant — Python, FastAPI, TF-IDF | Personal project
```
• Implemented TF-IDF retrieval from scratch on the standard library alone — smoothed IDF, sublinear term
  frequency, L2-normalised cosine similarity — with no NumPy or scikit-learn in the core path.
• Discarded any LLM answer citing no retrieved source, returning extractive passages instead, so an
  ungrounded generation is never served.
• Gated quality in CI: 8 held-out questions over 2 documents give 6 correct top-3 matches and 2 correct
  abstentions, with the build failing on regression.
```
**Thay cho Retail Reliability Lab.** Lab không có repo công khai; RAG Assistant có link và thể hiện
kỹ năng mạnh hơn. Nếu muốn giữ cả hai, Lab nên xuống cuối.

## Skills and Technologies
```
Frontend: Angular, Angular 19, AngularJS, TypeScript, JavaScript, RxJS, NgRx SignalStore, HTML5, CSS3,
  Tailwind CSS, React
Backend: C#, .NET, ASP.NET Core, ASP.NET MVC, Web API, REST API Design, Entity Framework / EF Core,
  Dapper, LINQ
Data: SQL Server, PostgreSQL, MySQL, Redis, Database Design, Stored Procedures, Query Optimization, Indexing
Security: Keycloak, JWT, OAuth 2.0, OpenID Connect, Claims, RBAC
Engineering: OOP, SOLID, Design Patterns, Dependency Injection, Repository Pattern, Clean Architecture,
  Microservices, Debugging, Performance Optimization
Testing and DevOps: Unit Testing, Integration Testing, Logging, Observability, Docker, CI/CD,
  GitHub Actions, IIS, Git, Git Flow, Swagger/OpenAPI, Azure, AWS
Python: Python, FastAPI, Pydantic, SQLite
AI-assisted development: Claude, Cursor, GitHub Copilot, MCP
Practices: Agile/Scrum, Code Review, Problem Solving, Technical Documentation, Cross-team Collaboration
```
**Đã bỏ (R-7):** `Message Queues` · `Node.js, Java Spring Boot` · `Vector Databases` ·
`LLMs, Custom GPTs, AI Agents, n8n, OpenClaw, Agent Skills` · `Communication` (trùng).
**Đã thêm:** `Angular 19`, `NgRx SignalStore` tách riêng (từ khoá JD hay tìm, và đã verify trong code) ·
nhóm `Python` riêng.
**Đã chuyển:** `Azure, AWS` xuống cuối dòng DevOps.

## Education
```
University of Information Technology (UIT), VNU-HCM | Information Technology | Graduated June 2026
Worked full-time at Con Cung while completing the degree.
```

## Languages
```
English: Conversational (professional reading and written communication) | Vietnamese: Native
```
