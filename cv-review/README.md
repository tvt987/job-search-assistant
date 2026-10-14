# CV REVIEW — Truong Van Tinh

Review 3 CV đối chiếu với **code thật** trong 4 repo GitHub. Ngày: **2026-10-14**.

| File | Nội dung |
| :--- | :--- |
| **`REVIEW.md`** | **Bắt đầu từ đây.** Điểm từng CV, chẩn đoán, 10 việc cần làm theo mức ưu tiên |
| `EVIDENCE.md` | Đối chiếu từng claim ⟷ dòng code. 15 claim đúng, 4 con số không có cơ sở, 11 điểm mạnh bị bỏ sót |
| `CV_Backend_v2.md` | Bản viết lại — track Backend .NET |
| `CV_FullStack_v2.md` | Bản viết lại — track Full Stack .NET + Angular |
| `CV_AI_v2.md` | Bản viết lại — track AI Application Engineer |
| **`QUESTIONS.md`** | 9 câu cần bạn trả lời để nâng từ 8.5 lên 9.0+ |

## Điểm

| CV | Hiện tại | Sau bản v2 | Sau khi có số liệu Con Cung |
| :--- | :---: | :---: | :---: |
| Backend | 6.5 | **8.0** | 8.5–9.0 |
| FullStack | 7.5 | **8.5** | 9.0 |
| AI | 5.5 | **8.5** | 9.0 |

## Hai kết luận chính

**1. Có 4 con số không tồn tại trong code** — phải xoá:
`10 HTTP scenarios` (thật: 7 test function) · `120 schema combinations` (không có) ·
`720 urgent-rule cases` (không có) · `1.000 SQLite review decisions` (không có).
CV gắn link GitHub nên interviewer sẽ mở repo — `grep` một phút là thấy.

**2. Điểm mạnh thật thì không được nhắc một chữ** — và đây mới là phần đáng giá:
tự implement TF-IDF trên stdlib (không sklearn) · chặn LLM trả lời không dẫn nguồn ·
phòng prompt injection · CI gác regression · rule bảo mật override LLM · mask PII trước khi gọi provider.

→ Sửa cả hai cùng lúc thì CV **vừa an toàn hơn vừa mạnh hơn**. Không phải đánh đổi.

## Chưa làm (chờ bạn)

- **Số liệu quy mô Con Cung** (R-6) — đòn bẩy lớn nhất còn lại, tôi không bịa được
- **D-7** — `Layout-Store` + `Ecommerce-Admin` chứa code Con Cung → chưa gắn link repo vào CV
- **Định dạng xuất** — markdown, PDF hay .docx
