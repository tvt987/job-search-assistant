# REVIEW 3 CV — ĐÁNH GIÁ & KẾ HOẠCH CẢI THIỆN

Ngày: **2026-10-14** · Đối chiếu với code thật trong 4 repo (xem `EVIDENCE.md`)

---

## Điểm hiện tại

| CV | Điểm | Nhận xét một dòng |
| :--- | :---: | :--- |
| `CV_Backend_TruongVanTinh.pdf` | **6.5/10** | Nền tảng tốt, nhưng có 2 con số bịa và 1 claim dự án sai |
| `CV_FullStack_TruongVanTinh.pdf` | **7.5/10** | **Mạnh nhất trong ba bản.** Không có claim bịa nào |
| `CV_AI_TruongVanTinh.pdf` | **5.5/10** | Nội dung hay nhất nhưng **chứa cả 4 con số không có cơ sở** |

**Điểm chung đáng khen:** 1 trang A4, ~470 từ — độ dài chuẩn. Cấu trúc rõ. Ba bản tách track đúng
chiến lược. Có số liệu cụ thể (đúng hướng, chỉ sai ở chỗ một số số không thật).

---

## Chẩn đoán cốt lõi

CV đang mắc **hai lỗi ngược chiều nhau cùng lúc**:

> **Thổi phồng** thứ không có (4 con số test không tồn tại trong code)
> **Bán rẻ** thứ có thật (toàn bộ guardrail kỹ thuật thực sự tinh tế, không được nhắc một chữ)

Sửa cả hai cùng lúc thì CV **vừa an toàn hơn vừa mạnh hơn**. Đây không phải đánh đổi.

---

## Danh sách việc — theo mức ưu tiên

### 🔴 R-1. Xoá 4 con số không có cơ sở — BẮT BUỘC

| Bỏ | Thay bằng (có thật) |
| :--- | :--- |
| ~~"Tested **10** FastAPI HTTP scenarios"~~ | "Covered the triage flow with unit, API and end-to-end tests run in CI" |
| ~~"Validated **120** synthetic schema combinations"~~ | "Rejected malformed LLM responses that failed schema validation" |
| ~~"**720** urgent-rule cases"~~ | "Enforced urgent-rule overrides that escalate security tickets even when the model classifies them as normal" |
| ~~"Validated **1,000** synthetic SQLite review decisions"~~ | "Enforced idempotent persistence: ticket ID is the primary key, so a duplicate submission cannot overwrite a recorded decision" |

**Lý do:** CV có link GitHub → interviewer sẽ mở repo. `grep` một phút là thấy 7 test chứ không phải 10,
và 120/720/1000 không tồn tại. Khi đó **cả 15 claim đúng cũng mất giá trị**.
Con số nhỏ verify được > con số lớn sụp khi kiểm tra.

### 🔴 R-2. Sửa claim sai về Ecommerce-Admin trong `CV_Backend`

Hiện ghi: `Ecommerce-Admin | **C#, Angular, PostgreSQL**, REST APIs` và *"PostgreSQL data contracts"*.
**Repo có 0 file `.cs`, 0 file `.sql`, 0 tham chiếu PostgreSQL** — chỉ có `frontend/`.
→ Sửa thành Angular/TypeScript, hoặc **bỏ project này khỏi CV_Backend** (đúng hơn, vì nó không phải bằng
chứng backend).

### 🔴 R-3. Bỏ "undeployed templates"

Hiện có trên **cả 3 CV**: *"Authored **undeployed** templates for Docker Compose and Azure."*
Đây là tự quảng cáo thứ **chưa làm xong**. Không ai cộng điểm cho template chưa deploy.
→ **Xoá câu này.** Đồng thời hạ `Azure`/`AWS` xuống cuối mục skill (nguồn duy nhất là lab này).

### 🟠 R-4. Đưa guardrail kỹ thuật lên — đây là đòn mạnh nhất

Đang thiếu hoàn toàn, mà toàn bộ đều có trong code:
- **Chặn LLM trả lời không dẫn nguồn** → nếu output không chứa `[source_id]`, loại bỏ, dùng bản extractive
- **Phòng prompt injection** → system prompt chỉ thị coi tài liệu là *data, never instructions*
- **Tự viết TF-IDF** (IDF smoothed, sublinear TF, L2-norm) **không dùng sklearn** — core chỉ dùng stdlib
- **CI gác regression** → eval trả exit code khác 0 nếu retrieval tụt, build fail
- **Rule bảo mật override LLM** → ticket security vẫn escalate dù model chấm "normal"
- **Mask PII trước khi gọi provider ngoài**
- **Retrieval thay thế được** → TF-IDF mặc định, semantic bật qua env, cùng một interface

Chi tiết + vị trí dòng code: `EVIDENCE.md`.

