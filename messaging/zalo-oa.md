# ZBS Template
=======
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
>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)

### 📨 ZBS Template Message

**ZBS (Zalo Business Solutions)** dùng để gửi tin nhắn qua Zalo và đã được Zalo phê duyệt tới người dùng bao gồm những tin :

* Thông báo giao dịch
* Yêu cầu thanh toán
* Tin OTP
* Nhắc thanh toán
* Chăm sóc khách hàng
* Đánh giá dịch vụ

📌 Tài liệu này tập trung vào **hướng dẫn tạo Template ZBS trên CRM TriAnh**.

***

### I. Tổng quan

Template ZBS là thành phần quan trọng trong giao tiếp khách hàng, yêu cầu nội dung phải tuân thủ quy định và được **Zalo kiểm duyệt** trước khi gửi.

#### 1. Lịch sử cập nhật

| Ngày       | Người Cập Nhật | Version | Mô tả                       |
| ---------- | -------------- | ------- | --------------------------- |
| 27/01/2026 | Lý Anh Khoa    | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |

***

### II. Các bước thực hiện

#### 1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)

#### 🔹 Bước 1: Truy cập menu

Tại giao diện CRM, click vào icon **Mẫu Email, SMS, ZNS** để vào giao diện quản lý.

![](<../.gitbook/assets/vao-email-template (1).png>)

Hình 1: Vị trí menu Mẫu Email, SMS, ZNS

#### 🔹 Bước 2: Khởi tạo

1. Click vào biểu tượng **Dấu +**.
2. Nhấn nút **Tạo bản mẫu Zalo ZBS** để khởi tạo template .
3. ![](../.gitbook/assets/khoi-tao-template.png)
4. Hình 2: Khởi tạo template

#### 🔹 Bước 3: Thiết lập nội dung

**📌 Thông tin cơ bản**

* **Tên mẫu ZBS:** Tên nội bộ để quản lý.
* **Nguồn liên hệ:** Chọn đúng Zalo OA của mình.
* **Loại ZBS:** Chọn "Mẫu Tùy Chỉnh".
* **Mục đích:** Chọn mục đích gửi tương ứng.
* ![](../.gitbook/assets/thong-tin-co-ban.png)
* Hình 3: Nhập thông tin cơ bản

**🖼 Nội dung hiển thị**

* **Logo:** Xử lý ảnh kích thước **400x96 px và xóa background** trước khi upload.
* **Tiêu đề & Văn bản:** Biến phải đặt trong dấu `{} nếu có`. _Lưu ý: Phải nhập tối thiểu 1 ô văn bản và tiêu đề._
* **Phần Bảng:** "Tiêu đề" là tên biến, "Nội dung" là giá trị biến (đặt trong `{}`).
* **Nút thao tác:** Tùy chọn thêm nếu cần dẫn link.
* **Tham số:** Tuyệt đối **không bỏ dấu ngoặc `{}`** ở phần này.
* **Ghi chú kiểm duyệt:** Điền nội dung bất kỳ để hỗ trợ admin Zalo duyệt (VD: "Template dùng để xác nhận đơn hàng").
* **Mã tracking:** Đây là mã tự sinh từ hệ thống.
* ![](../.gitbook/assets/dien-cac-truong-thong-tin-khac.png)
* Hình 4: Thêm logo, nhập tiêu đề và văn bản
* ![](../.gitbook/assets/dien-cac-truong-thong-tin-khac-2.png)
* Hình 5: Nhập các trường còn lại theo lưu ý
=======
<div style="border-left:4px solid #ff6b6b; padding:16px; margin:24px 0; background:#fcfcfc;">
<h3 style="margin-top:0">🔹 Bước 1: Truy cập menu quản lý</h3>
<p>Tại giao diện chính của CRM, tìm và nhấn vào icon <strong>Mẫu Email, SMS, ZNS</strong>.</p>
<img src="../assets/zbs/vao-email-template.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />
<p style="font-size:13px; color:#888; text-align:center;"><i>Hình 1: Truy cập menu Mẫu Email, SMS, ZNS</i></p>
</div>

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 2: Khởi tạo bản mẫu</h3>
<ol>
<li>Chọn biểu tượng <strong>Dấu +</strong> tại góc giao diện</li>
<li>Nhấn chọn dòng <strong>Tạo bản mẫu Zalo ZBS</strong></li>
</ol>
<img src="../assets/zbs/khoi-tao-template.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />
<p style="font-size:13px; color:#888; text-align:center;"><i>Hình 2: Thao tác khởi tạo template mới</i></p>
</div>

