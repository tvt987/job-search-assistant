# PHASE 1 — BÁO CÁO XÁC MINH & DANH SÁCH THIẾU DỮ LIỆU

Ngày chạy: **2026-10-14**
Đối chiếu: 3 CV trong `resumes/` ⟷ `APPLICANT_CONTEXT.md` ⟷ `application-templates/screening_qa.md`

---

## PHẦN 1 — Kết quả đối chiếu CV

### ✅ Đã khớp hoàn toàn (không cần xử lý)

| Hạng mục | Trạng thái |
| :--- | :--- |
| Tên, email, location, GitHub | Khớp cả 3 CV + context |
| Điện thoại | Khớp — CV ghi `0931467024`, context ghi `+84 931 467 024`, **cùng một số**, chỉ khác định dạng |
| Con Cung: chức danh `Full Stack Developer`, từ `11/2023` | Khớp cả 3 CV + context |
| FPT: `Frontend Intern`, `09/2023`–`11/2023` | Khớp cả 3 CV + context |
| Học vấn: UIT, VNU-HCM, Information Technology, 2026 | Khớp cả 3 CV + context |
| English: `Conversational` | Khớp cả 3 CV + context |
| Tổng kinh nghiệm `3+ năm` | Khớp — 09/2023 → 14/10/2026 = **3 năm 1 tháng** ✓ |
| 7 phép tính quyền lợi gói 3/6/12 tháng | Khớp |
| Keycloak / JWT / OAuth 2.0 / OIDC / RBAC | Khớp |
| Công cụ preview/copy cho 4 loại code template | Khớp |
| Layout-Store: 10 routes ASP.NET Core/PostgreSQL | Khớp CV_Backend + context |
| Retail RAG: 8 synthetic queries, CI pass | Khớp — CV chi tiết hơn (6 top-3 đúng + 2 abstention đúng), context nén lại. Không xung đột. |
| Support Ticket: 5 nhóm, 10 HTTP tests, 120 schema combos, 1.000 SQLite decisions | Khớp |
| Retail Reliability Lab: Redis TTL 60s, 22 tests, 3.63ms → 0.005ms, 100.000 rows | Khớp |

### ⚠️ Điểm lệch đã phát hiện — KHÔNG tự giải quyết, cần bạn xác nhận

#### D-1. Ba file PDF bị trùng ở thư mục gốc
Ba file ở `/` có **MD5 giống y hệt** ba file trong `resumes/`:
```
05e7ab0c...  CV_Backend_TruongVanTinh.pdf   ==  resumes/CV_Backend_TruongVanTinh.pdf
46c75257...  CV_FullStack_TruongVanTinh.pdf ==  resumes/CV_FullStack_TruongVanTinh.pdf
87c0300e...  CV_AI_TruongVanTinh.pdf        ==  resumes/CV_AI_TruongVanTinh.pdf
```
`README.md` chỉ mô tả cấu trúc có `resumes/`. **Rủi ro:** sau này sửa 1 bản mà upload bản còn lại
→ nộp CV cũ mà không biết.
**Đề xuất:** xoá 3 bản ở gốc, chỉ giữ `resumes/`. ⚠️ Chưa xoá — chờ bạn đồng ý.

#### D-2. Dự án Ecommerce-Admin được mô tả khác nhau giữa 2 CV
| Nguồn | Mô tả |
| :--- | :--- |
| `APPLICANT_CONTEXT.md` §4.B.2 | "Frontend development" — Angular 19, TypeScript, RxJS, NgRx SignalStore |
| `CV_FullStack` | "Frontend development" — Angular 19, TypeScript, RxJS, NgRx SignalStore ✓ |
| `CV_Backend` | "**Frontend/API integration**" — **C#, Angular, PostgreSQL**, REST APIs |

→ CV_Backend gán thêm **C# và PostgreSQL** cho dự án này, context và CV_FullStack thì không.
**Cần bạn xác nhận:** bạn có thật sự làm phần C#/PostgreSQL trong Ecommerce-Admin không?
- Nếu **có** → nên bổ sung vào `APPLICANT_CONTEXT.md` cho nhất quán.
- Nếu **không** → nên sửa `CV_Backend` để tránh bị hỏi sâu rồi không trả lời được.

Hiện tại các file profile dùng **bản mô tả của context/CV_FullStack** (chỉ frontend) — bản an toàn hơn.

