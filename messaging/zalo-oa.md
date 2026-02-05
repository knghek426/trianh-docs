<div style="border:1px solid #fde2e2; background:#fff5f5; padding:20px; border-radius:12px;">
<h2 style="margin-top:0">📨 ZBS Template Message</h2>
<p><strong>ZBS (Zalo Business Solutions)</strong> là giải pháp gửi tin nhắn thông báo từ Zalo OA tới người dùng đã được Zalo phê duyệt. Các loại tin nhắn bao gồm:</p>
<ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
<li>• Thông báo giao dịch</li>
<li>• Yêu cầu thanh toán</li>
<li>• Tin mã OTP</li>
<li>• Nhắc lịch thanh toán</li>
<li>• Chăm sóc khách hàng</li>
<li>• Đánh giá dịch vụ</li>
</ul>
<p style="margin-bottom:0">📌 Tài liệu này hướng dẫn chi tiết <strong>quy trình tạo Template ZBS trên hệ thống CRM TriAnh</strong>.</p>
</div>

---

## I. Tổng quan

Template ZBS là thành phần quan trọng trong giao tiếp khách hàng, yêu cầu nội dung phải tuân thủ quy định và được **Zalo kiểm duyệt** trước khi sử dụng.

### 1. Lịch sử cập nhật
| Ngày | Người Cập Nhật | Version | Mô tả |
| :--- | :--- | :--- | :--- |
| 27/01/2026 | Lý Anh Khoa | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |

---

## II. Các bước thực hiện

### 1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)

<div style="border-left:4px solid #ff6b6b; padding:16px; margin:24px 0; background:#fcfcfc;">
<h3 style="margin-top:0">🔹 Bước 1: Truy cập menu quản lý</h3>
<p>Tại giao diện chính của CRM, tìm và nhấn vào icon <strong>Mẫu Email, SMS, ZNS</strong>.</p>
</div>

<img src="../assets/zbs/vao-email-template.png" style="width:100%; max-width:1000px; border-radius:8px; border:1px solid #eee; display: block; margin: 20px 0;" />
<p style="font-size:14px; color:#888; margin-top:-10px; margin-bottom:25px;"><i>Hình 1: Truy cập menu Mẫu Email, SMS, ZNS</i></p>

---

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 2: Khởi tạo bản mẫu</h3>
<ol>
<li>Chọn biểu tượng <strong>Dấu +</strong> tại góc giao diện.</li>
<li>Nhấn chọn dòng <strong>Tạo bản mẫu Zalo ZBS</strong>.</li>
</ol>
</div>

<img src="../assets/zbs/khoi-tao-template.png" style="width:100%; max-width:1000px; border-radius:8px; border:1px solid #eee; display: block; margin: 20px 0;" />
<p style="font-size:14px; color:#888; margin-top:-10px; margin-bottom:25px;"><i>Hình 2: Thao tác khởi tạo template mới</i></p>

---

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 3: Thiết lập nội dung chi tiết</h3>

<h4>📌 3.1. Thông tin cơ bản</h4>
<ul>
<li><strong>Tên mẫu ZBS:</strong> Đặt tên gợi nhớ để quản lý nội bộ.</li>
<li><strong>Nguồn liên hệ:</strong> Chọn đúng Zalo OA đang hoạt động.</li>
<li><strong>Loại ZBS:</strong> Chọn <strong>Mẫu Tùy Chỉnh</strong>.</li>
<li><strong>Mục đích:</strong> Lựa chọn mục đích phù hợp (Giao dịch, Thông báo...).</li>
</ul>
</div>

