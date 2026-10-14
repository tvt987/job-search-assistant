# MASTER PROFILE CONTENT — TRUONG VAN TINH

**Nguồn dữ liệu:** `resumes/CV_Backend_TruongVanTinh.pdf`, `resumes/CV_FullStack_TruongVanTinh.pdf`,
`resumes/CV_AI_TruongVanTinh.pdf` + `APPLICANT_CONTEXT.md`.
**Nguyên tắc:** mọi câu trong file này đều truy vết được về CV hoặc context đã xác minh.
Không thêm công ty, dự án, chứng chỉ, con số hay số năm kinh nghiệm nào không có trong nguồn.

> Đây là **khối nội dung dùng chung**. Mỗi nền tảng có file riêng (`linkedin.md`, `itviec.md`, ...)
> chỉ map field của form đó sang các khối ở đây.

---

## 1. Identity block (giống nhau trên mọi nền tảng)

| Field | Giá trị |
| :--- | :--- |
| Full name | `Truong Van Tinh` |
| Tên tiếng Việt | `Trương Văn Tình` |
| Email | `tinhkun102@gmail.com` |
| Phone (quốc tế) | `+84 931 467 024` |
| Phone (nội địa) | `0931467024` |
| Location | `Ho Chi Minh City, Vietnam` |
| GitHub | `https://github.com/tvt987` |
| Ngôn ngữ | English — Conversational *(tuyệt đối không khai Fluent / Native / Bilingual)* |

**Không điền** (chưa xác minh): ngày sinh, số CCCD, địa chỉ nhà chi tiết, giới tính, tình trạng hôn nhân,
LinkedIn URL hiện tại, ảnh profile. Xem `VERIFICATION_AND_GAPS.md`.

---

## 2. Headline — 4 biến thể

Chọn theo track của nền tảng/vị trí. Độ dài đã kiểm tra ≤ 220 ký tự (giới hạn headline LinkedIn).

### 2.1 FullStack (mặc định — dùng khi nền tảng chỉ cho 1 profile)
```
Full Stack Developer | .NET & Angular | ASP.NET Core · C# · SQL Server/Dapper · Keycloak/OAuth2 · Angular 19 · RxJS/NgRx | Python & FastAPI for applied GenAI | Ho Chi Minh City
```

### 2.2 Backend
```
Backend Developer | C# / .NET | ASP.NET Core · Web API · SQL Server · Dapper · EF Core · PostgreSQL · Redis · Keycloak/JWT/OAuth 2.0 · Docker · CI/CD | Clean Architecture | Ho Chi Minh City
```

### 2.3 AI Application Engineer
```
AI Application Engineer | Python & FastAPI | RAG · Document Retrieval · TF-IDF/Embeddings · LLM Integration & Output Validation · Human-in-the-loop | Enterprise .NET background | HCMC
```

### 2.4 Bản ngắn (cho field "Job title" chỉ 1 dòng, ~60 ký tự)
- Backend: `Backend Developer | C# / .NET / ASP.NET Core`
- FullStack: `Full Stack Developer | .NET & Angular`
- AI: `AI Application Engineer | Python & FastAPI`

---

## 3. About / Professional Summary

### 3.1 Bản dài — EN (LinkedIn About, giới hạn 2.600 ký tự)