#### D-3. Dự án Layout-Store cũng mô tả khác nhau
| Nguồn | Mô tả đóng góp |
| :--- | :--- |
| `APPLICANT_CONTEXT.md` + `CV_Backend` | 10 routes ASP.NET Core/PostgreSQL (search, CRUD, approval, Excel import) + nối HTTP handler → stored procedure qua async interface & DI |
| `CV_FullStack` | "Contributed **Angular workflows** and PostgreSQL data structures for store layouts and product placement" |

→ Hai CV kể hai phần việc khác nhau trong cùng dự án (backend routes vs Angular workflows).
Có thể bạn làm cả hai, nhưng context chỉ ghi phần backend.
**Cần bạn xác nhận** phần Angular trong Layout-Store có thật không. Profile hiện dùng **bản backend**
(có trong context).

#### D-4. Skill có trong CV nhưng không có trong APPLICANT_CONTEXT
CV liệt kê, context §3 **không** liệt kê:
`Node.js` · `Java Spring Boot` · `Message Queues` · `Vector Databases`

CV gắn nhãn `Node.js`/`Java Spring Boot` là **"Additional stacks"**, còn `Message Queues` và
`Vector Databases` nằm lẫn trong danh sách chính.

**Quyết định đã áp dụng:** giữ trong CV PDF, **không đưa vào skill tag của profile**.
Lý do: không có dòng kinh nghiệm hay dự án nào trong CV chống lưng cho 4 skill này, nên khi NTD
hỏi "mấy năm Node.js / có dùng Kafka/RabbitMQ gì chưa?" thì không có dữ liệu để trả lời trung thực,
và skill tag lệch sẽ kéo về JD sai stack.
**Cần bạn xác nhận** có muốn giữ quyết định này hay không.

#### D-5. `screening_qa.md` khai số năm thấp hơn thực tế
`screening_qa.md` chốt `.NET / C#: 2+ years`. Thực tế Con Cung `11/2023 → 14/10/2026` =
**2 năm 11 tháng**, tức gần 3 năm.

→ "2+" vẫn **đúng sự thật** (chỉ là bảo thủ), nên tôi **giữ nguyên "2+"** trong mọi profile để
đồng nhất với template đã chốt. Nhưng bạn nên biết là có thể nâng lên `~3 years` một cách trung thực
nếu muốn khớp JD yêu cầu "3+ years .NET".
**Cần bạn chọn:** giữ `2+` hay đổi sang `3` (và tôi sẽ sửa cả `screening_qa.md`).

#### D-6. `Azure` / `AWS` được chống lưng rất mỏng
Nguồn duy nhất là Retail Reliability Lab, và CV ghi rõ: *"Authored **undeployed** templates for
Docker Compose and Azure"*. Context §4.B.5 cũng chỉ ghi "thử nghiệm".

→ Đã xử lý: `Azure`/`AWS` đặt ở nhóm skill thấp, **không đưa vào headline**, CareerViet khai mức `Cơ bản`.
Không bỏ hẳn (vì có trong CV) nhưng không quảng bá.

---

## 🔴 D-7 — PHÁT HIỆN NGHIÊM TRỌNG: 2 repo "portfolio" chứa source code Con Cung

Bạn bảo tôi *"xem git thử"* để giải quyết D-2/D-3. Tôi đã clone và đọc cả hai repo.
Hai câu hỏi ban đầu đã trả lời được — nhưng tôi tìm ra một vấn đề lớn hơn nhiều.

### Bằng chứng

| Kiểm tra | `tvt987/Layout-Store` | `tvt987/Ecommerce-Admin` |
| :--- | :--- | :--- |
| Trạng thái repo | **Public** | **Public** |
| Số commit | **1** — `d3fce2d "push all"`, 2026-04-19 | **1** — `"push all"`, 2026-04-19 |
| Tác giả | Chỉ `Trương Văn Tình <tinhkun102@gmail.com>` | Chỉ `Trương Văn Tình <tinhkun102@gmail.com>` |
| Namespace / branding | `CCI.API.Layout`, `CCI.Business.Layout`, `CCI.DTO.Layout`, `CCI.Database`, `CCI.Release` — **689** chỗ xuất hiện `CCI` | **15** file chứa `CCI`, font `ConCung-Font.ttf`, `conCungFontFace` |
| Hạ tầng nội bộ Con Cung | `https://nexus.ingress.concung.io` (Nexus registry nội bộ), NuGet feed `concung.com` | `cdn1.concung.com`, `123test.concung.com` (môi trường test nội bộ) — **36** file chứa `concung` |
| Hệ thống nghiệp vụ | Connection string `ConnectionStringMDM`, `ConnectionStringSCM` (Master Data / Supply Chain) | — |
| Quy mô | 29 controller, **182** endpoint HTTP, 368 file `.cs`, 363 file `.ts` | 589 file `.ts` |

