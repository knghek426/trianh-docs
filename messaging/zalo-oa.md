<div style="border:1px solid #fde2e2; background:#fff5f5; padding:20px; border-radius:12px;">
<h2 style="margin-top:0">📨 Zalo OA & ZNS</h2>
<p><strong>Zalo OA (Official Account)</strong> và <strong>ZNS (Zalo Notification Service)</strong> dùng để gửi tin nhắn đã được Zalo phê duyệt tới người dùng:</p>
<ul>
<li>Thông báo giao dịch</li>
<li>OTP</li>
<li>Nhắc thanh toán</li>
<li>Chăm sóc khách hàng</li>
</ul>
<p>📌 Tài liệu này tập trung vào <strong>hướng dẫn tạo Template ZBS trên CRM TriAnh</strong>.</p>
</div>


---


## Tổng quan


Template <strong>ZBS (Zalo Business Service)</strong> là mẫu tin nhắn Zalo được gửi từ Zalo OA của doanh nghiệp tới khách hàng và bắt buộc phải <strong>được Zalo kiểm duyệt</strong> trước khi sử dụng.


---


## Lịch sử cập nhật


<table>
<thead>
<tr><th>Ngày</th><th>Người cập nhật</th><th>Version</th><th>Mô tả</th></tr>
</thead>
<tbody>
<tr><td>27/01/2026</td><td>Lý Anh Khoa</td><td>Ver 1.0</td><td>Bắt đầu soạn tài liệu</td></tr>
</tbody>
</table>


---


## Quy trình tạo template ZBS – Mẫu tuỳ chỉnh


<div style="border-left:4px solid #ff6b6b; padding:16px; margin:24px 0; background:#fff;">
<h3 style="margin-top:0">🔹 Bước 1: Truy cập màn hình tạo template</h3>
<p>Tại giao diện CRM, chọn:</p>
<p><strong>Mẫu Email, SMS, ZNS</strong> → vào màn hình quản lý template</p>
<img src="../assets/zbs/vao-email-template.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />
<p style="font-size:14px; color:#666;">Hình 1: Vị trí menu Mẫu Email, SMS, ZNS</p>
</div>


<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 2: Tạo template Zalo ZBS</h3>
<ol>
<li>Chọn biểu tượng <strong>Zalo</strong></li>
<li>Nhấn <strong>Tạo mới</strong> để khởi tạo template</li>
</ol>
</div>


<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 3: Nhập thông tin template</h3>
<h4>📌 Thông tin cơ bản</h4>
<table>
<tr><td><strong>Tên mẫu ZBS</strong></td><td>Tên nội bộ để quản lý</td></tr>
<tr><td><strong>Nguồn liên hệ</strong></td><td>Zalo OA tương ứng</td></tr>
<tr><td><strong>Loại ZBS</strong></td><td>Tuỳ chỉnh</td></tr>
<tr><td><strong>Mục đích gửi</strong></td><td>Giao dịch / Thông báo</td></tr>
</table>


<h4>🖼 Nội dung hiển thị</h4>
<ul>
<li><strong>Logo:</strong> Kích thước 400×96 px</li>
<li><strong>Tiêu đề:</strong> Có thể chứa biến <code>{}</code></li>
<li><strong>Văn bản:</strong> Tối thiểu 1 ô, biến đặt trong <code>{}</code></li>
</ul>
</div>


<div style="display:flex; justify-content:space-between; margin-top:40px;">
<a href="../messaging/sms-brandname.md">← SMS Brandname</a>
<a href="../api/overview.md">Hướng dẫn API →</a>
</div>