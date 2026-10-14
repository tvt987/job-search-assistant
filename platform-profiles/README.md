# PLATFORM PROFILES — Bộ nội dung hoàn thiện hồ sơ 6 nền tảng

Sinh ngày **2026-10-14** từ `resumes/*.pdf` + `APPLICANT_CONTEXT.md` + `application-templates/`.

> ## ⚠️ Đọc trước
> Session này **không có công cụ browser**, nên tôi **chưa đăng nhập và chưa cập nhật** profile nào
> trên LinkedIn/ITviec/TopDev/VietnamWorks/CareerViet/Glints. Không có nền tảng nào được đánh dấu
> là đã hoàn thiện.
> Thư mục này là **nội dung đã soạn sẵn, đã kiểm tra giới hạn ký tự, sẵn sàng dán**.
> Chi tiết lý do + 3 phương án xử lý: `VERIFICATION_AND_GAPS.md` **Phần 3**.

---

## Thứ tự đọc

| # | File | Nội dung |
| :-- | :--- | :--- |
| 1 | **`VERIFICATION_AND_GAPS.md`** | **Bắt đầu từ đây.** Kết quả đối chiếu 3 CV (6 điểm lệch cần bạn xác nhận) + 12 field `NEEDS_USER_INPUT` + trạng thái đăng nhập |
| 2 | `MASTER_CONTENT.md` | Khối nội dung chuẩn: headline, About (4 bản), experience bullets theo 3 track, 5 project, skill đã xếp hạng, số năm kinh nghiệm |
| 3 | `linkedin.md` | 18 bước lên All-Star + 50 skill đúng thứ tự |
| 4 | `itviec.md` | Lên mức "Rất tốt" + cảnh báo nhãn Fresher/Undergraduate |
| 5 | `vietnamworks.md` | + vấn đề salary chặn 100% profile |
| 6 | `topdev.md` | Bản VI, track Backend |
| 7 | `careerviet.md` | Bản VI + thang đánh giá skill |
| 8 | `glints.md` | Bản EN, track AI, + lưu ý salary khu vực SEA |

---

## Track CV theo nền tảng

| Nền tảng | Track profile | CV upload mặc định |
| :--- | :--- | :--- |
| LinkedIn | FullStack | `CV_FullStack_TruongVanTinh.pdf` |
| ITviec | Backend | `CV_Backend_TruongVanTinh.pdf` |
| TopDev | Backend | `CV_Backend_TruongVanTinh.pdf` |
| VietnamWorks | FullStack | `CV_FullStack_TruongVanTinh.pdf` |
| CareerViet | FullStack | `CV_FullStack_TruongVanTinh.pdf` |
| Glints | FullStack + AI | `CV_FullStack_TruongVanTinh.pdf` → đổi `CV_AI_...` cho JD AI |

---

## 🔴 ĐANG CHẶN: xem `VERIFICATION_AND_GAPS.md` mục **D-7**

Hai repo `tvt987/Layout-Store` và `tvt987/Ecommerce-Admin` đang **public** và chứa **source code
Con Cung** (`CCI.*` namespace, `nexus.ingress.concung.io`, `cdn1.concung.com`). Tôi đã **bỏ link
hai repo này khỏi mọi profile** và chờ bạn quyết. Không có credential nào bị lộ — đã quét riêng.

## 4 câu hỏi đã trả lời ✅ *(2026-10-14)*

| | Trả lời |
| :--- | :--- |
| Tháng tốt nghiệp | `06/2026` *(năm bắt đầu `2022` là suy luận — xác nhận nếu khác)* |
| Mức lương mong muốn | `28.000.000 – 32.000.000 VND/tháng`, thương lượng |
| Ngày bắt đầu | 1 tháng sau khi nhận offer |
| FPT | `FPT Software` ⚠️ *3 CV PDF vẫn ghi `FPT` — nên sửa cho khớp* |

### Còn thiếu (ít quan trọng hơn)
Ngày sinh (G-9) · ảnh profile (G-11) · LinkedIn slug (G-12) · số năm Python/FastAPI (G-2)

### Quyết định đã chốt

- **G-8 — chế độ hiển thị: ✅ công khai hoàn toàn** *(2026-10-14)*. Bật `#OpenToWork` trên LinkedIn
  và mở hồ sơ cho mọi NTD trên cả 6 sàn. Đã áp dụng vào cả 6 file nền tảng.
- **Hướng thực thi: cấp browser access** — xem mục dưới.

---

## Cách thực thi: chạy session trên máy bạn

Bước này cần **máy của bạn** — session hiện tại chạy trong container cloud nên không với tới
browser và các session đăng nhập của bạn được.

Để tôi tự điền profile, mở lại công việc này trong một session chạy trên máy bạn:
- **Claude Desktop app**, hoặc
- `claude remote-control` trong terminal, tại thư mục repo này (session sẽ hiện trong Claude Code app).

Khi đó tôi sẽ: kiểm tra từng trang xem account đang đăng nhập có đúng `tinhkun102@gmail.com` →
tự điền các field đã xác minh → **dừng và hỏi bạn** ở các field G-1…G-12 và ở mọi bước OTP/MFA/CAPTCHA.

---

## Nguyên tắc đã áp dụng khi soạn

- ✅ Mọi câu đều truy vết được về CV hoặc `APPLICANT_CONTEXT.md`.
- ✅ Không bịa công ty, dự án, chứng chỉ, con số, số năm kinh nghiệm.
- ✅ Giữ chức danh Con Cung là `Full Stack Developer` trên mọi nền tảng — kể cả khi ứng tuyển
  Backend. Muốn nhấn Backend thì đổi headline và thứ tự bullet, **không** đổi chức danh.
- ✅ English luôn khai `Conversational` / `Intermediate` / `Professional working` — không bao giờ
  `Fluent` / `Native` / `Advanced`.
- ✅ Không điền Certifications / Awards / References / Volunteer — CV không có các mục này.
- ✅ Không đưa `Node.js` / `Java Spring Boot` / `Message Queues` / `Vector Databases` vào skill tag
  (chi tiết: D-4).
- ✅ Không có mật khẩu, cookie, session token, OTP nào trong bất kỳ file nào ở đây.
