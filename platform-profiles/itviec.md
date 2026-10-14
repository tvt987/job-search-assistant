# ITVIEC — Checklist hoàn thiện profile

**Mục tiêu:** đưa hồ sơ lên mức **"Rất tốt"** — ITviec chỉ cho xem & tải CV từ hồ sơ sau khi đạt mức này,
và nhà tuyển dụng ưu tiên hồ sơ hoàn chỉnh.
**Track:** Backend là chính (ITviec rất mạnh về JD .NET), nhưng field "Vị trí mong muốn" nên để FullStack
để nhận cả hai luồng JD.

---

## A. Hai thứ tách biệt trên ITviec — đừng lẫn

ITviec có **2 thực thể khác nhau** trong mục *"Hồ sơ và CV"*:

1. **ITviec Profile** — hồ sơ cấu trúc, điền từng field. Đây là thứ nhà tuyển dụng **tìm kiếm** được.
2. **CV tải lên** — file PDF đính kèm, dùng khi ứng tuyển.

→ Phải làm **cả hai**. Profile để được tìm thấy, CV PDF để nộp đơn.
→ CV tải lên: dùng `resumes/CV_Backend_TruongVanTinh.pdf` làm mặc định cho ITviec.
→ ITviec kiểm duyệt hồ sơ/CV **tối đa 24 giờ** — tính vào lịch trước khi bắt đầu nộp đơn loạt.

---

## B. Mapping từng field

### B.1 Thông tin cá nhân
| Field ITviec | Giá trị |
| :--- | :--- |
| Họ và tên | `Truong Van Tinh` |
| Email | `tinhkun102@gmail.com` |
| Số điện thoại | `0931467024` |
| Địa chỉ / Thành phố | `Ho Chi Minh City` |
| Ngày sinh | ⚠️ **NEEDS_USER_INPUT** — không có trong nguồn (G-9) |
| Giới tính | ⚠️ **NEEDS_USER_INPUT** — thông tin nhân khẩu, không tự điền |
| Link GitHub | `https://github.com/tvt987` |
| Link LinkedIn | ⚠️ điền sau khi chốt custom URL ở `linkedin.md` mục 9 |

### B.2 Vị trí & nguyện vọng
| Field | Giá trị |
| :--- | :--- |
| Vị trí mong muốn / Job title | `Full Stack Developer | .NET & Angular` |
| Cấp bậc hiện tại | `Middle` *(3+ năm — không phải Fresher, chưa đủ cơ sở khai Senior)* |
| Địa điểm làm việc mong muốn | `Ho Chi Minh City` |
| Hình thức | `Full-time` — nhận `On-site` / `Hybrid` / `Remote` |
| Mức lương mong muốn | ⚠️ **NEEDS_USER_INPUT** (G-4). ITviec cho **ẩn** field này với NTD — nếu bạn chưa muốn chốt số, bật chế độ ẩn thay vì điền số bừa. |
| Sẵn sàng đi làm từ | ⚠️ **NEEDS_USER_INPUT** (G-3) |

### B.3 Giới thiệu bản thân / About me
→ Dán khối mục **3.2** (EN, 748 ký tự) của `MASTER_CONTENT.md`.
ITviec là sàn IT dùng tiếng Anh phổ biến với JD quốc tế → **ưu tiên bản EN**.

### B.4 Kinh nghiệm làm việc
Nhập **2 mục**, thứ tự thời gian đảo ngược (ITviec khuyến nghị reverse-chronological):

**Mục 1 —** Con Cung · `Full Stack Developer` · `11/2023` – `Hiện tại`
→ bullets **track Backend** (mục 4.1) vì ITviec mapping JD .NET nhiều hơn.

**Mục 2 —** FPT · `Frontend Intern` · `09/2023` – `11/2023`
→ bullets mục 4.2.

> ⚠️ **Quan trọng — nhãn hồ sơ:** ITviec tự gán nhãn **"Fresher"** dựa trên *kinh nghiệm làm việc chuyên nghiệp
> khai trong hồ sơ*, và nhãn **"Undergraduate"** dựa trên *thời gian học khai trong hồ sơ*.
> Vì học vấn ghi tốt nghiệp **2026** (tức là vừa xong), nếu khai thời gian học kéo đến 2026 mà phần kinh
> nghiệm điền thiếu/sơ sài thì hồ sơ dễ bị gắn nhãn **Undergraduate/Fresher** → bị lọc khỏi JD Middle.
> → **Phải điền đầy đủ cả 2 mục kinh nghiệm trên với ngày tháng chính xác** để nhãn phản ánh đúng 3+ năm.