### ✅ Tin tốt: không có credential nào bị lộ
Tôi đã quét riêng phần này. **Không có** `appsettings.json` thật được commit, không có password,
không có API key, không có token. Các chỗ `ClientSecret` / `ConnectionString` chỉ là **tên khoá cấu hình**
trong code (`AppCoreConfig.Common.Oauth2ForWeb.OauthClientSecret`), giá trị được nạp từ ngoài.
`nuget.config` chỉ có URL package source, không có thông tin đăng nhập.

### Vì sao đây là vấn đề

1. **Rủi ro với hợp đồng lao động.** Đây là source code sản phẩm nội bộ của Con Cung — nơi bạn
   **đang làm việc** — đang nằm công khai trên GitHub cá nhân, kèm cả tên hạ tầng nội bộ.
   Hầu hết hợp đồng lao động và thoả thuận bảo mật đều cấm việc này. Rủi ro thuộc về bạn, không
   phải về tôi hay về repo này.

2. **Nó đi ngược mục tiêu tìm việc của bạn.** Bạn vừa yêu cầu bật `#OpenToWork` công khai và
   đưa link repo lên 6 nền tảng. Nếu làm đúng như vậy, mỗi recruiter mở link sẽ thấy ngay code
   của công ty hiện tại bạn trong repo cá nhân. Với nhiều nhà tuyển dụng — đặc biệt là công ty
   lớn và công ty nước ngoài — đây là **tín hiệu đỏ về ý thức bảo mật**, nó trừ điểm chứ không
   cộng điểm. Và hồ sơ công khai cũng có nghĩa Con Cung có thể thấy.

3. **Nhãn "Contributor" / "Personal project" không khớp.** Cả hai repo chỉ có **1 commit duy nhất
   của riêng bạn**, dạng "push all" — tức là đẩy nguyên codebase lên, không phải chuỗi đóng góp
   vào dự án của người khác. Repo cũng không tách được phần nào là của bạn: CV ghi *"10 routes"*
   nhưng repo có **182 endpoint**, recruiter mở ra không biết 10 cái nào là của bạn.

### 🔴 Vì vậy tôi đã làm gì

**Tôi đã bỏ link 2 repo này ra khỏi mọi file profile**, và **không** đưa chúng lên bất kỳ nền tảng nào
cho tới khi bạn quyết. Tôi không tự xoá/đổi gì trên GitHub của bạn — đó là quyết định của bạn.

### Bạn cần chọn

| Phương án | Nội dung | Đánh giá |
| :--- | :--- | :--- |
| **A. Chuyển 2 repo sang Private** *(khuyến nghị)* | GitHub → Settings → Danger Zone → Change visibility → Private. Vẫn giữ được code cho bản thân. | Xử lý gốc rễ. Mất phần "khoe code" nhưng 3 project AI bên dưới vẫn đủ để khoe. |
| **B. Xoá repo** | Nếu bạn có bản local rồi | Dứt điểm nhất |
| **C. Viết lại thành bản sạch** | Tạo repo mới **chỉ chứa code bạn tự viết**, bỏ hết namespace `CCI.*`, branding và host nội bộ | Tốt nhất cho portfolio, nhưng tốn thời gian và vẫn phải cẩn thận về quyền sở hữu code |
| **D. Giữ public** | Chấp nhận rủi ro | Tôi sẽ vẫn **không** đưa link lên profile và sẽ nói rõ lý do mỗi lần bạn hỏi |

### Portfolio thay thế — vẫn đủ mạnh

Ba project này **là của bạn thật**, tự viết, không liên quan Con Cung — và đã đủ để chứng minh năng lực:
- `retail-rag-assistant` — RAG có dẫn nguồn, abstention, extractive fallback, CI pass
- `support-ticket-ai-triage` — 10 HTTP test, 120 schema combination, 1.000 SQLite decision
- Retail Reliability Lab — 22 test trên Redis thật, 3.63ms → 0.005ms

