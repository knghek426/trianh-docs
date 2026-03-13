# ZBS Template

### 📨 ZBS Template Message

**ZBS (Zalo Business Solutions)** là giải pháp gửi tin nhắn thông báo từ Zalo OA tới người dùng đã được Zalo phê duyệt. Các loại tin nhắn bao gồm:

* Thông báo giao dịch
* Yêu cầu thanh toán
* Tin mã OTP
* Nhắc lịch thanh toán
* Chăm sóc khách hàng
* Đánh giá dịch vụ

📌 Tài liệu này hướng dẫn chi tiết **quy trình tạo Template ZBS trên hệ thống CRM TriAnh**.

***

### I. Tổng quan

**TriAnh Solutions** là công ty công nghệ với hơn 16 năm kinh nghiệm, chuyên cung cấp các giải pháp chuyển đổi số cho doanh nghiệp bao gồm: CRM, OmniChannel Contact Center, SMS Brandname, ZNS/ZBS và tích hợp API. Hệ thống CRM của TriAnh tích hợp sẵn tính năng tạo và quản lý **Template ZBS**, giúp doanh nghiệp chủ động gửi thông báo đến khách hàng một cách nhanh chóng và đúng quy định.

#### 1. Lịch sử cập nhật

| Ngày       | Người Cập Nhật | Version | Mô tả                       |
| ---------- | -------------- | ------- | --------------------------- |
| 27/01/2026 | Lý Anh Khoa    | Ver 1.0 | Khởi tạo tài liệu hướng dẫn |

#### 2. Mục lục