<img src="../assets/zbs/thong-tin-co-ban.png" style="width:100%; max-width:1000px; border-radius:8px; border:1px solid #eee; display: block; margin: 20px 0;" />
<p style="font-size:14px; color:#888; margin-top:-10px; margin-bottom:25px;"><i>Hình 3: Thiết lập các trường thông tin cơ bản</i></p>

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h4>🖼 3.2. Nội dung hiển thị & Tham số</h4>
<ul>
<li><strong>Logo:</strong> Sử dụng ảnh kích thước <strong>400x96 px</strong>, yêu cầu <strong>xóa background</strong> trước khi upload.</li>
<li><strong>Tiêu đề & Văn bản:</strong> Bắt buộc nhập đầy đủ. Nếu sử dụng biến động, đặt tên biến trong dấu <code>{ten_bien}</code>.</li>
<li><strong>Phần Bảng:</strong> Định nghĩa "Tiêu đề" (nhãn) và "Nội dung" (giá trị hoặc biến trong <code>{}</code>).</li>
<li><strong>Tham số:</strong> Tuyệt đối <strong>không xóa dấu ngoặc <code>{}</code></strong> tại mục này.</li>
<li><strong>Ghi chú kiểm duyệt:</strong> Giải thích ngắn gọn mục đích gửi tin để Zalo duyệt nhanh hơn.</li>
</ul>
</div>

<img src="../assets/zbs/dien-cac-truong-thong-tin-khac.png" style="width:100%; max-width:1000px; border-radius:8px; border:1px solid #eee; display: block; margin: 20px 0;" />
<p style="font-size:14px; color:#888; margin-top:-10px; margin-bottom:25px;"><i>Hình 4: Thiết lập hình ảnh và nội dung tin nhắn</i></p>

<img src="../assets/zbs/dien-cac-truong-thong-tin-khac-2.png" style="width:100%; max-width:1000px; border-radius:8px; border:1px solid #eee; display: block; margin: 20px 0;" />
<p style="font-size:14px; color:#888; margin-top:-10px; margin-bottom:25px;"><i>Hình 5: Hoàn thiện tham số và ghi chú kiểm duyệt</i></p>

<p style="padding-left: 20px;">👉 Sau khi kiểm tra kỹ, nhấn nút <strong>Tạo</strong> để hoàn tất.</p>

---

### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu tin nhắn này yêu cầu tuân thủ nghiêm ngặt các quy định về tài chính của Zalo:

<div style="border-left:4px solid #3498db; padding:16px; margin:24px 0; background:#f4f9ff;">
<h3 style="margin-top:0">🔹 Đặc điểm riêng của Mẫu Thanh toán</h3>
<p>Tại <strong>Bước 3</strong>, mục <strong>Loại ZBS</strong> hãy chọn: <strong>Yêu cầu thanh toán</strong>.</p>
</div>

<h4>⚠️ Quy định về Tài khoản ngân hàng</h4>
<ul>
<li><strong>Tính chính chủ:</strong> Tài khoản nhận tiền phải <strong>đứng tên chính doanh nghiệp</strong> sở hữu Zalo OA đó.</li>
<li><strong>Trường hợp ủy quyền:</strong> Nếu dùng tài khoản bên thứ 3 (cá nhân/DN khác), phải cung cấp hợp đồng/văn bản ủy quyền thu hộ qua mục <em>Ghi chú</em> hoặc biểu mẫu hỗ trợ: <a href="https://go.zalo.me/zbs-support" target="_blank">go.zalo.me/zbs-support</a>.</li>
</ul>

<h4>📌 Theo dõi trạng thái</h4>
<ul>
<li>Sau khi tạo, theo dõi cột <strong>Trạng thái</strong> trong danh sách:
    <ul>
        <li><span style="color:#27ae60">●</span> <strong>Được duyệt:</strong> Có thể bắt đầu sử dụng để gửi tin.</li>
        <li><span style="color:#e74c3c">●</span> <strong>Từ chối:</strong> Xem lý do, chỉnh sửa và tạo lại template mới.</li>
    </ul>
</li>
</ul>

<div style="display:flex; justify-content:space-between; margin-top:40px; border-top:1px solid #eee; padding-top:20px;">
<a href="../messaging/sms-brandname.md" style="text-decoration:none; color:#666;">← SMS Brandname</a>
<a href="../api/overview.md" style="text-decoration:none; color:#666;">Hướng dẫn API →</a>
</div>