→ Tôi đã **đổi thứ tự project** trên mọi profile để 3 cái này lên trước.

### Hai câu hỏi ban đầu — đã trả lời

**D-2 (Ecommerce-Admin có C#/PostgreSQL không?) → KHÔNG.**
Repo có **0 file `.cs`**, **0 file `.sql`**, **0 tham chiếu PostgreSQL**, chỉ có duy nhất thư mục `frontend/`.
→ `CV_Backend` khai *"C#, Angular, PostgreSQL, REST APIs"* và *"PostgreSQL data contracts"* cho project này
là **khai quá so với thực tế**. `APPLICANT_CONTEXT.md` và `CV_FullStack` (chỉ frontend) mới là bản đúng.
🔧 **Cần sửa `CV_Backend_TruongVanTinh.pdf`** — bỏ C#/PostgreSQL khỏi mục Ecommerce-Admin.
Xác nhận được: Angular `19.2.14` ✓, `@ngrx/signals 19.2.1` ✓, `signalStore` dùng trong **29** file ✓, RxJS `7.8.1` ✓
→ claim Angular 19 / NgRx SignalStore của `CV_FullStack` là **chính xác**.

**D-3 (Layout-Store: backend routes hay Angular workflows?) → CẢ HAI đều có thật.**
Repo có `BE/` (ASP.NET Core, **Npgsql trong 25 file**, **Dapper trong 33 file**, 21 file `.sql`)
và `FE/` (Angular `21.1.5`, 29 component, 92 service).
→ Cả hai CV đều mô tả đúng, chỉ là mỗi CV kể một phần khác nhau. **Không phải lỗi.**
Claim *"ASP.NET Core / PostgreSQL routes + Dapper + stored procedures"* được code xác nhận.

---

## PHẦN 2 — `NEEDS_USER_INPUT`: những field tôi sẽ không tự điền

Theo `CLAUDE.md` Phase 4 và `APPLICANT_CONTEXT.md` §7.2.
**Bạn trả lời xong mục nào, tôi điền được mục đó ngay.**

| ID | Field | Vì sao không tự điền | Nền tảng bị chặn |
| :-- | :--- | :--- | :--- |
| ~~**G-1**~~ | ~~Tháng tốt nghiệp~~ | ✅ **ĐÃ TRẢ LỜI: `06/2026`.** Năm bắt đầu `2022` là **suy luận** từ chương trình 4 năm — xác nhận lại nếu khác. | — |
| **G-2** | **Số năm kinh nghiệm Python/FastAPI** | Chỉ có project cá nhân, nguồn không ghi mốc bắt đầu | ITviec (field số năm theo skill) |
| ~~**G-3**~~ | ~~Ngày bắt đầu / notice period~~ | ✅ **ĐÃ TRẢ LỜI: 1 tháng sau khi nhận offer.** | — |
| ~~**G-4**~~ | ~~Mức lương mong muốn~~ | ✅ **ĐÃ TRẢ LỜI: 28.000.000 – 32.000.000 VND/tháng, thương lượng.** | — |
| **G-5** | **Sẵn sàng relocate** | `CLAUDE.md` cấm đoán | VietnamWorks, Glints |
| ~~**G-6**~~ | ~~FPT là pháp nhân nào?~~ | ✅ **ĐÃ TRẢ LỜI: `FPT Software`.** Đã áp vào cả 6 file. ⚠️ CV PDF vẫn chỉ ghi `FPT` — nên cập nhật 3 CV cho khớp. | — |
| **G-7** | **Layout-Store & Ecommerce-Admin là việc công ty hay cá nhân?** | 🔴 **ĐÃ ĐIỀU TRA — xem D-7 bên dưới.** Code trong 2 repo này là của Con Cung. Cần bạn quyết gấp. | **Cả 6 — đang chặn** |
| ~~**G-8**~~ | ~~Có bật chế độ công khai tìm việc không?~~ | ✅ **ĐÃ QUYẾT 2026-10-14: công khai hoàn toàn.** Bật `#OpenToWork` trên LinkedIn + mở hồ sơ cho mọi NTD trên cả 6 sàn. Bạn đã xác nhận chấp nhận việc Con Cung có thể thấy. | — |
| **G-9** | **Ngày sinh** | Không có trong bất kỳ nguồn nào; thuộc nhóm thông tin nhạy cảm | ITviec, TopDev, VietnamWorks, CareerViet, Glints |
| **G-10** | **Work authorization** | Suy luận "công dân VN, không cần sponsor" là hợp lý nhưng là **khai báo pháp lý** → `CLAUDE.md` yêu cầu bạn xác nhận | VietnamWorks |
| **G-11** | **Ảnh profile + ảnh banner** | Không có file ảnh trong repo | LinkedIn (bắt buộc cho All-Star), Glints |
| **G-12** | **LinkedIn custom URL** | Cần bạn chọn slug và kiểm tra còn trống | LinkedIn → rồi điền chéo sang 5 sàn kia |

### Câu hỏi tối thiểu để mở khoá phần lớn công việc

Chỉ cần 4 câu này là tôi điền được ~90% các field:

1. **Tháng tốt nghiệp** (G-1) — ví dụ `06/2026`? Và năm bắt đầu học?
2. **Mức lương mong muốn** (G-4) — một khoảng VND/tháng, hoặc "chọn Thương lượng", hoặc "để trống".
3. **Ngày có thể bắt đầu** (G-3) — ví dụ "sau 30 ngày báo trước" / "ngay".
4. **FPT là công ty con nào** (G-6)?

Và một câu quyết định chính sách: **G-8** — có bật chế độ công khai đang tìm việc không?

---

## PHẦN 3 — Trạng thái đăng nhập các nền tảng

`CLAUDE.md` Phase 1 yêu cầu kiểm tra session đăng nhập và xác minh nó thuộc về `tinhkun102@gmail.com`
trước khi dùng.

**Kết quả kiểm tra: không thực hiện được trong session này.**

| Nền tảng | Phương thức đăng nhập | Email/tài khoản | Trạng thái |
| :--- | :--- | :--- | :--- |
| LinkedIn | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |
| ITviec | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |
| TopDev | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |
| VietnamWorks | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |
| CareerViet | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |
| Glints | Chưa xác minh | Chưa xác minh | **Chưa kiểm tra được** |

**Lý do:** session này chạy trong một container cloud **không có công cụ browser nào**. Tôi đã kiểm tra
toàn bộ toolset: không có Claude Browser, không có Chrome extension, không có computer-use, không có
remote-device nào được liên kết. Container có Chromium + Playwright, nhưng đó là browser **trắng trong
container** — không có session đăng nhập nào của bạn, và `CLAUDE.md` Phase 5 quy định
*"Use only the browser session and automation tools explicitly available in this environment"*,
đồng thời cấm tôi xử lý mật khẩu/cookie/OTP.

→ Vì vậy tôi **không** đăng nhập, **không** tạo account mới, và **không** báo cáo profile nào là đã cập nhật.
Phù hợp với `context.md` §9 (chưa xác minh được mapping Google account ↔ nền tảng nào) và nguyên tắc
"không tạo account thứ hai nếu có thể đã tồn tại account".

### Cách để thực sự cập nhật được profile

**Phương án A — bạn tự dán (dùng được ngay, không cần gì thêm).**
Mở từng file `platform-profiles/<nền-tảng>.md`, dán theo bảng mapping. Nội dung đã viết sẵn đúng
giới hạn ký tự của từng field.

**Phương án B — cho tôi quyền browser trên máy bạn.**
Chạy session Claude Code từ **desktop app** (hoặc liên kết session cloud này với máy bạn qua
Remote Control), rồi bật **Claude in Chrome** hoặc **built-in browser**. Khi đó tôi dùng được
session đăng nhập sẵn của bạn, và sẽ:
1. Kiểm tra từng trang xem account đang đăng nhập có đúng `tinhkun102@gmail.com`;
2. Tự điền các field đã xác minh;
3. **Dừng lại và hỏi bạn** ở đúng các field G-1…G-12 và ở mọi bước OTP/MFA/CAPTCHA.

**Phương án C — tôi xuất nội dung ra định dạng khác.** Nếu bạn muốn một bản HTML/doc để copy nhanh
hơn, hoặc muốn gộp hết 6 nền tảng thành 1 trang checklist in được, nói tôi làm.
