# HƯỚNG DẪN BẬT CLAUDE IN CHROME

Để agent điền profile tuyển dụng bằng **session đăng nhập sẵn** trên Chrome của bạn.
Nguồn: [Claude Code — Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome) ·
[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)

---

## Tại sao phải làm trên máy bạn

Claude in Chrome *"opens new tabs for browser tasks and **shares your browser's login state**, so it can
access any site you're already signed into"*. Đúng thứ cần cho việc này: bạn đã đăng nhập LinkedIn/ITviec
rồi thì agent vào được ngay, **không cần mật khẩu của bạn**.

Và: *"When Claude encounters a login page or CAPTCHA, **it pauses and asks you to handle it manually**"* —
khớp với quy định trong `CLAUDE.md` là chỉ dừng đúng bước cần bạn.

---

## Yêu cầu trước khi bắt đầu

| # | Yêu cầu | Ghi chú |
| :-- | :--- | :--- |
| 1 | **Chrome** (hoặc Edge, Brave, Arc, Vivaldi, Opera) | ❌ **Không hỗ trợ WSL** (Windows Subsystem for Linux) |
| 2 | **Extension Claude in Chrome** v1.0.36+ | [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) |
| 3 | **Claude Code** cài trên máy | Kiểm tra: `claude --version` |
| 4 | **Gói Anthropic trực tiếp**: Pro, Max, Team hoặc Enterprise | ❌ Không dùng được qua Bedrock / Vertex / Microsoft Foundry |
| 5 | Đăng nhập bằng **`/login`** | ❌ Nếu dùng **API key** hoặc token từ `claude setup-token` thì Chrome integration **luôn bị tắt**, kể cả khi truyền `--chrome` |

---

## Các bước

### 1. Cài extension
Vào [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn),
cài extension, đăng nhập bằng tài khoản Claude của bạn, và **ghim vào toolbar**.

> ⚠️ **Sau lần cài đầu tiên, khởi động lại Chrome.** Claude Code ghi một file *native messaging host
> config*, và Chrome chỉ đọc file này khi startup. Không restart thì extension thường báo "Not detected".

### 2. Clone repo về máy
```bash
git clone https://github.com/tvt987/job-search-assistant.git
cd job-search-assistant
git checkout claude/serene-archimedes-3bvvdm
```
> Branch `claude/serene-archimedes-3bvvdm` chứa toàn bộ thư mục `platform-profiles/`.

### 3. Đăng nhập Claude Code (nếu chưa)
```bash
claude
```
rồi trong phiên: `/login`

### 4. Mở Chrome và đăng nhập các sàn
Đăng nhập sẵn bằng **`tinhkun102@gmail.com`**:
LinkedIn · ITviec · TopDev · VietnamWorks · CareerViet · Glints

> Tài khoản **Claude** và tài khoản **sàn tuyển dụng** là hai thứ khác nhau — không cần trùng nhau.

### 5. Khởi động Claude Code với Chrome
```bash
claude --chrome
```
Lần đầu sẽ có một dialog giới thiệu + giải thích cách site permission hoạt động → **Enter** để tiếp tục.

### 6. Kiểm tra kết nối
Trong phiên Claude Code, gõ:
```
/chrome
```
✅ Thành công khi thấy **`Status: Enabled`** và **`Extension: Installed`**.

### 7. Ra lệnh
```
Đọc platform-profiles/ và hoàn thiện profile trên LinkedIn trước, rồi ITviec.
Kiểm tra account đang đăng nhập có đúng tinhkun102@gmail.com trước khi sửa gì.
```

---

## Bật sẵn cho các phiên sau (không cần `--chrome` mỗi lần)

Gõ `/chrome` → chọn **`Enabled by default`**.

> ⚠️ Đánh đổi: bật mặc định làm **tăng lượng context tiêu thụ**, vì browser tools và hướng dẫn của chúng
> luôn được nạp. Nếu thấy tốn context thì tắt đi, chỉ dùng `--chrome` khi cần.

---

## ⚠️ Repo KHÔNG thể tự bật Chrome — bạn phải tự chạy

Nếu bạn thấy cảnh báo này:
```
Claude Code ignored CLAUDE_CODE_ENABLE_CFC in this project's settings:
a project can't turn on Claude in Chrome.
```
thì đây là **cơ chế bảo mật có chủ đích**, không phải lỗi: *"a repository you check out must not be able
to connect Claude to your browser"*. Một repo bạn clone về **không được phép** tự kết nối Claude vào
trình duyệt của bạn.

→ Nghĩa là: **tôi không thể tự bật Chrome từ trong repo này.** Bắt buộc bạn chạy `claude --chrome`
hoặc `/chrome` → `Enabled by default`.

*(Repo `job-search-assistant` hiện **không** set biến này — nêu ra để bạn biết nếu sau này gặp.)*

---

## Phân quyền theo site

Site permission **kế thừa từ extension**, quản lý trong settings của extension —
bạn kiểm soát site nào Claude được xem, click và gõ.

Khi agent thao tác, có thể xuất hiện prompt bắt đầu bằng `Claude in Chrome wants to`,
kèm option cho phép tất cả hành động trên site đó trong phiên hiện tại.

---

## Xử lý sự cố

| Lỗi | Nguyên nhân | Cách sửa |
| :--- | :--- | :--- |
| `Extension: Not detected` | Extension chưa cài / bị disable | Kiểm tra `chrome://extensions`; **restart Chrome** (xem bước 1) |
| `Browser extension is not connected` | Extension đăng nhập **tài khoản hoặc organization khác** với Claude Code | Gõ `/status`, đọc dòng `Organization`, rồi logout/login extension vào đúng org đó |
| `Status: Not connected` | Kết nối của phiên đã chết | `/chrome` → **Reconnect extension** |
| `Receiving end does not exist` | Service worker của extension idle (phiên dài) | `/chrome` → **Reconnect extension** |
| `No tab available` | Agent thao tác trước khi tab sẵn sàng | Yêu cầu tạo tab mới rồi thử lại |
| Browser treo | Có modal dialog (alert/confirm) chặn page | Tự tắt dialog trong Chrome, rồi bảo agent tiếp tục |

> ⚠️ **Đừng logout extension** nếu chưa thử các cách khác — logout sẽ mất shortcuts và scheduled tasks
> đã lưu trong đó.

Nếu vẫn lỗi, kiểm tra file config tồn tại chưa:
- **macOS:** `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json`
- **Linux:** `~/.config/google-chrome/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json`
- **Windows:** registry `HKCU\Software\Google\Chrome\NativeMessagingHosts\`

---

## 🔴 Làm trước khi profile lên sóng công khai

Bạn đã chọn **công khai hoàn toàn** (`#OpenToWork`). Trước khi bật, xử lý **D-7** trong
`VERIFICATION_AND_GAPS.md`: hai repo `Layout-Store` và `Ecommerce-Admin` đang public và chứa
source code Con Cung. Nên chuyển Private / xoá / viết lại bản sạch **trước**, vì khi hồ sơ đã công khai
thì link repo có thể đã bị index.