### B.5 Kỹ năng (ITviec cho gắn số năm cho từng skill)
| Skill | Số năm khai | Cơ sở |
| :--- | :--- | :--- |
| `C#` | `2+` | Con Cung 11/2023→nay |
| `.NET` / `ASP.NET Core` | `2+` | Con Cung |
| `SQL Server` | `2+` | Con Cung |
| `Dapper` | `2+` | Con Cung |
| `AngularJS` | `2+` | Con Cung |
| `Angular` | `2+` | FPT + portfolio Angular 19 |
| `TypeScript` | `2+` | Ecommerce-Admin + Con Cung |
| `PostgreSQL` | `1+` | Layout-Store, Ecommerce-Admin |
| `Keycloak` / `OAuth 2.0` / `JWT` | `2+` | Con Cung |
| `Docker` | `2+` | Con Cung (hỗ trợ triển khai) + projects |
| `Python` / `FastAPI` | ⚠️ **để trống số năm** | Chỉ có project cá nhân, nguồn không ghi mốc bắt đầu (G-2). Vẫn **thêm skill**, chỉ không khai số năm. |
| `Redis` | `1+` | Retail Reliability Lab |
| `Git` | `3+` | Từ 09/2023 |

Skill thêm (không cần số năm): `Web API` · `REST API Design` · `Entity Framework Core` · `LINQ` ·
`Stored Procedures` · `Query Optimization` · `RxJS` · `NgRx` · `React` · `Tailwind CSS` ·
`RBAC` · `OpenID Connect` · `Microservices` · `Clean Architecture` · `SOLID` · `CI/CD` ·
`GitHub Actions` · `IIS` · `Swagger/OpenAPI` · `Unit Testing` · `Integration Testing` ·
`RAG` · `LLM Integration` · `Prompt Engineering` · `SQLite` · `Agile/Scrum`

❌ Không thêm: `Node.js`, `Java`, `Spring Boot` (mục 7 nhóm G).

### B.6 Học vấn
| Field | Giá trị |
| :--- | :--- |
| Trường | `University of Information Technology (UIT), VNU-HCM` |
| Bằng | `Bachelor` |
| Chuyên ngành | `Information Technology` |
| Thời gian | `?/2022` – `?/2026` ⚠️ **NEEDS_USER_INPUT** cả tháng bắt đầu và kết thúc (G-1) |
| GPA | Để trống — không có trong CV |

### B.7 Dự án
Nhập **4 project** (ITviec có mục Dự án riêng), thứ tự track Backend: **P1 → P5 → P4 → P2**.
Nội dung + repo lấy từ mục 6. P5 để trống link.

### B.8 Ngoại ngữ
| Ngôn ngữ | Mức |
| :--- | :--- |
| English | `Intermediate` / `Conversational` — **không chọn Advanced/Fluent** |
| Vietnamese | `Native` |

### B.9 Chứng chỉ
→ **Để trống.** CV không có mục certifications. Không thêm gì.

---

## C. Lưu ý riêng của ITviec

- **Một tài khoản = một ứng viên.** ITviec quy định vậy → không dùng chung/tạo nhiều account.
- **Không tạo account mới nếu có thể đã tồn tại account.** Phải kiểm tra login trước
  (`CLAUDE.md` Phase 1). Nếu quên mật khẩu → dùng luồng khôi phục của ITviec với
  `tinhkun102@gmail.com`, không tạo account thứ hai.
- **Chế độ hiển thị hồ sơ:** bật cho NTD tìm thấy (`Allow employers to find my profile`)
  — nhưng ⚠️ cân nhắc: Con Cung cũng tuyển dụng trên ITviec. Xem G-8.
- CV PDF dành cho ITviec: `resumes/CV_Backend_TruongVanTinh.pdf`.
  Khi ứng tuyển JD Angular/FullStack thì đổi sang `CV_FullStack_...`, JD AI thì `CV_AI_...`.