```
Full Stack Developer with 3+ years of software development experience (since Sep 2023), currently building enterprise .NET and AngularJS applications at Con Cung in Ho Chi Minh City.

WHAT I BUILD DAY TO DAY
• Voucher workflows end to end: .NET Web APIs for search, creation and updates, with permission checks, promotion validation and Excel preview before batch creation.
• 7 subscription benefit calculations across 3-, 6- and 12-month plans, with side-by-side comparison.
• Data access on SQL Server with Dapper and stored procedures — typed result mappings, plus diagnosing and fixing retrieval defects.
• ERP integration: verifying API request/response mappings between systems.
• Authentication and authorization with Keycloak, JWT, OAuth 2.0 and OpenID Connect, including role-based access control.
• Deployment support on Docker and IIS.
• An AngularJS preview/copy tool covering 4 generated template types: controller, repository, view and script.

PORTFOLIO & OPEN SOURCE
• Layout-Store — contributed 10 ASP.NET Core / PostgreSQL routes for search, CRUD, approval and Excel import, connecting HTTP handlers to stored procedures through async interfaces and dependency injection.
• Ecommerce-Admin — Angular 19 admin screens with TypeScript, RxJS and NgRx SignalStore, managing loading, success and error states across workflows.
• Retail RAG Assistant — FastAPI document question-answering with cited retrieval (TF-IDF/cosine, optional SentenceTransformers), low-score abstention and extractive fallback when LLM calls fail. On 8 synthetic queries over 2 documents: 6 correct top-3 matches and 2 correct abstentions, CI green.
• Support Ticket AI Triage — LLM-assisted triage across 5 ticket categories with priority/sentiment validation, rules fallback, token-protected human review and contact masking; raw ticket text is never stored. 10 HTTP scenarios tested, 120 schema combinations validated, 1,000 SQLite review decisions verified.

HOW I WORK
Reliability first: validated outputs, explicit fallbacks, tests that actually run in CI, and a human in the loop wherever a wrong answer would be expensive.

Stack: C#, .NET, ASP.NET Core, Web API, Dapper, EF Core, SQL Server, PostgreSQL, Redis, Angular, AngularJS, TypeScript, RxJS, NgRx, Python, FastAPI, Docker, CI/CD, Git.

Open to Backend .NET, Full Stack .NET + Angular, and AI Application Engineer roles in Ho Chi Minh City — on-site, hybrid or remote.
tinhkun102@gmail.com | github.com/tvt987
```

### 3.2 Bản trung — EN (~700 ký tự, cho ITviec / VietnamWorks / Glints "About me")

```
Full Stack Developer with 3+ years of software development experience. At Con Cung I build .NET and AngularJS voucher and subscription workflows, with SQL Server/Dapper and stored procedures, ERP API integration, and Keycloak JWT/OAuth 2.0/OIDC authentication with role-based authorization; I also support Docker and IIS deployment.

Alongside enterprise work, I build Python/FastAPI applications: a RAG document assistant with cited retrieval, low-score abstention and extractive fallback, and an LLM ticket-triage service with validated outputs, rules fallback and token-protected human review — both covered by automated tests running in CI.

Open to Backend .NET, Full Stack .NET + Angular and AI Application Engineer roles in Ho Chi Minh City.
```

### 3.3 Bản trung — VI (cho nền tảng ưu tiên tiếng Việt: CareerViet, TopDev)

```
Full Stack Developer với hơn 3 năm kinh nghiệm phát triển phần mềm. Tại Con Cung, tôi phát triển và bảo trì các workflow voucher và subscription trên .NET và AngularJS: xây dựng Web API cho tìm kiếm/tạo/cập nhật, kiểm tra quyền, validate promotion và preview Excel trước khi tạo batch; triển khai 7 phép tính quyền lợi gói thành viên cho các kỳ 3, 6 và 12 tháng.

Về dữ liệu và bảo mật, tôi làm việc với SQL Server, Dapper và stored procedures, tích hợp ERP API, đồng thời triển khai xác thực Keycloak JWT / OAuth 2.0 / OpenID Connect và phân quyền theo vai trò (RBAC). Tôi cũng hỗ trợ triển khai trên Docker và IIS.

Ngoài công việc chính, tôi xây dựng ứng dụng Python/FastAPI: một trợ lý hỏi đáp tài liệu theo hướng RAG có dẫn nguồn, biết từ chối trả lời khi độ tin cậy thấp; và một hệ thống phân loại ticket dùng LLM có validate kết quả, fallback theo rule và bước review của con người. Cả hai đều có test tự động chạy trên CI.

Mục tiêu: vị trí Backend .NET, Full Stack .NET + Angular hoặc AI Application Engineer tại TP.HCM.
```

### 3.4 Bản ngắn — EN (~300 ký tự, cho field summary bị giới hạn)

```
Full Stack Developer, 3+ years. Enterprise .NET + AngularJS at Con Cung: Web APIs, SQL Server/Dapper, stored procedures, ERP integration, Keycloak JWT/OAuth 2.0/OIDC with RBAC, Docker/IIS. Also Python/FastAPI applied-AI projects (RAG with citations, LLM triage with validated outputs) tested in CI.
```

---

## 4. Work Experience — nhập đúng từng ký tự

