# Hướng dẫn tạo template CSKH và gửi chiến dịch A.C tại các đơn vị

*Hướng dẫn này dùng để các đơn vị sẽ tạo chiến dịch gửi tin thông báo cho Khách hàng sử dụng app SAWACO.*

## 1. Tạo Mẫu tin và Mẫu tin Gateway trên trang TCRM của đơn vị

### a) Tạo mẫu tin trong danh sách mẫu tin

- **Bước 1**: Vào **Quản lý** -> **Cài đặt** -> **Chức năng mới** -> **Danh sách mẫu tin**
  ![Truy cập Danh sách mẫu tin](../assets/extracted_images/chien_dich_cskh/image1.png)

- **Bước 2**: Click vào nút hình dấu ![Icon Thêm](../assets/extracted_images/chien_dich_cskh/image2.png) để tạo mẫu tin
  ![Chọn nút Thêm mẫu tin](../assets/extracted_images/chien_dich_cskh/image3.png)

- **Bước 3**: Gồm có các thông tin cần điền vào template như sau:
  - **Mã template**: Điền tên của template.
  - **VMG Template ID**: Điền id muốn đặt.
  - **Chủ đề**: Điền chủ đề cần gửi vào đây.
  - **Loại gửi**: CSKH App.
  - **Nguồn liên hệ**: Thông báo.
  - **Nội dung**: Điền thông tin nội dung của tin nhắn và gán biến vào nội dung dưới dạng ví dụ `{tenkh}`, `{sodanhbo}`.
  - **File**: Click vào ![Icon Chọn Tệp](../assets/extracted_images/chien_dich_cskh/image4.png) để add file vào template.
  ![Điền các thông tin cơ bản](../assets/extracted_images/chien_dich_cskh/image5.png)

  - **Tổ chức và Người dùng**: Chọn theo đơn vị.
  ![Chọn Tổ chức và Người dùng](../assets/extracted_images/chien_dich_cskh/image6.png)

  - **Chuẩn bị file excel như sau**:
  ![File excel chứa các trường tùy biến](../assets/extracted_images/chien_dich_cskh/image7.png)

- **Bước 5**: Cấu hình biến của file excel sau khi đã tạo xong template
  - Click vào tên template vừa mới tạo.
    ![Template vừa tạo trong danh sách](../assets/extracted_images/chien_dich_cskh/image8.png)
  - Bấm vào nút cấu hình.
    ![Nút cấu hình](../assets/extracted_images/chien_dich_cskh/image9.png)
  - Mặc định là các biến sẽ là ignore, nhấn vào để gán lại cho đúng biến.
    ![Cấu hình biến Excel](../assets/extracted_images/chien_dich_cskh/image10.png)
  - Sau đó nhấn ![Icon Save Config](../assets/extracted_images/chien_dich_cskh/image11.png) để lưu lại.

### b) Tạo Mẫu tin Gateway để gửi chiến dịch

- **Bước 1**: Click vào **Quản lý** -> **Cài đặt** -> **Mẫu Email & SMS** -> **Mẫu tin Gateway**
  ![Truy cập Mẫu tin Gateway](../assets/extracted_images/chien_dich_cskh/image12.png)

- **Bước 2**: Click vào hình dấu ![Icon Thêm](../assets/extracted_images/chien_dich_cskh/image13.png) hoặc ![Nút tạo Gateway](../assets/extracted_images/chien_dich_cskh/image14.png) để thêm mới.

- **Bước 3**: Gồm những thông tin như ( Có thể tham khảo hình ở dưới):
  - **Tên mẫu tin**: Tên hiển thị bên ngoài
  - **Mẫu tin**: Lấy giá trị ở các mẫu tin có sẵn. (VD: template cskh mình đang tạo mẫu tin)
    ![Thông tin Gateway 1](../assets/extracted_images/chien_dich_cskh/image15.png)
  - Chọn các biến để mapping với mẫu tin cskh.
    ![Thông tin Gateway 2](../assets/extracted_images/chien_dich_cskh/image16.png)
  - Chọn gửi từ CSKH App.
    ![Thông tin Gateway 3](../assets/extracted_images/chien_dich_cskh/image17.png)

- **Bước 4**: Sau khi thiết lập xong cấu hình gửi tin thì lưu cấu hình lại.
  ![Lưu Mẫu tin Gateway](../assets/extracted_images/chien_dich_cskh/image18.png)

## 2. Tạo và gửi chiến dịch CSKH tại trang TCRM của đơn vị

- **Bước 1**: Click vào **Khách hàng** -> **Chiến dịch tự động** -> **Quản lý chiến dịch**.
  ![Truy cập Quản lý chiến dịch](../assets/extracted_images/chien_dich_cskh/image19.png)

- **Bước 2**: Click vào nút dấu ![Icon Thêm chiến dịch](../assets/extracted_images/chien_dich_cskh/image20.png) để tạo chiến dịch

- **Bước 3**: Có các thông tin cần chọn như sau:
  - **Loại**: Chọn loại tin cần gửi ( ở đây là Gateway ).
  - **Biểu mẫu**: Chọn biểu mẫu cần gửi.
  - **Dowload template**: Tải File excel về nếu chưa có.
  - ![Icon Upload](../assets/extracted_images/chien_dich_cskh/image22.png) : Click vào đây để đẩy file lên.
  - Nhấn nút ![Icon Lưu](../assets/extracted_images/chien_dich_cskh/image23.png) để bắt đầu tạo chiến dịch.
    ![Cấu hình tạo chiến dịch](../assets/extracted_images/chien_dich_cskh/image21.png)

- **Bước 4**: Sau khi lưu xong, nhấn vào nút “play” để bắt đầu gửi chiến dịch.
  ![Nút Gửi chiến dịch](../assets/extracted_images/chien_dich_cskh/image24.png)
  ![Gửi chiến dịch trực tiếp](../assets/extracted_images/chien_dich_cskh/image25.png)