| STT | Nội dung |
| :-: | :--- |
| 1 | [Quy trình tạo template ZBS — Mẫu Tùy Chỉnh](#1-quy-trinh-tao-template-zbs-mau-tuy-chinh) |
| 2 | [Quy trình tạo template ZBS — Mẫu Yêu cầu thanh toán](#2-quy-trinh-tao-template-zbs-mau-yeu-cau-thanh-toan) |
| 3 | [Quy trình tạo template ZBS — Mẫu Đánh giá dịch vụ](#3-quy-trinh-tao-template-zbs-mau-danh-gia-dich-vu) |
| 4 | [Quy trình tạo template ZBS — Mẫu Voucher](#4-quy-trinh-tao-template-zbs-mau-voucher) |
| 5 | [Quy trình tạo template ZBS — Mẫu Xác thực](#5-quy-trinh-tao-template-zbs-mau-xac-thuc) |

***

### II. Các bước thực hiện

#### 1. Quy trình tạo template ZBS (Mẫu Tùy Chỉnh)

#### 🔹 Bước 1: Truy cập menu quản lý

Tại giao diện chính của CRM, tìm và nhấn vào icon **Mẫu Email, SMS, ZNS**.

![](<../.gitbook/assets/vao-email-template (4).png>)

Hình 1: Truy cập menu Mẫu Email, SMS, ZNS

***

#### 🔹 Bước 2: Khởi tạo bản mẫu

1. Chọn biểu tượng **Dấu +** tại góc giao diện.
2. Nhấn chọn dòng **Tạo bản mẫu Zalo ZBS**.

![](<../.gitbook/assets/khoi-tao-template (3).png>)

Hình 2: Thao tác khởi tạo template mới

***

#### 🔹 Bước 3: Thiết lập nội dung chi tiết

**Thông tin cơ bản**

* **Tên mẫu ZBS:** Đặt tên gợi nhớ để quản lý nội bộ.
* **Nguồn liên hệ:** Chọn đúng Zalo OA đang hoạt động.
* **Loại ZBS:** Chọn **Mẫu Tùy Chỉnh**.
* **Mục đích:** Lựa chọn mục đích phù hợp (Giao dịch, Thông báo...).

![](<../.gitbook/assets/thong-tin-co-ban (3).png>)

Hình 3: Thiết lập các trường thông tin cơ bản

**Nội dung hiển thị & Tham số**

* **Logo:** Sử dụng ảnh kích thước **400x96 px**, yêu cầu **xóa background** trước khi upload.
* **Tiêu đề & Văn bản:** Bắt buộc nhập đầy đủ. Nếu sử dụng biến động, đặt tên biến trong dấu `{ten_bien}`.
* **Phần Bảng:** Định nghĩa "Tiêu đề" (nhãn) và "Nội dung" (giá trị hoặc biến trong `{}`).
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`** tại mục này.
* **Ghi chú kiểm duyệt:** Giải thích ngắn gọn mục đích gửi tin để Zalo duyệt nhanh hơn.

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac (3).png>)

Hình 4: Thiết lập hình ảnh và nội dung tin nhắn

![](<../.gitbook/assets/dien-cac-truong-thong-tin-khac-2 (3).png>)

Hình 5: Hoàn thiện tham số và ghi chú kiểm duyệt

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất gửi yêu cầu cho Zalo.

***

#### 2. Quy trình tạo template ZBS (Mẫu Yêu cầu thanh toán)

Mẫu tin nhắn này yêu cầu tuân thủ nghiêm ngặt các quy định về tài chính của Zalo.

#### 🔹 Đặc điểm riêng của Mẫu Thanh toán

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Yêu cầu thanh toán**. Các bước còn lại thực hiện tương tự Mẫu Tùy Chỉnh.

**⚠️ Quy định về Tài khoản ngân hàng**

* **Tính chính chủ:** Tài khoản nhận tiền phải **đứng tên chính doanh nghiệp** sở hữu Zalo OA đó.
* **Trường hợp ủy quyền:** Nếu dùng tài khoản bên thứ 3 (cá nhân/DN khác), phải cung cấp hợp đồng/văn bản ủy quyền thu hộ qua mục _Ghi chú_ hoặc biểu mẫu hỗ trợ: [go.zalo.me/zbs-support](https://go.zalo.me/zbs-support).

_📸 \[Hình ảnh giao diện cập nhật thông tin thanh toán Zalo OA — sẽ bổ sung sau]_

**📌 Theo dõi trạng thái**

Sau khi tạo, theo dõi cột **Trạng thái** trong danh sách:

* ● **Được duyệt:** Có thể bắt đầu sử dụng để gửi tin.
* ● **Từ chối:** Xem lý do, chỉnh sửa và cập nhật lại template.

_📸 \[Hình ảnh màn hình trạng thái duyệt / từ chối — sẽ bổ sung sau]_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất gửi yêu cầu cho Zalo.

***

#### 3. Quy trình tạo template ZBS (Mẫu Đánh giá dịch vụ)

Mẫu này cho phép doanh nghiệp thu thập phản hồi từ khách hàng thông qua câu hỏi đánh giá chất lượng dịch vụ, hiển thị trực tiếp trên giao diện Zalo.

#### 🔹 Đặc điểm riêng của Mẫu Đánh giá

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Đánh giá dịch vụ**. Các bước còn lại thực hiện tương tự Mẫu Tùy Chỉnh.

**Phần câu hỏi đánh giá**

* Nhập **Câu hỏi đánh giá** (ví dụ: _Bạn đánh giá thế nào về dịch vụ của chúng tôi?_).
* Chọn **Loại đánh giá** phù hợp:
  * **Sao (1–5):** Khách hàng chọn từ 1 đến 5 sao — phổ biến nhất.
  * **Thang điểm số:** Khách hàng chọn điểm trong khoảng quy định.
  * **Lựa chọn văn bản:** Liệt kê các đáp án để khách hàng chọn một.
* Có thể thêm **câu hỏi phụ** (câu hỏi mở) để khách hàng nhập nhận xét tự do.

**Thông tin khác**

* **Phần Bảng:** Điền các trường thông tin liên quan. Biến đặt trong dấu `{}`.
* **Nút thao tác** (không bắt buộc): Có thể thêm nút _Gửi đánh giá_.
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`**.
* **Ghi chú kiểm duyệt:** Ví dụ: _Template dùng để thu thập đánh giá chất lượng dịch vụ sau giao dịch._
* **Mã tracking:** Mã tự sinh, không cần chỉnh sửa.

_📸 \[Hình ảnh giao diện nhập câu hỏi đánh giá — sẽ bổ sung sau]_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất gửi yêu cầu cho Zalo.

***

#### 4. Quy trình tạo template ZBS (Mẫu Voucher)

Mẫu này dùng để gửi mã ưu đãi, coupon hoặc voucher tới khách hàng thông qua Zalo OA.

#### 🔹 Đặc điểm riêng của Mẫu Voucher

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Voucher**. Các bước còn lại thực hiện tương tự Mẫu Tùy Chỉnh.

**Phần thông tin Voucher**

* **Phần Bảng:** Điền thông tin Voucher gồm: mã giảm giá (`{ma_voucher}`), mức giảm, hạn sử dụng (`{han_su_dung}`), điều kiện áp dụng. Biến đặt trong dấu `{}`.
* **Nút thao tác** (không bắt buộc): Có thể thêm nút _Dùng ngay_, _Xem chi tiết_.
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`**.
* **Ghi chú kiểm duyệt:** Ví dụ: _Template gửi voucher ưu đãi cho khách hàng thân thiết._
* **Mã tracking:** Mã tự sinh, không cần chỉnh sửa.

_📸 \[Hình ảnh giao diện thiết lập Mẫu Voucher — sẽ bổ sung sau]_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất gửi yêu cầu cho Zalo.

***

#### 5. Quy trình tạo template ZBS (Mẫu Xác thực)

Mẫu này dùng để gửi mã OTP hoặc liên kết xác thực danh tính người dùng qua Zalo OA.

#### 🔹 Đặc điểm riêng của Mẫu Xác thực

Tại **Bước 3**, mục **Loại ZBS** hãy chọn: **Xác thực**. Các bước còn lại thực hiện tương tự Mẫu Tùy Chỉnh.

**Phần thông tin Xác thực**

* **Tiêu đề & Văn bản:** Nhập nội dung thông báo. Biến động (mã OTP) đặt trong `{ten_bien}`. Bắt buộc ít nhất 1 ô văn bản.
* **Phần Bảng:** Điền mã xác thực (`{ma_otp}`) và thời gian hiệu lực (ví dụ: _5 phút_).
* **Nút thao tác** (không bắt buộc): Có thể thêm nút _Xác nhận_ hoặc _Xác thực ngay_.
* **Tham số:** Tuyệt đối **không xóa dấu ngoặc `{}`**.
* **Ghi chú kiểm duyệt:** Ví dụ: _Template gửi mã OTP xác thực tài khoản khách hàng._
* **Mã tracking:** Mã tự sinh, không cần chỉnh sửa.

_📸 \[Hình ảnh giao diện thiết lập Mẫu Xác thực — sẽ bổ sung sau]_

👉 Sau khi kiểm tra kỹ, nhấn nút **Tạo** để hoàn tất gửi yêu cầu cho Zalo.

***

[← SMS Brandname](sms-brandname.md) [Hướng dẫn API →](../api/overview.md)
