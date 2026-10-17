# Market research: what Vietnamese employers ask for (October 2026)

Prepared 2026-10-17 for the three CV tracks of Truong Van Tinh (Ho Chi Minh City, 3+ years of software development, .NET work since 11/2023).

## Method and limitations (read first)

- **Access.** This environment's network policy blocks the job boards directly (ITviec, TopDev, VietnamWorks, TopCV, LinkedIn, Glints, Indeed, Greenhouse/Lever and similar hosts returned DNS failures). There is no browser.
- **What was used.** Web-search result summaries, which quote parts of postings, and the URLs those searches returned. Full job descriptions were **not** read end to end. Some requirements below may be truncated, and dates are the ones shown in search results.
- **Counts.** The target was ≥15 postings per track.

  | Track | Distinct postings with usable requirement detail | Target met |
  |---|---|---|
  | Backend .NET | 18 | Yes |
  | Full Stack .NET + Angular | 14 | No (one short) |
  | AI Application Engineer | 12 | No |

  Postings with no requirement detail in the snippet are not counted.
- **Freshness.** Several postings are older or expired (marked). They are kept only as evidence of recurring requirements, not as open jobs.
- **Not done here.** Nothing in this file was applied to, and no profile was changed.

## 1. Backend Developer (.NET)

| # | Employer / title | Location | Level / years | Key requirements seen | Date / status | Source |
|---|---|---|---|---|---|---|
| 1 | FPT IS — Backend Developer (.NET) | HCMC | 2–3 yrs | .NET 8, ASP.NET Core Web API, EF Core, SQL Server, Redis, RabbitMQ, microservices, Clean Architecture | deadline 18/10/2026 | jobsgo.vn (search summary) |
| 2 | FPT Telecom International — Software Engineer (.NET) | HCMC | — | C#, ASP.NET Core, EF, REST, microservices, SQL Server/PostgreSQL; Docker, K8s, CI/CD, unit tests a plus | deadline 09/04/2026, expired | search summary |
| 3 | FPT IS — .NET Developer | HCMC D7 | — | .NET Framework/Core, WinForms, SQL Server | UNKNOWN | search summary |
| 4 | Saigon Technology — .NET Developer (Junior/Middle) | HCMC | 2+ yrs | C#, ASP.NET Core (.NET 6/7+), Web API, SQL Server, EF Core, React or Angular | 2026 | search summary |
| 5 | Saigon Technology — .NET (Middle/Senior) | HCMC | 4+ yrs | microservices, Azure, CI/CD, DDD | 2026 | search summary |
| 6 | KMS Technology — .NET Software Engineer | HCMC | 1+ yrs | C#, ASP.NET, .NET Core, OOP, unit testing, Agile/Scrum, upper-intermediate English | 2024 postings | search summary |
| 7 | KMS Technology — Senior .NET | HCMC | senior | same core plus design, mentoring | 2024–2025 | search summary |
| 8 | Bibo Mart — .NET Backend (Middle) | Hanoi | middle | REST/gRPC, SQL/NoSQL optimisation, unit and integration tests, code review, CI/CD | ~Sep 2026 | search summary |
| 9 | HDWEBSOFT — .NET Developer | HCMC | — | .NET Core, Azure, MVC | May 2026 | search summary |
| 10 | Creative Force — Backend (.NET), remote | remote | — | C#, .NET Core, SQL Server, REST, AWS, CI/CD, English | 2026 | search summary |
| 11 | MiTek Vietnam — .NET (Middle/Senior) | HCMC | middle+ | C#, .NET, SQL, WinForms, English | 2026 | search summary |
| 12 | VIHAT — .NET Developer | HCMC | — | .NET Core, microservices, ReactJS | 2026 | search summary |
| 13 | Persol — .NET Developer (hybrid) | HCMC | — | .NET, hybrid | 2026 | search summary |
| 14 | Quang Trung Software — Middle .NET Core 8 | HCMC | 4+ yrs | .NET 8, REST, microservices, DI, CI/CD | 2026 | search summary |
| 15 | TMA Solutions — .NET Developer | HCMC | — | C#, .NET, SQL Server | 2026 | search summary |
| 16 | CMC Global — .NET Developer (Middle/Senior/Lead) | — | middle+ | reusable, reliable .NET code (requirement list not shown) | Oct 2026 | [cmcglobal.com.vn](https://cmcglobal.com.vn/career/net-developer/) |
| 17 | Ekino — .NET | HCMC | — | .NET, REST | 2023, expired | search summary |
| 18 | KMS Technology — Fresher .NET | HCMC | fresher | C#, OOP, SQL | 2024 | search summary |

**Recurring requirements, in order of frequency (Backend):**
- **Core stack:** C# / .NET (Core, 6–8) / ASP.NET Core Web API, in ~18/18 postings.
- **SQL Server:** ~13/18. PostgreSQL appears in a few.
- **EF Core:** ~8/18. Dapper is rarer, but the candidate has real Dapper use.
- **Microservices, message queues, DI:** RabbitMQ, Kafka and DI appear in ~8/18. Clean Architecture or DDD appear in ~4/18.
- **Unit and integration testing:** ~7/18.
- **CI/CD, Docker, cloud:** CI/CD or Docker in ~7/18; Azure or AWS in ~6/18, usually listed as a plus.
- **English:** ~5/18 ask for English, mostly "able to read and write technical documents"; the multinationals ask for communication.
- **Experience:** typical asks are 2+ years (junior or middle) and 4+ years (middle or senior).

**Implications for the Backend CV:**
- Lead with ASP.NET Core / Web API / SQL Server / Dapper / stored procedures.
- Show tests concretely: the BFF has 42 xUnit tests, including a concurrency test.
- Show messaging and resilience (RabbitMQ, Polly, idempotency), because "microservices / message queue" is a frequent filter.
- Keep EF Core in the skills list; the candidate claims it in the original CVs. There is no project evidence of EF Core, so do not headline it.
- Do not claim production microservices or cloud deployment.

## 2. Full Stack Developer (.NET + Angular)

| # | Employer / title | Location | Level / years | Key requirements seen | Date / status | Source |
|---|---|---|---|---|---|---|
| 1 | The Access Group — Middle Fullstack Engineer (.NET and Angular) | HCMC, hybrid | 3+ yrs | full stack (UI, API, middleware, DB, integrations); 3+ yrs SQL Server incl. stored procedures, DB design, query tuning; Agile/Lean; Atlassian | 2026 | [itviec](https://itviec.com/viec-lam-it/middle-fullstack-engineer-net-and-angular-the-access-group-3211), [careers.ta.com](https://careers.ta.com/companies/the-access-group/jobs/60674426-fullstack-engineer-net-and-angular) |
| 2 | Savills Vietnam — Fullstack Developer .NET/Angular (all levels) | HCMC | 4–9 yrs | ASP.NET Core, .NET 5/6, MVC, REST; Angular, TypeScript, JS, HTML5, CSS3, Blazor; Azure DevOps CI/CD | 2026 | [itviec](https://itviec.com/viec-lam-it/fullstack-developer-net-angular-all-levels-savills-vietnam-2530) |
| 3 | Savills Vietnam — Senior Fullstack (.NET & Angular) | HCMC | 8+ yrs | .NET Core, MS SQL, Angular, Blazor, Azure, mentoring | 2026 | [freehire](https://freehire.me/jobs/fullstack-engineer-middle-senior-savills-vietnam-hqptozlk) |
| 4 | Orient Software — Fullstack .NET Engineer | HCMC | middle | .NET, front end, degree in CS, problem solving | 2026 | [semesteria](https://app.semesteria.com/jobs/fullstack-net-engineer-ho-chi-minh-city-orient-software-development-corp-b7e04379-819f-4779-8d26-9553776e754d) |
| 5 | Orient Software — Senior Software Engineer (.NET, Angular/React) | HCMC | 3+ yrs | C#, TypeScript, React, Angular, GraphQL, Azure or AWS | 2026 | [nodeflair](https://nodeflair.com/jobs/orient-software-senior-software-engineer-net-angular-reactjs-497154), [itviec](https://itviec.com/viec-lam-it/senior-fullstack-net-engineer-orient-software-development-corp-5433) |
| 6 | CMC Global — Full-stack .NET + Angular Developer | HCMC | 3+ yrs | C#, ASP.NET Core, Angular, relational DB tuning | 30/11/2026 | [cmcglobal.com.vn](https://cmcglobal.com.vn/career/full-stack-net-angular-developer/) |
| 7 | Blogic Systems — Senior/Lead Fullstack (.NET + Angular) | HCMC | senior | TypeScript, C#, SQL Server, PostgreSQL, Angular, RxJS, Kafka, RabbitMQ | Oct 2026, valid to mid-Nov | [freehire](https://freehire.me/jobs/senior-leader-fullstack-engineer-net-angular-blogic-systems-25m57q27) |
| 8 | Ambitionplus Custom Solutions — Fullstack .NET Core / Angular 12+ / SQL Server | HCMC D12, on-site | 2+ yrs | Angular 12+, .NET 8, SQL Server | recent | [itviec](https://itviec.com/it-jobs/fullstack-developer-net-core-angular-12-sql-server-ambitionplus-custom-solutions-5055) |
| 9 | Netpower Vietnam — Fullstack .NET/Angular | HCMC | 2+ yrs | .NET Core APIs, REST design, Angular, SQL Server, EF Core | deadline 03/04/2025, expired | search summary |
| 10 | Topicus Vietnam — Fullstack .NET/Angular (healthcare) | HCMC Phú Nhuận | intermediate/senior | Angular, .NET Core, AWS | 2026 | [itviec](https://itviec.com/viec-lam-it/fullstack-net-angular-topicus-vietnam-3028) |
| 11 | Coder Trove — Lead Full Stack (.NET, Angular/React/Vue) | HCMC D3, hybrid | senior | .NET, a modern SPA framework | 2026 | [itviec](https://itviec.com/it-jobs/lead-full-stack-developer-net-angular-react-vue-coder-trove-3151) |
| 12 | Restaff (House of Norway) — Fullstack .NET (Angular/React, SQL) | HCMC | — | .NET, Angular or React, SQL | 2026 | [itviec](https://itviec.com/it-jobs/fullstack-net-developer-angular-react-sql-restaff-house-of-norway-5859) |
| 13 | Unattributed — Software Engineer (.NET + Angular) | — | 3+ yrs BE, 2+ yrs Angular 15+ | JWT authentication, Azure a plus | 2026 | [nodeflair](https://nodeflair.com/jobs/cmc-global-software-engineer-net-angular-502043) |
| 14 | 3W Logistics / CodeHQ — Fullstack .NET + Angular (earlier session) | HCMC | middle | .NET, Angular, SQL Server, Agile | 2026 | search summary |

**International benchmark (not counted).** Encora's .NET + Angular + AWS role (6–9 years) asks for Angular 18+, RxJS, NgRx, ASP.NET Core Web API and xUnit: [greenhouse](https://job-boards.greenhouse.io/encora10/jobs/5143231007).

**Recurring requirements (Full Stack):**
- **Core stack:** C# / ASP.NET Core + Angular + TypeScript in 14/14.
- **SQL Server:** ~10/14, often with stored procedures, design and tuning.
- **REST API design:** ~9/14.
- **RxJS:** ~4/14, named explicitly. NgRx appears mainly at senior level or abroad.
- **Cloud and CI/CD:** Azure, AWS or Azure DevOps CI/CD in ~6/14.
- **Messaging:** Kafka or RabbitMQ in ~2/14.
- **Experience:** most postings ask for 3+ years. The junior and middle listings found ask for 2+ years.

**Implications for the Full Stack CV:**
- Put "Angular + ASP.NET Core + SQL Server (stored procedures)" in the headline and in the first bullet.
- Show modern Angular concretely: Angular 19 standalone components, @ngrx/signals SignalStore, RxJS and Native Federation in Ecommerce-Admin.
- Show the production AngularJS work as well; legacy-to-modern Angular is a common reality in these teams.
- Show JWT/OIDC with Keycloak, which matches the JWT authentication item in posting #13.

## 3. AI Application Engineer (Python / FastAPI / RAG / LLM)

| # | Employer / title | Location | Level / years | Key requirements seen | Date / status | Source |
|---|---|---|---|---|---|---|
| 1 | EPAM — AI Engineer (LLM) | HCMC | 0–1 to 2–4 yrs | FastAPI and Python APIs for LLM apps; Azure OpenAI/OpenAI integration with streaming, retries, cost controls; RAG chunking, metadata, citations, relevance tuning | 2026 | [careers.epam.com](https://careers.epam.com/en/vacancy/ai-engineer-llm-blt4i4hdf4z0f1vvp3w_en), [monster](https://www.monster.co.th/job/ai-engineer-epam-ho-chi-minh-62968496) |
| 2 | EPAM (via Joboko, earlier session) — AI Engineer | HCMC | 3 yrs | groundedness/faithfulness, retrieval metrics, production deployment, English | 2026 | search summary |
| 3 | MiTek Vietnam — Senior AI Engineer (LLM, RAG, Azure, MLOps) | HCMC | senior | LLM, RAG, agentic AI, Azure, MLOps | 2026 | [itviec](https://itviec.com/it-jobs/senior-ai-engineer-agentic-ai-mlops-mitek-vietnam-5058) |
| 4 | CloudTeam — AI Engineer | HCMC | — | Python, LLM, RAG, LangChain, AI agents | 2026 | search summary |
| 5 | Innotech — AI Engineer Intern | HCMC | intern | RAG, embeddings, vector search, document parsing, preprocessing, Python | 2026 | search summary |
| 6 | Namitech — Junior AI Engineer | HCMC | junior | LLM chatbots and voicebots, vector databases | 2026 | search summary |
| 7 | TopCV-listed — AI Engineer (LLM, RAG) | — | 3 yrs | LLM, RAG, Python | 2026 | search summary |
| 8 | Multi-agent AI platform — Junior AI Engineer | HCMC | junior | Python for data processing and API calls, FastAPI | 2026 | Indeed VN (search summary) |
| 9 | HCMC AI Engineer (unnamed) | HCMC | — | vector databases, semantic search, PostgreSQL | 2026 | Indeed / Monster VN (search summary) |
| 10 | FPT Securities — Junior AI/ML | Hanoi | 1–3 yrs | prompt engineering, RAG pipelines | mid-2026 | [glassdoor](https://www.glassdoor.com/Job/vietnam-machine-learning-jobs-SRCH_IL.0,7_IN251_KO8,24.htm) |
| 11 | ITviec — Fresher/Junior AI Agent Engineer | Vietnam | fresher/junior | Python, LLM, FastAPI, prompt engineering | 2026 | [itviec llm](https://itviec.com/it-jobs/llm?click_source=Skill+tag&lab_jr_frequency=jr-3xweek&lab_vjr_frequency=vjr-1xweek) |
| 12 | Indeed VN — Junior AI Engineer (graduates) | HCMC | fresher | GenAI and LLM knowledge, ≥1 AI project (chatbot or automation), RAG, agents, prompt engineering | Oct 2026 | [indeed](https://jobs.vn.indeed.com/q-junior-ai-engineer-jobs.html) |

**Recurring requirements (AI):**
- **Python and LLM integration:** 12/12.
- **RAG:** ~10/12, with chunking, embeddings, vector search and citations.
- **FastAPI:** ~5/12, named explicitly.
- **Vector databases, semantic search:** ~5/12.
- **Agents:** ~5/12 mention AI agents or multi-agent systems.
- **Prompt engineering:** ~4/12.
- **Evaluation:** ~3/12 name groundedness, faithfulness or retrieval metrics. The 2026 hiring guides describe this as the differentiator for junior AI engineers ("an end-to-end project with basic evals").
- **LangChain:** named in 1–2 postings; usually a plus.
- **Cloud LLM, MLOps, production:** Azure OpenAI, MLOps and production deployment appear at middle and senior levels.

**Implications for the AI CV:**
- Headline the Retail RAG Assistant: it has parsing, a vector DB, LangChain, citations, abstention, an evaluation harness and green CI. That is the junior "end-to-end project with evals" the guides describe.
- Put the production AI work at Con Cung (vector semantic search, n8n pipelines, Claude + MCP loop) first in experience.
- Do not claim production RAG, fine-tuning, MLOps or Azure OpenAI deployment.

## 4. Cross-track findings

1. **Experience bar.** Most HCMC middle postings ask for 2–4 years. "3+ years of software development" is accurate and should be stated once, plainly. Do not inflate it to "3+ years of .NET".
2. **English.** It is usually a reading and writing requirement for local companies and a speaking requirement for multinationals. The candidate's English line (good reading and writing, basic spoken) is truthful and enough for most local postings. It will filter out some multinational roles, and the CV should not hide this.
3. **ATS.** ITviec, TopCV and LinkedIn parse uploaded PDFs; recruiters at outsourcing companies (FPT, KMS, Saigon Technology, CMC) skim for stack keywords and years. Single-column text with standard headings is safest. Exact keyword forms seen in postings include:
   - ASP.NET Core
   - Web API
   - RESTful API
   - SQL Server
   - Entity Framework Core
   - Unit Test
   - CI/CD
   - Docker
   - Microservices
   - RabbitMQ
   - Angular
   - TypeScript
   - RxJS
   - RAG
   - LLM
   - FastAPI
   - Vector Database
   - Prompt Engineering
4. **Photos.** Vietnamese recruiters commonly expect a photo on locally formatted CVs. International companies and ATS-heavy pipelines do not need one. The plan is to keep the photo in the designed version and leave it out of the ATS-first version.
5. **Salary context.** Reference only, not used in the CVs: junior .NET roles are around ₫20M–35M per month (secondtalent); JobsGO's average is about ₫17.1M; Glints shows junior AI roles at ₫18–40M. Salary expectations remain `NEEDS_USER_INPUT` for applications.
