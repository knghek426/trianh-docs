# Hướng dẫn tạo template ZBS trên CRM

Version 1.0 - Internal Document - Tri Anh Solutions Corp.

## CHƯƠNG I. TỔNG QUAN

### 1. Lịch sử cập nhật

| Ngày | Người Cập Nhật | Version | Mô tả |
| :--- | :--- | :--- | :--- |
| 27/01/2026 | Lý Anh Khoa | Ver1.0 | Bắt đầu |

## CHƯƠNG II. CÁC BƯỚC THỰC HIỆN

Hướng dẫn cấu hình template tạo ZBS trên CRM

### 1. Quy trình tạo template ZBS ( Mẫu Tùy Chỉnh )

- **Bước 1**: Click vào hình ![Icon Cài đặt](../assets/extracted_images/zbs_crm/image1.png) => Mẫu Email, SMS, ZNS để vào giao diện tạo template.
  ![Giao diện Mẫu SMS Email ZNS](../assets/extracted_images/zbs_crm/image2.png)

- **Bước 2**: Click vào hình ![Icon Mở rộng](../assets/extracted_images/zbs_crm/image3.png) sau đó click vào nút ![Icon Thêm thẻ ZBS](../assets/extracted_images/zbs_crm/image4.png) để tạo bản mẫu Zalo ZBS.

- **Bước 3**: Điền các thông tin cần thiết như:
  - Điền Tên mẫu ZBS.
  - Chọn Nguồn liên hệ là Zalo OA của mình.
  - Chọn loại ZBS.
  - Chọn mục đích gửi ZBS.
  ![Khai báo nội dung ZBS](../assets/extracted_images/zbs_crm/image5.png)

  - Chọn file logo ảnh ( Xử lý ảnh bên ngoài theo kích thước 400x96 trước khi đưa ảnh lên ).
  - Nhập tiêu đề ( Nếu tiêu đề có biến, biến phải để trong dấu `{}` ).
  - Nhập văn bản ( Nếu tiêu đề có biến, biến phải để trong dấu `{}` và nhập tối thiểu 1 ô văn bản).
  ![Khai báo Hình ảnh, Tiêu đề, Văn bản](../assets/extracted_images/zbs_crm/image6.png)

  - Ở phần Bảng, nhập “Tiêu đề” là tên của biến và “Nội dung” là tên biến ( Biến phải để trong dấu `{}` ). Có thể click vào hình dấu ![Icon thêm hàng](../assets/extracted_images/zbs_crm/image8.png) để thêm hàng mới.
  - Nút thao tác ( không bắt buộc ).
  - Nhập Tham số ( không được bỏ ngoặc `{}` ở phần này ).
  - Ghi chú cho kiểm duyệt có thể điền nội dung bất kì. Ví dụ: Template này dùng để giao dịch.
  - Mã tracking là mã tự sinh.
  ![Khai báo Bảng và Tham số](../assets/extracted_images/zbs_crm/image9.png)

  - Kiểm tra lại một lượt nữa và nhấn nút ![Icon Tạo](../assets/extracted_images/zbs_crm/image10.png) để tạo template và đẩy lên Zalo.

### 2. Quy trình tạo template ZBS ( Mẫu Yêu cầu thanh toán)

- **Bước 1**: Click vào hình ![Icon Cài đặt](../assets/extracted_images/zbs_crm/image1.png) => Mẫu Email, SMS, ZNS để vào giao diện tạo template.
- **Bước 2**: Click vào hình ![Icon Mở rộng](../assets/extracted_images/zbs_crm/image3.png) sau đó click vào nút ![Icon Thêm thẻ ZBS](../assets/extracted_images/zbs_crm/image4.png) để tạo bản mẫu Zalo ZBS.
- **Bước 3**: Click chọn Loại ZBS Yêu cầu thanh toán => Thêm hình ảnh logo, tiêu đề văn bản như Mẫu Tùy Chỉnh.
  ![Chọn Loại ZBS Thanh toán](../assets/extracted_images/zbs_crm/image11.png)

  - Cập nhật thông tin thanh toán Zalo OA.

  > **Lưu ý**: Tài khoản ngân hàng phải đứng tên chính doanh nghiệp sở hữu Zalo OA đó. Trường hợp doanh nghiệp sử dụng số tài khoản của doanh nghiệp khác hoặc sử dụng số tài khoản cá nhân khác (không phải chủ sở hữu DN/người đại diện pháp lý của doanh nghiệp) - vui lòng cung cấp được văn bản/hợp đồng thể hiện doanh nghiệp đã ủy quyền thu hộ (cung cấp qua mục ghi chú hoặc qua biểu mẫu: https://go.zalo.me/zbs-support để được hỗ trợ).

  ![Điền Thông tin thanh toán](../assets/extracted_images/zbs_crm/image12.png)

  - Ở phần Bảng, nhập “Tiêu đề” là tên của biến và “Nội dung” là biến ( Nếu có biến, biến phải để trong dấu `{}` ). Có thể click vào hình dấu ![Icon thêm hàng](../assets/extracted_images/zbs_crm/image8.png) để thêm hàng mới.
  - Nút thao tác ( không bắt buộc ).
  - Nhập Tham số ( không bỏ ngoặc `{}` ở phần này ).
  - Ghi chú cho kiểm duyệt có thể điền nội dung bất kì. Ví dụ: Template này dùng để giao dịch.
  - Mã tracking là mã tự sinh.
  ![Điền Bảng, Tham số mẫu Thanh toán](../assets/extracted_images/zbs_crm/image13.png)

  - Kiểm tra lại một lượt nữa và nhấn nút ![Icon Tạo](../assets/extracted_images/zbs_crm/image10.png) để tạo template và đẩy lên Zalo.

- Màn hình giao diện template được duyệt và từ chối như sau:
  ![Trạng thái template](../assets/extracted_images/zbs_crm/image14.png)

> **Lưu ý**: Nếu template bị từ chối, vui lòng tạo lại template khác.
