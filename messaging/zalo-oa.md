# ZBS Template

Version 1.0 - Internal Document - Tri Anh Solutions Corp.

## CHƯƠNG I. TỔNG QUAN

### 1. Lịch sử cập nhật

| Ngày       | Người Cập Nhật | Version | Mô tả   |
| ---------- | -------------- | ------- | ------- |
| 27/01/2026 | Lý Anh Khoa    | Ver1.0  | Bắt đầu |

## CHƯƠNG II. CÁC BƯỚC THỰC HIỆN

Hướng dẫn cấu hình template tạo ZBS trên CRM

### 1. Quy trình tạo template ZBS ( Mẫu Tùy Chỉnh )

* **Bước 1**: Click vào hình ![Icon ZNS](<../.gitbook/assets/image1 (5).png>) => Mẫu Email, SMS, ZNS để vào giao diện tạo template. ![Giao diện Mẫu SMS Email ZNS](<../.gitbook/assets/image2 (5).png>)
* **Bước 2**: Click vào hình sau đó click vào nút ![Icon Thêm](<../.gitbook/assets/image3 (3).png>) để tạo bản mẫu Zalo ZBS. ![Tạo bản mẫu Zalo ZBS](<../.gitbook/assets/image4 (2).png>)
* **Bước 3**: Điền các thông tin cần thiết như:
  * Điền Tên mẫu ZBS.
  * Chọn Nguồn liên hệ là Zalo OA của mình.
  * Chọn loại ZBS.
  * Chọn mục đích gửi ZBS. ![Cấu hình thông tin 1](<../.gitbook/assets/image5 (3).png>)
  * Chọn file logo ảnh ( Xử lý ảnh bên ngoài theo kích thước 400x96 trước khi đưa ảnh lên ).
  * Nhập tiêu đề ( Nếu tiêu đề có biến, biến phải để trong dấu `{}` ).
  * Nhập văn bản ( Nếu tiêu đề có biến, biến phải để trong dấu `{}` và nhập tối thiểu 1 ô văn bản).
  * Ở phần Bảng, nhập “Tiêu đề” là tên của biến và “Nội dung” là tên biến ( Biến phải để trong dấu `{}` ). Có thể click vào hình dấu ![Icon thêm hàng](<../.gitbook/assets/image8 (1).png>) để thêm hàng mới. ![Cấu hình thông tin 2](<../.gitbook/assets/image6 (3).png>)
  * Nút thao tác ( không bắt buộc ).
  * Nhập Tham số ( không được bỏ ngoặc `{}` ở phần này ).
  * Ghi chú cho kiểm duyệt có thể điền nội dung bất kì. Ví dụ: Template này dùng để giao dịch.
  * Mã tracking là mã tự sinh. ![Cấu hình thông tin 3](<../.gitbook/assets/image7 (3).png>)
  * Kiểm tra lại một lượt nữa và nhấn nút ![Icon Lưu](<../.gitbook/assets/image10 (1).png>) để tạo template và đẩy lên Zalo.

### 2. Quy trình tạo template ZBS ( Mẫu Yêu cầu thanh toán)

* **Bước 1**: Click vào hình ![Icon ZNS](<../.gitbook/assets/image1 (5).png>) => Mẫu Email, SMS, ZNS để vào giao diện tạo template.
* **Bước 2**: Click vào hình sau đó click vào nút ![Icon Thêm](<../.gitbook/assets/image3 (3).png>) để tạo bản mẫu Zalo ZBS.
* **Bước 3**: Click chọn Loại ZBS Yêu cầu thanh toán => Thêm hình ảnh logo, tiêu đề văn bản như Mẫu Tùy Chỉnh.
  * Cập nhật thông tin thanh toán Zalo OA.

{% hint style="warning" %}
**Lưu ý**: Tài khoản ngân hàng phải đứng tên chính doanh nghiệp sở hữu Zalo OA đó. Trường hợp doanh nghiệp sử dụng số tài khoản của doanh nghiệp khác hoặc sử dụng số tài khoản cá nhân khác (không phải chủ sở hữu DN/người đại diện pháp lý của doanh nghiệp) - vui lòng cung cấp được văn bản/hợp đồng thể hiện doanh nghiệp đã ủy quyền thu hộ (cung cấp qua mục ghi chú hoặc qua biểu mẫu: https://go.zalo.me/zbs-support để được hỗ trợ).
{% endhint %}

![Cấu hình thanh toán OA](<../.gitbook/assets/image9 (2).png>)

* Ở phần Bảng, nhập “Tiêu đề” là tên của biến và “Nội dung” là biến ( Nếu có biến, biến phải để trong dấu `{}` ). Có thể click vào hình dấu ![Icon Thêm hàng](<../.gitbook/assets/image8 (1).png>) để thêm hàng mới.
* Nút thao tác ( không bắt buộc ).
* Nhập Tham số ( không bỏ ngoặc `{}` ở phần này ).
* Ghi chú cho kiểm duyệt có thể điền nội dung bất kì. Ví dụ: Template này dùng để giao dịch.
* Mã tracking là mã tự sinh.
* Kiểm tra lại một lượt nữa và nhấn nút ![Icon Lưu](<../.gitbook/assets/image10 (1).png>) để tạo template và đẩy lên Zalo.
* Màn hình giao diện template được duyệt và từ chối như sau: ![Giao diện danh sách duyệt](<../.gitbook/assets/image11 (3).png>) ![Giao diện danh sách từ chối](<../.gitbook/assets/image12 (3).png>)

{% hint style="danger" %}
- Lưu ý: Nếu template bị từ chối, vui lòng tạo lại template khác.
{% endhint %}

!\[Chi tiết mẫu từ chối]\(../assets/extracted\_images/zbs\_crm/image13.png) !\[Tạo lại template]\(../assets/extracted\_images/zbs\_crm/image14.png)