> **Quan trọng:** job title tại Con Cung là **Full Stack Developer** trên cả 3 CV.
> Không được đổi thành "Backend Developer" dù đang ứng tuyển backend — đó là sai sự thật.
> Muốn nhấn backend thì đổi **headline** và thứ tự bullet, không đổi job title.

### 4.1 Con Cung — hiện tại

| Field | Giá trị |
| :--- | :--- |
| Job title | `Full Stack Developer` |
| Company | `Con Cung` |
| Employment type | `Full-time` |
| Location | `Ho Chi Minh City, Vietnam` |
| Start | `November 2023` |
| End | `Present` (tick "I am currently working in this role") |
| Industry | Retail *(Con Cung là chuỗi bán lẻ mẹ & bé)* |

**Bullets — thứ tự cho track FullStack (mặc định):**
```
• Delivered AngularJS/.NET voucher search, creation and update workflows with permission checks, promotion validation and Excel preview before batch creation.
• Implemented 7 subscription benefit calculations across 3-, 6- and 12-month plans, with side-by-side comparisons.
• Resolved SQL Server/Dapper retrieval defects and verified ERP API request/response mappings.
• Implemented Keycloak JWT/OAuth 2.0/OIDC authentication and role-based authorization; supported Docker/IIS deployment.
• Built an AngularJS preview/copy tool for 4 generated template types: controller, repository, view and script.
```

**Bullets — thứ tự cho track Backend** (đảo lên các bullet API/data, bỏ nhấn AngularJS):
```
• Delivered .NET voucher APIs for search, creation and updates; added promotion validation and Excel preview before batch creation.
• Implemented typed Dapper mappings for SQL Server stored-procedure results across 3-, 6- and 12-month subscription plans.
• Resolved SQL Server/Dapper retrieval defects and verified ERP API mappings.
• Implemented Keycloak JWT/OAuth 2.0/OIDC authentication and role-based authorization for application actions.
• Built a preview/copy tool for 4 generated template types: controller, repository, view and script.
```

**Bullets — thứ tự cho track AI** (bản nén 3 dòng, dành chỗ cho project):
```
• Delivered AngularJS/.NET voucher workflows, 7 subscription benefit calculations and a tool for 4 generated code-template types.
• Implemented Keycloak JWT/OAuth 2.0/OIDC authentication and role-based authorization; supported Docker/IIS deployment.
• Resolved SQL Server/Dapper retrieval defects and verified ERP API request/response mappings.
```

### 4.2 FPT — thực tập

| Field | Giá trị |
| :--- | :--- |
| Job title | `Frontend Intern` |
| Company | `FPT` |
| Employment type | `Internship` |
| Location | `Ho Chi Minh City, Vietnam` |
| Start | `September 2023` |
| End | `November 2023` |

**Bullets (giống nhau trên cả 3 track):**
```
• Developed Angular/JavaScript components and integrated REST APIs for an e-commerce system.
• Corrected mobile UI defects across devices.
```

---

## 5. Education

| Field | Giá trị |
| :--- | :--- |
| School | `University of Information Technology (UIT), VNU-HCM` |
| Tên tiếng Việt | `Trường Đại học Công nghệ Thông tin, ĐHQG-HCM` |
| Degree | `Bachelor's degree` |
| Field of study | `Information Technology` |
| Graduation year | `2026` |
| Graduation **month** | ⚠️ **NEEDS_USER_INPUT** — CV chỉ ghi "Graduated 2026", không có tháng. Xem `VERIFICATION_AND_GAPS.md` mục G-1. |
| GPA | Không điền (không có trong CV) |

---

## 6. Projects — 5 mục

Thứ tự ưu tiên thay đổi theo track. Repo chỉ điền với 4 project đầu; **Retail Reliability Lab không có repo công khai trong nguồn** → để trống link.

### P1. Layout-Store
- **Role:** Contributor
- **Repo:** `https://github.com/tvt987/Layout-Store`
- **Tech:** C#, ASP.NET Core, Dapper, PostgreSQL, Angular
- **Mô tả:**
```
Contributed 10 ASP.NET Core / PostgreSQL routes covering search, CRUD, approval and Excel import. Connected HTTP handlers to stored-procedure data access through async interfaces and dependency injection.
```

