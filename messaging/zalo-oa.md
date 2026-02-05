<div style="border:1px solid #fde2e2; background:#fff5f5; padding:20px; border-radius:12px;">
<h2 style="margin-top:0">📨 ZBS Template Message</h2>
<p><strong>ZBS (Zalo Business Solutions) </strong>dùng để gửi tin nhắn qua Zalo và đã được Zalo phê duyệt tới người dùng bao gồm những tin :</p>
<ul>
<li>Thông báo giao dịch</li>
<li>Yêu cầu thanh toán</li>
<li>Tin OTP</li>
<li>Nhắc thanh toán</li>
<li>Chăm sóc khách hàng</li>
<li>Đánh giá dịch vụ</li>
</ul>
<p>📌 Tài liệu này tập trung vào <strong>hướng dẫn tạo Template ZBS trên CRM TriAnh</strong>.</p>
</div>

---

## I. Tổng quan

Template **ZBS (Zalo Business Solutions)** là mẫu tin nhắn Zalo được gửi từ Zalo OA của doanh nghiệp tới khách hàng và bắt buộc phải **được Zalo kiểm duyệt** trước khi sử dụng.

### 1. Lịch sử cập nhật
| Ngày | Người Cập Nhật | Version | Mô tả |
| :--- | :--- | :--- | :--- |
| 27/01/2026 | Lý Anh Khoa | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |

---

## II. Các bước thực hiện

### 1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)

<div style="border-left:4px solid #ff6b6b; padding:16px; margin:24px 0; background:#fff;">
<h3 style="margin-top:0">🔹 Bước 1: Truy cập menu</h3>
<p>Tại giao diện CRM, click vào icon <strong>Mẫu Email, SMS, ZNS</strong> để vào giao diện quản lý.</p>
<img src="../assets/zbs/vao-email-template.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />

<p style="font-size:14px; color:#666;">Hình 1: Vị trí menu Mẫu Email, SMS, ZNS</p>
</div>

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 2: Khởi tạo</h3>
<ol>
<li>Click vào biểu tượng <strong>Dấu +</strong>.</li>
<li>Nhấn nút <strong>Tạo bản mẫu Zalo ZBS</strong> để khởi tạo template .</li>
<img src="../assets/zbs/khoi-tao-template.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />

<p style="font-size:14px; color:#666;">Hình 2: Khởi tạo template</p>
</ol>
</div>

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 3: Thiết lập nội dung</h3>

<h4>📌 Thông tin cơ bản</h4>
<ul>
<li><strong>Tên mẫu ZBS:</strong> Tên nội bộ để quản lý.</li>
<li><strong>Nguồn liên hệ:</strong> Chọn đúng Zalo OA của mình.</li>
<li><strong>Loại ZBS:</strong> Chọn "Mẫu Tùy Chỉnh".</li>
<li><strong>Mục đích:</strong> Chọn mục đích gửi tương ứng.</li>
<img src="../assets/zbs/thong-tin-co-ban.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />

<p style="font-size:14px; color:#666;">Hình 3: Nhập thông tin cơ bản</p>
</ul>

<h4>🖼 Nội dung hiển thị</h4>
<ul>
<li><strong>Logo:</strong> Xử lý ảnh kích thước <strong>400x96 px và xóa background </strong> trước khi upload.</li>
<li><strong>Tiêu đề & Văn bản:</strong> Biến phải đặt trong dấu <code>{} nếu có</code>. <em>Lưu ý: Phải nhập tối thiểu 1 ô văn bản và tiêu đề.</em></li>
<li><strong>Phần Bảng:</strong> "Tiêu đề" là tên biến, "Nội dung" là giá trị biến (đặt trong <code>{}</code>).</li>
<li><strong>Nút thao tác:</strong> Tùy chọn thêm nếu cần dẫn link.</li>
<li><strong>Tham số:</strong> Tuyệt đối <strong>không bỏ dấu ngoặc <code>{}</code></strong> ở phần này.</li>
<li><strong>Ghi chú kiểm duyệt:</strong> Điền nội dung bất kỳ để hỗ trợ admin Zalo duyệt (VD: "Template dùng để xác nhận đơn hàng").</li>
<li><strong>Mã tracking:</strong> Đây là mã tự sinh từ hệ thống.</li>
<img src="../assets/zbs/dien-cac-truong-thong-tin-khac.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />

<p style="font-size:14px; color:#666;">Hình 4: Thêm logo, nhập tiêu đề và văn bản</p>

<img src="../assets/zbs/dien-cac-truong-thong-tin-khac-2.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />

<p style="font-size:14px; color:#666;">Hình 5: Nhập các trường còn lại theo lưu ý</p>
</ul>

<p>👉 Kiểm tra lại và nhấn nút <strong>Tạo</strong> để đẩy lên Zalo.</p>
</div>

---

### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu này yêu cầu khắt khe hơn về thông tin tài chính:

<div style="border-left:4px solid #3498db; padding:16px; margin:24px 0; background:#f9f9f9;">
<h3 style="margin-top:0">🔹 Cấu hình thanh toán</h3>
<p>Tại Bước 3, chọn <strong>Loại ZBS: Yêu cầu thanh toán</strong>.</p>
</div>

<h4>⚠️ Quy định về Tài khoản ngân hàng:</h4>
<ul>
<li>Tài khoản phải <strong>đứng tên chính doanh nghiệp</strong> sở hữu Zalo OA.</li>
<li><strong>Trường hợp dùng tài khoản khác</strong> (Cá nhân/DN khác): Phải có văn bản/hợp đồng ủy quyền thu hộ. Cung cấp minh chứng qua mục <em>Ghi chú</em> hoặc qua biểu mẫu: <a href="https://go.zalo.me/zbs-support">https://go.zalo.me/zbs-support</a>.</li>
</ul>

<h4>📌 Hoàn tất:</h4>
<ul>
<li>Kiểm tra trạng thái tại màn hình danh sách: <strong>Được duyệt</strong> hoặc <strong>Từ chối</strong>.</li>
<li><strong>Lưu ý:</strong> Nếu bị từ chối, hệ thống yêu cầu tạo lại template mới thay vì chỉnh sửa bản cũ.</li>
</ul>

<div style="display:flex; justify-content:space-between; margin-top:40px;">
<a href="../messaging/sms-brandname.md">← SMS Brandname</a>
<a href="../api/overview.md">Hướng dẫn API →</a>
</div>