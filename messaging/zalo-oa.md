# ZBS Template

## ZBS Template

\=======

### 📨 ZBS Template Message

**ZBS (Zalo Business Solutions)** là giải pháp gửi tin nhắn thông báo từ Zalo OA tới người dùng đã được Zalo phê duyệt. Các loại tin nhắn bao gồm:

* • Thông báo giao dịch
* • Yêu cầu thanh toán
* • Tin mã OTP
* • Nhắc lịch thanh toán
* • Chăm sóc khách hàng
* • Đánh giá dịch vụ

📌 Tài liệu này hướng dẫn chi tiết **quy trình tạo Template ZBS trên hệ thống CRM TriAnh**.

\>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)

#### 📨 ZBS Template Message

**ZBS (Zalo Business Solutions)** dùng để gửi tin nhắn qua Zalo và đã được Zalo phê duyệt tới người dùng bao gồm những tin :

* Thông báo giao dịch
* Yêu cầu thanh toán
* Tin OTP
* Nhắc thanh toán
* Chăm sóc khách hàng
* Đánh giá dịch vụ

📌 Tài liệu này tập trung vào **hướng dẫn tạo Template ZBS trên CRM TriAnh**.

***

#### I. Tổng quan

Template ZBS là thành phần quan trọng trong giao tiếp khách hàng, yêu cầu nội dung phải tuân thủ quy định và được **Zalo kiểm duyệt** trước khi gửi.

**1. Lịch sử cập nhật**

| Ngày       | Người Cập Nhật | Version | Mô tả                       |
| ---------- | -------------- | ------- | --------------------------- |
| 27/01/2026 | Lý Anh Khoa    | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |

***

#### II. Các bước thực hiện

**1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)**

**🔹 Bước 1: Truy cập menu**

Tại giao diện CRM, click vào icon **Mẫu Email, SMS, ZNS** để vào giao diện quản lý.

![](<../.gitbook/assets/vao-email-template (1).png>)

Hình 1: Vị trí menu Mẫu Email, SMS, ZNS

**🔹 Bước 2: Khởi tạo**

1. Click vào biểu tượng **Dấu +**.
2. Nhấn nút **Tạo bản mẫu Zalo ZBS** để khởi tạo template .
3. ![](../.gitbook/assets/khoi-tao-template.png)
4. Hình 2: Khởi tạo template

**🔹 Bước 3: Thiết lập nội dung**

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
* Hình 5: Nhập các trường còn lại theo lưu ý =======

#### 🔹 Bước 1: Truy cập menu quản lý

Tại giao diện chính của CRM, tìm và nhấn vào icon **Mẫu Email, SMS, ZNS**.

![](<../.gitbook/assets/vao-email-template (2).png>)

_Hình 1: Truy cập menu Mẫu Email, SMS, ZNS_

#### 🔹 Bước 2: Khởi tạo bản mẫu

1. Chọn biểu tượng **Dấu +** tại góc giao diện
2. Nhấn chọn dòng **Tạo bản mẫu Zalo ZBS**

![](<../.gitbook/assets/khoi-tao-template (1).png>)

_Hình 2: Thao tác khởi tạo template mới_

#### 🔹 Bước 3: Thiết lập nội dung chi tiết

**📌 3.1. Thông tin cơ bản**

* **Tên mẫu ZBS:** Đặt tên gợi nhớ để quản lý nội bộ
* **Nguồn liên hệ:** Chọn đúng Zalo OA đang hoạt động
* **Loại ZBS:** Chọn **Mẫu Tùy Chỉnh**
* **Mục đích:** Lựa chọn mục đích phù hợp (Giao dịch, Thông báo...)

![](<../.gitbook/assets/thong-tin-co-ban (1).png>)

_Hình 3: Thiết lập các trường thông tin cơ bản_

***

**🖼 3.2. Nội dung hiển thị & Tham số**

* **Logo:** Sử dụng ảnh kích thước **400x96 px**, yêu cầu **xóa background** trước khi upload
* **Tiêu đề & Văn bản:** Bắt buộc nhập đầy đủ. Nếu sử dụng biến động, đặt tên biến trong dấu `{ten_bien}`
* **Phần Bảng:** Định nghĩa "Tiêu đề" (nhãn) và "Nội dung" (giá trị hoặc biến trong `{}`)
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`** tại mục này
* **Ghi chú kiểm duyệt:** Giải thích ngắn gọn mục đích gửi tin để Zalo duyệt nhanh hơn

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac (1).png>)

_Hình 4: Thiết lập hình ảnh và nội dung tin nhắn_

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac-2 (1).png>)

_Hình 5: Hoàn thiện tham số và ghi chú kiểm duyệt_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để gửi yêu cầu phê duyệt lên hệ thống Zalo.

\>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)

👉 Kiểm tra lại và nhấn nút **Tạo** để đẩy lên Zalo.

***

**2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)**

Mẫu tin nhắn này yêu cầu tuân thủ nghiêm ngặt các quy định về tài chính của Zalo:

**🔹 Cấu hình thanh toán**

Tại Bước 3, chọn **Loại ZBS: Yêu cầu thanh toán**.

**⚠️ Quy định về Tài khoản ngân hàng:**

* Tài khoản phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA.
* **Trường hợp dùng tài khoản khác** (Cá nhân/DN khác): Phải có văn bản/hợp đồng ủy quyền thu hộ. Cung cấp minh chứng qua mục _Ghi chú_ hoặc qua biểu mẫu: [https://go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

**📌 Hoàn tất:**

* Kiểm tra trạng thái tại màn hình danh sách: **Được duyệt** hoặc **Từ chối**.
* **Lưu ý:** Nếu bị từ chối, hệ thống yêu cầu tạo lại template mới thay vì chỉnh sửa bản cũ.

## [← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)

#### 🔹 Đặc điểm riêng của Mẫu Thanh toán

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Yêu cầu thanh toán**.

**⚠️ Quy định về Tài khoản ngân hàng**

* **Tính chính chủ:** Tài khoản nhận tiền phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA đó.
* **Trường hợp ủy quyền:** Nếu dùng tài khoản bên thứ 3 (cá nhân/DN khác), phải cung cấp hợp đồng/văn bản ủy quyền thu hộ qua mục _Ghi chú_ hoặc biểu mẫu hỗ trợ: [go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

**📌 Theo dõi trạng thái**

* Sau khi tạo, theo dõi cột **Trạng thái** trong danh sách:
  * ● **Được duyệt:** Có thể bắt đầu sử dụng để gửi tin.
  * ● **Từ chối:** Xem lý do, chỉnh sửa và tạo lại template mới.

[← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)>>>>>>> a22c275 (cap nhat noi dung ZBS lan thu 7)