### P2. Ecommerce-Admin
- **Role:** Frontend development
- **Repo:** `https://github.com/tvt987/Ecommerce-Admin`
- **Tech:** Angular 19, TypeScript, RxJS, NgRx SignalStore
- **Mô tả:**
```
Built responsive Angular 19 admin screens and integrated authenticated REST APIs for search, creation and updates. Managed loading, success and error states with RxJS and NgRx SignalStore across admin workflows.
```

### P3. Retail RAG Assistant
- **Role:** Personal project
- **Repo:** `https://github.com/tvt987/retail-rag-assistant`
- **Tech:** Python, FastAPI, TF-IDF, SentenceTransformers, Docker
- **Mô tả:**
```
Built cited document retrieval with TF-IDF/cosine similarity over paragraph chunks, with optional SentenceTransformers embeddings. Developed FastAPI question, document and health endpoints with low-score abstention and extractive fallback when LLM calls fail. Evaluated retrieval on 8 synthetic queries across 2 documents: 6 correct top-3 matches and 2 correct abstentions; GitHub Actions CI passed.
```

### P4. Support Ticket AI Triage
- **Role:** Personal project
- **Repo:** `https://github.com/tvt987/support-ticket-ai-triage`
- **Tech:** Python, FastAPI, LLM Integration, SQLite, Docker
- **Mô tả:**
```
Automated LLM-assisted triage for 5 ticket categories with priority/sentiment validation and a rules-based fallback. Protected human-review endpoints with a token, masked contact data and added urgent-rule overrides; raw ticket text is excluded from storage. Tested 10 FastAPI HTTP scenarios with mocked LLM responses (CI passed on main), validated 120 synthetic schema combinations and 720 urgent-rule cases, and verified SQLite persistence for 1,000 review decisions.
```

### P5. Retail Reliability Lab
- **Role:** AI-assisted lab *(dùng đúng nhãn này — không gọi là production system)*
- **Repo:** — *(không có trong nguồn, để trống)*
- **Tech:** FastAPI, Redis, SQLite, Azure
- **Mô tả:**
```
Validated a Redis cache-aside pattern with a 60-second TTL, invalidation and outage fallback; 22 local API/cache tests passed against a real Redis instance. Reduced local SQLite median lookup from 3.63 ms to 0.005 ms over 200 queries on 100,000 synthetic rows. Authored Docker Compose and Azure templates (not deployed).
```

**Thứ tự project theo track:**
- Backend: P1 → P5 → P4 → P2
- FullStack: P2 → P1 → P3 → P5
- AI: P3 → P4 → P5 → P1

---

## 7. Skills — danh sách đã xếp hạng

Xếp theo **thứ tự ưu tiên tìm kiếm của recruiter**. Khi nền tảng giới hạn số skill, cắt từ dưới lên.

### Nhóm A — luôn đưa lên đầu (Top 5 pin trên LinkedIn)
1. `C#`
2. `.NET` *(và `ASP.NET Core`)*
3. `SQL Server`
4. `Angular`
5. `RESTful API` / `Web API`

### Nhóm B — core, phải có
`ASP.NET Core` · `ASP.NET MVC` · `Web API` · `REST API Design` · `Dapper` · `Entity Framework Core` · `LINQ` ·
`PostgreSQL` · `MySQL` · `Redis` · `Stored Procedures` · `Database Design` · `Query Optimization` · `Indexing` ·
`Angular` · `AngularJS` · `TypeScript` · `JavaScript` · `RxJS` · `NgRx` · `HTML5` · `CSS3` · `Tailwind CSS` · `React`

### Nhóm C — bảo mật & kiến trúc
`Keycloak` · `JWT` · `OAuth 2.0` · `OpenID Connect` · `RBAC` · `Claims` ·
`OOP` · `SOLID` · `Design Patterns` · `Dependency Injection` · `Repository Pattern` ·
`Clean Architecture` · `Microservices`

### Nhóm D — DevOps & testing
`Docker` · `CI/CD` · `GitHub Actions` · `Git` · `Git Flow` · `IIS` · `Swagger/OpenAPI` ·
`Unit Testing` · `Integration Testing` · `Logging` · `Observability` · `Azure` · `AWS`

### Nhóm E — Python & AI
`Python` · `FastAPI` · `RAG` · `LLM Integration` · `Prompt Engineering` · `Document Retrieval` ·
`TF-IDF` · `Semantic Embeddings` · `SQLite` · `Data Pipelines` · `Input Validation` ·
`Human-in-the-loop Workflows` · `MCP` · `AI Agents`

