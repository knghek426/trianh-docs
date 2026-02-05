# ZBS Template

### 📨 ZBS Template Message

**ZBS (Zalo Business Solutions)** là giải pháp gửi tin nhắn thông báo từ Zalo OA tới người dùng đã được Zalo phê duyệt. Các loại tin nhắn bao gồm:

* &#x20;Thông báo giao dịch
* &#x20;Yêu cầu thanh toán
* &#x20;Tin mã OTP
* &#x20;Nhắc lịch thanh toán
* &#x20;Chăm sóc khách hàng
* &#x20;Đánh giá dịch vụ

📌 Tài liệu này hướng dẫn chi tiết **quy trình tạo Template ZBS trên hệ thống CRM TriAnh**.

***

### I. Tổng quan

Template ZBS là thành phần quan trọng trong giao tiếp khách hàng, yêu cầu nội dung phải tuân thủ quy định và được **Zalo kiểm duyệt** trước khi sử dụng.

#### 1. Lịch sử cập nhật

| Ngày       | Người Cập Nhật | Version | Mô tả                       |
| ---------- | -------------- | ------- | --------------------------- |
| 27/01/2026 | Lý Anh Khoa    | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |



***

### II. Các bước thực hiện

#### 1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)

#### 🔹 Bước 1: Truy cập menu quản lý

Tại giao diện chính của CRM, tìm và nhấn vào icon **Mẫu Email, SMS, ZNS**.

![](<../.gitbook/assets/vao-email-template (3).png>)

_Hình 1: Truy cập menu Mẫu Email, SMS, ZNS_

***

#### 🔹 Bước 2: Khởi tạo bản mẫu

Chọn biểu tượng **Dấu +** tại góc giao diện.

Nhấn chọn dòng **Tạo bản mẫu Zalo ZBS**.

![](<../.gitbook/assets/khoi-tao-template (2).png>)

_Hình 2: Thao tác khởi tạo template mới_

***

#### 🔹 Bước 3: Thiết lập nội dung chi tiết

&#x20;**Thông tin cơ bản**

* **Tên mẫu ZBS:** Đặt tên gợi nhớ để quản lý nội bộ.
* **Nguồn liên hệ:** Chọn đúng Zalo OA đang hoạt động.
* **Loại ZBS:** Chọn **Mẫu Tùy Chỉnh**.
* **Mục đích:** Lựa chọn mục đích phù hợp (Giao dịch, Thông báo...).

![](<../.gitbook/assets/thong-tin-co-ban (2).png>)

_Hình 3: Thiết lập các trường thông tin cơ bản_

**Nội dung hiển thị & Tham số**

* **Logo:** Sử dụng ảnh kích thước **400x96 px**, yêu cầu **xóa background** trước khi upload.
* **Tiêu đề & Văn bản:** Bắt buộc nhập đầy đủ. Nếu sử dụng biến động, đặt tên biến trong dấu `{ten_bien}`.
* **Phần Bảng:** Định nghĩa "Tiêu đề" (nhãn) và "Nội dung" (giá trị hoặc biến trong `{}`).
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`** tại mục này.
* **Ghi chú kiểm duyệt:** Giải thích ngắn gọn mục đích gửi tin để Zalo duyệt nhanh hơn.

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac (2).png>)

_Hình 4: Thiết lập hình ảnh và nội dung tin nhắn_

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac-2 (2).png>)

_Hình 5: Hoàn thiện tham số và ghi chú kiểm duyệt_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất.

***

#### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu tin nhắn này yêu cầu tuân thủ nghiêm ngặt các quy định về tài chính của Zalo:

#### 🔹 Đặc điểm riêng của Mẫu Thanh toán

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Yêu cầu thanh toán**.

**⚠️ Quy định về Tài khoản ngân hàng**

* **Tính chính chủ:** Tài khoản nhận tiền phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA đó.
* **Trường hợp ủy quyền:** Nếu dùng tài khoản bên thứ 3 (cá nhân/DN khác), phải cung cấp hợp đồng/văn bản ủy quyền thu hộ qua mục _Ghi chú_ hoặc biểu mẫu hỗ trợ: [go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

**📌 Theo dõi trạng thái**

* Sau khi tạo, theo dõi cột **Trạng thái** trong danh sách:
  * ● **Được duyệt:** Có thể bắt đầu sử dụng để gửi tin.
  * ● **Từ chối:** Xem lý do, chỉnh sửa và tạo lại template mới.

[← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)
