# ZBS Template

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

Template **ZBS (Zalo Business Solutions)** là mẫu tin nhắn Zalo được gửi từ Zalo OA của doanh nghiệp tới khách hàng và bắt buộc phải **được Zalo kiểm duyệt** trước khi sử dụng.

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

👉 Kiểm tra lại và nhấn nút **Tạo** để đẩy lên Zalo.

***

#### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu này yêu cầu khắt khe hơn về thông tin tài chính:

#### 🔹 Cấu hình thanh toán

Tại Bước 3, chọn **Loại ZBS: Yêu cầu thanh toán**.

**⚠️ Quy định về Tài khoản ngân hàng:**

* Tài khoản phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA.
* **Trường hợp dùng tài khoản khác** (Cá nhân/DN khác): Phải có văn bản/hợp đồng ủy quyền thu hộ. Cung cấp minh chứng qua mục _Ghi chú_ hoặc qua biểu mẫu: [https://go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

**📌 Hoàn tất:**

* Kiểm tra trạng thái tại màn hình danh sách: **Được duyệt** hoặc **Từ chối**.
* **Lưu ý:** Nếu bị từ chối, hệ thống yêu cầu tạo lại template mới thay vì chỉnh sửa bản cũ.

[← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)