### 🟠 R-5. Giải thích "tốt nghiệp 2026 + 3 năm kinh nghiệm"

Hiện CV ghi `Graduated 2026` và `3+ years experience` mà **không giải thích**. Recruiter đọc sẽ thấy
mâu thuẫn hoặc nghi khai khống — một trong những lý do bị loại ở vòng sàng hồ sơ.

Sự thật: bạn **đi làm full-time từ 11/2023 trong khi vẫn đang học, tốt nghiệp 06/2026.** Đó là **điểm mạnh**,
nhưng phải nói ra mới ăn điểm.
→ Thêm vào mục Education: `Worked full-time at Con Cung while completing the degree`.

### 🟠 R-6. Con Cung cần số liệu quy mô — **chỉ bạn trả lời được**

Đây là **điểm yếu lớn nhất còn lại**. Mọi bullet Con Cung đều mô tả *hoạt động*, không có *quy mô hay kết quả*:

> "Delivered .NET voucher APIs for search, creation and updates"

Interviewer đọc xong không biết hệ thống này lớn cỡ nào. So sánh:

> "Delivered voucher APIs handling **~X requests/day** across **Y stores**, cutting batch-creation errors by **Z%**"

**Tôi không bịa các số này.** Cần bạn cung cấp — xem `QUESTIONS.md`. Đây là thứ nâng CV từ 7.5 lên 9.

### 🟡 R-7. Dọn mục Skills

**Bỏ hẳn:**
- `OpenClaw`, `Custom GPTs`, `Agent Skills`, `n8n` → đọc như "sưu tầm tool", không phải năng lực kỹ thuật
- `Node.js`, `Java Spring Boot` → không có dòng kinh nghiệm hay project nào chống lưng
- `Message Queues`, `Vector Databases` → không có bằng chứng trong bất kỳ repo nào

**Giữ nhưng gộp lại:** mục `AI-assisted Development Tools` hiện có 11 item → gộp thành một dòng ngắn:
`AI-assisted development: Claude, Cursor, GitHub Copilot, MCP`.

**Lý do:** 9 nhóm skill dày đặc làm loãng tín hiệu. Reviewer kỹ thuật nhìn danh sách quá dài thì
**giảm** tin tưởng, vì không ai giỏi 80 thứ. Danh sách ngắn hơn, đúng hơn thì mạnh hơn.

### 🟡 R-8. Thông tin liên hệ

| Sửa | Lý do |
| :--- | :--- |
| `0931467024` → `+84 931 467 024` | JD quốc tế / công ty nước ngoài cần mã quốc gia |
| Thêm `linkedin.com/in/...` | Hiện chỉ có GitHub. Recruiter luôn tìm LinkedIn |
| `Target location: Ho Chi Minh City` → `Ho Chi Minh City, Vietnam · Open to hybrid/remote` | "Target location" nghe như chưa ở đó. Bạn **đang** ở HCMC — nói luôn, và mở thêm cửa remote |

### 🟡 R-9. Vấn đề commit history

Cả 4 repo chỉ có **1 commit "push all"**. Interviewer xem history sẽ thấy không có quá trình phát triển,
và dễ đặt câu hỏi liệu code có thật do bạn viết dần hay không.

→ **Với 2 project AI** (`retail-rag-assistant`, `support-ticket-ai-triage`): các commit sau này hãy commit
từng bước có message rõ. Không cần làm lại lịch sử cũ.
→ **Với Layout-Store / Ecommerce-Admin**: xem **D-7** trong `platform-profiles/VERIFICATION_AND_GAPS.md` —
hai repo này còn vấn đề nghiêm trọng hơn (chứa code Con Cung), nên xử lý ở đó trước.

### 🟢 R-10. Thứ tự section theo track

- `CV_Backend` / `CV_FullStack`: Work Experience **trước** Projects ✅ (đang đúng)
- `CV_AI`: Projects **trước** Work Experience ✅ (đang đúng — hợp lý vì kinh nghiệm AI nằm ở project)

Giữ nguyên. Đây là điểm đã làm tốt.

---

## Tác động dự kiến

| | Hiện tại | Sau R-1→R-5, R-7→R-8 | Sau khi có thêm số liệu R-6 |
| :--- | :---: | :---: | :---: |
| CV_Backend | 6.5 | **8.0** | 8.5–9.0 |
| CV_FullStack | 7.5 | **8.5** | 9.0 |
| CV_AI | 5.5 | **8.5** | 9.0 |

Phần tôi làm được ngay: R-1 → R-5, R-7, R-8, R-10 → đã viết sẵn trong
`CV_Backend_v2.md`, `CV_FullStack_v2.md`, `CV_AI_v2.md`.
Phần cần bạn: **R-6** (số liệu Con Cung) và **R-9** (commit history) → `QUESTIONS.md`.