### Nhóm F — soft skills (điền sau cùng, nếu còn chỗ)
`Agile/Scrum` · `Code Review` · `Problem Solving` · `Technical Documentation` · `Cross-team Collaboration`

### ⚠️ Nhóm G — CÓ trong CV nhưng KHÔNG nên đẩy lên profile
`Node.js` · `Java Spring Boot` · `Message Queues` · `Vector Databases`

**Lý do:** CV gắn nhãn các mục này là *"Additional stacks"*, và `APPLICANT_CONTEXT.md` không liệt kê chúng
trong phần định vị năng lực. Đưa lên profile sẽ kéo về JD lệch stack, và khi recruiter hỏi "mấy năm kinh nghiệm
Node.js?" thì không có dữ liệu để trả lời trung thực. Giữ trong CV PDF, không bỏ vào skill tag của profile.
Xem `VERIFICATION_AND_GAPS.md` mục D-3.

**`Azure` / `AWS`:** để ở nhóm D, **không đưa vào headline**. Nguồn duy nhất là Retail Reliability Lab, và
CV ghi rõ template Azure *"not deployed"* → không đủ cơ sở để quảng bá như năng lực cloud chính.

---

## 8. Số năm kinh nghiệm — dùng con số nào

Mốc tính: FPT từ **09/2023**, Con Cung từ **11/2023**. Hôm nay: **14/10/2026**.

| Câu hỏi | Trả lời an toàn | Cơ sở |
| :--- | :--- | :--- |
| Total years of experience | `3+ years` | 09/2023 → nay = 3 năm 1 tháng |
| Years of C# / .NET | `2+ years` | Con Cung 11/2023 → nay = 2 năm 11 tháng. `screening_qa.md` đã chốt "2+" — giữ nguyên, đừng tự nâng lên 3. |
| Years of Angular / AngularJS | `2+ years` | FPT (Angular) + Con Cung (AngularJS) |
| Years of SQL / Database | `2+ years` | SQL Server/Dapper tại Con Cung |
| Years of Python / FastAPI | ⚠️ **NEEDS_USER_INPUT** | Chỉ có project cá nhân, nguồn không ghi thời điểm bắt đầu → không suy đoán. Mục G-2. |
| Experience level | `Middle` / `Mid-level` | 3+ năm, không phải Fresher, chưa đủ cơ sở khai Senior |

---

## 9. Khối "Open to work" / nguyện vọng

| Field | Giá trị |
| :--- | :--- |
| Job titles muốn nhận | `Backend Developer`, `.NET Developer`, `C# Developer`, `ASP.NET Core Developer`, `Full Stack Developer`, `Software Engineer`, `API Engineer`, `AI Application Engineer`, `Python Developer` |
| Location | `Ho Chi Minh City, Vietnam` (ưu tiên 1) |
| Work arrangement | `On-site`, `Hybrid`, `Remote` — nhận cả ba |
| Job type | `Full-time` |
| Start date | ⚠️ **NEEDS_USER_INPUT** (mục G-3) |
| Expected salary | ⚠️ **NEEDS_USER_INPUT** (mục G-4) |
| Relocation | ⚠️ **NEEDS_USER_INPUT** (mục G-5) |

---

## 10. Khối ATS keyword (dán vào field "Skills" dạng text tự do)

```
C#, .NET, .NET Core, ASP.NET Core, ASP.NET MVC, Web API, REST API, RESTful API Design, Microservices, Clean Architecture, SOLID, OOP, Design Patterns, Dependency Injection, Repository Pattern, Dapper, Entity Framework Core, LINQ, SQL Server, PostgreSQL, MySQL, Redis, Stored Procedures, Database Design, Query Optimization, Indexing, Keycloak, JWT, OAuth 2.0, OpenID Connect, RBAC, Angular, Angular 19, AngularJS, TypeScript, JavaScript, RxJS, NgRx, HTML5, CSS3, Tailwind CSS, React, Python, FastAPI, RAG, LLM Integration, Prompt Engineering, Semantic Embeddings, TF-IDF, SQLite, Docker, CI/CD, GitHub Actions, IIS, Git, Git Flow, Swagger, OpenAPI, Unit Testing, Integration Testing, Agile, Scrum
```