<div style="border:1px solid #eee; border-radius:12px; padding:20px; margin:24px 0;">
<h3 style="margin-top:0">🔹 Bước 3: Thiết lập nội dung chi tiết</h3>

<h4>📌 3.1. Thông tin cơ bản</h4>
<ul>
<li><strong>Tên mẫu ZBS:</strong> Đặt tên gợi nhớ để quản lý nội bộ</li>
<li><strong>Nguồn liên hệ:</strong> Chọn đúng Zalo OA đang hoạt động</li>
<li><strong>Loại ZBS:</strong> Chọn <strong>Mẫu Tùy Chỉnh</strong></li>
<li><strong>Mục đích:</strong> Lựa chọn mục đích phù hợp (Giao dịch, Thông báo...)</li>
</ul>
<img src="../assets/zbs/thong-tin-co-ban.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />
<p style="font-size:13px; color:#888; text-align:center;"><i>Hình 3: Thiết lập các trường thông tin cơ bản</i></p>

<hr style="border:0; border-top:1px dashed #eee; margin:20px 0;">

<h4>🖼 3.2. Nội dung hiển thị & Tham số</h4>
<ul>
<li><strong>Logo:</strong> Sử dụng ảnh kích thước <strong>400x96 px</strong>, yêu cầu <strong>xóa background</strong> trước khi upload</li>
<li><strong>Tiêu đề & Văn bản:</strong> Bắt buộc nhập đầy đủ. Nếu sử dụng biến động, đặt tên biến trong dấu <code>{ten_bien}</code></li>
<li><strong>Phần Bảng:</strong> Định nghĩa "Tiêu đề" (nhãn) và "Nội dung" (giá trị hoặc biến trong <code>{}</code>)</li>
<li><strong>Tham số:</strong> Tuyệt đối <strong>không xóa dấu ngoặc <code>{}</code></strong> tại mục này</li>
<li><strong>Ghi chú kiểm duyệt:</strong> Giải thích ngắn gọn mục đích gửi tin để Zalo duyệt nhanh hơn</li>
</ul>

<img src="../assets/zbs/dien-cac-truong-thong-tin-khac.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin:12px 0;" />
<p style="font-size:13px; color:#888; text-align:center;"><i>Hình 4: Thiết lập hình ảnh và nội dung tin nhắn</i></p>

<img src="../assets/zbs/dien-cac-truong-thong-tin-khac-2.png" style="width:100%; max-width:900px; border-radius:8px; border:1px solid #eee; margin-top:12px;" />
<p style="font-size:13px; color:#888; text-align:center;"><i>Hình 5: Hoàn thiện tham số và ghi chú kiểm duyệt</i></p>

<p style="margin-top:15px;">👉 Sau khi kiểm tra kỹ, nhấn nút <strong>Tạo</strong> để gửi yêu cầu phê duyệt lên hệ thống Zalo.</p>
</div>
>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)

👉 Kiểm tra lại và nhấn nút **Tạo** để đẩy lên Zalo.

***

#### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu tin nhắn này yêu cầu tuân thủ nghiêm ngặt các quy định về tài chính của Zalo:

#### 🔹 Cấu hình thanh toán

Tại Bước 3, chọn **Loại ZBS: Yêu cầu thanh toán**.

**⚠️ Quy định về Tài khoản ngân hàng:**

* Tài khoản phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA.
* **Trường hợp dùng tài khoản khác** (Cá nhân/DN khác): Phải có văn bản/hợp đồng ủy quyền thu hộ. Cung cấp minh chứng qua mục _Ghi chú_ hoặc qua biểu mẫu: [https://go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

**📌 Hoàn tất:**

* Kiểm tra trạng thái tại màn hình danh sách: **Được duyệt** hoặc **Từ chối**.
* **Lưu ý:** Nếu bị từ chối, hệ thống yêu cầu tạo lại template mới thay vì chỉnh sửa bản cũ.

[← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)
=======
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
>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)
