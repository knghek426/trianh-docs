# Hướng dẫn tạo Template CSKH và gửi chiến dịch A.C tại các đơn vị

*Hướng dẫn nãy dùng để các đơn vị sẽ tạo chiến dịch gửi tin thông báo cho Khách hàng (ví dụ sử dụng app SAWACO).*

## 1. Tạo Mẫu tin và Mẫu tin Gateway trên trang TCRM của đơn vị

### a) Tạo mẫu tin trong danh sách mẫu tin

- **Bước 1**: Vào **Quản lý** -> **Cài đặt** -> **Chức năng mới** -> **Danh sách mẫu tin**
![Quản lý Cài đặt](../assets/extracted_images/chien_dich_cskh/image1.png)
![Danh sách mẫu tin](../assets/extracted_images/chien_dich_cskh/image2.png)

- **Bước 2**: Click vào nút hình dấu **+** để tạo mẫu tin
![Tạo mẫu tin](../assets/extracted_images/chien_dich_cskh/image3.png)

- **Bước 3**: Gồm có các thông tin cần điền vào template như sau:
  - **Mã template**: Điền tên của template.
  - **VMG Template ID**: Điền id muốn đặt.
  - **Chủ đề**: Điền chủ đề cần gửi vào đây.
  - **Loại gửi**: CSKH App.
  - **Nguồn liên hệ**: Thông báo.
  - **Nội dung**: Điền thông tin nội dung của tin nhắn và gán biến vào nội dung dưới dạng ví dụ `{tenkh}`, `{sodanhbo}`.
  - **File**: Click vào để add file vào template.
  - **Tổ chức và Người dùng**: Chọn theo đơn vị.
![Điền thông tin Template 1](../assets/extracted_images/chien_dich_cskh/image4.png)
![Điền thông tin Template 2](../assets/extracted_images/chien_dich_cskh/image5.png)
![Điền thông tin Template 3](../assets/extracted_images/chien_dich_cskh/image6.png)
![Điền thông tin Template 4](../assets/extracted_images/chien_dich_cskh/image7.png)

  - **Chuẩn bị file excel như sau**:
![File excel mẫu 1](../assets/extracted_images/chien_dich_cskh/image8.png)
![File excel mẫu 2](../assets/extracted_images/chien_dich_cskh/image9.png)

- **Bước 5**: Cấu hình biến của file excel sau khi đã tạo xong template
  - Click vào tên template vừa mới tạo.
  - Bấm vào nút **cấu hình**.
  - Mặc định là các biến sẽ là ignore, nhấn vào để gán lại cho đúng biến.
![Cấu hình biến Excel 1](../assets/extracted_images/chien_dich_cskh/image10.png)
  - Sau đó nhấn **Lưu** để lưu lại.
![Lưu cấu hình biến Excel](../assets/extracted_images/chien_dich_cskh/image11.png)

### b) Tạo Mẫu tin Gateway để gửi chiến dịch

- **Bước 1**: Click vào **Quản lý** -> **Cài đặt** -> **Mẫu Email & SMS** -> **Mẫu tin Gateway**
![Mẫu tin Gateway](../assets/extracted_images/chien_dich_cskh/image12.png)

- **Bước 2**: Click vào nút tạo để tạo mẫu Gateway
![Tạo Gateway](../assets/extracted_images/chien_dich_cskh/image13.png)

- **Bước 3**: Điền các thông tin giống với lúc tạo mẫu tin ở danh sách mẫu tin. **Template CSKH** chọn template vừa mới tạo, **Người dùng**: Chọn người dùng cần thấy để gửi chiến dịch.
![Thông tin Gateway](../assets/extracted_images/chien_dich_cskh/image14.png)

- **Bước 4**: Nhấn nút **Lưu** để tạo mẫu tin Gateway thành công.
![Lưu Gateway](../assets/extracted_images/chien_dich_cskh/image15.png)

## 2. Tạo và gửi chiến dịch CSKH tại trang TCRM của đơn vị

- **Bước 1**: Click vào **Khách hàng** -> **Chiến dịch tự động** -> **Quản lý chiến dịch**.
![Quản lý chiến dịch](../assets/extracted_images/chien_dich_cskh/image16.png)

- **Bước 2**: Click vào nút dấu **+** để tạo chiến dịch
![Tạo chiến dịch](../assets/extracted_images/chien_dich_cskh/image17.png)

- **Bước 3**: Có các thông tin cần chọn như sau:
  - **Loại**: Chọn loại tin cần gửi (ở đây là **Gateway**).
![Cấu hình chiến dịch 1](../assets/extracted_images/chien_dich_cskh/image18.png)
  - **Biểu mẫu**: Chọn biểu mẫu cần gửi.
![Cấu hình chiến dịch 2](../assets/extracted_images/chien_dich_cskh/image19.png)
  - **Dowload template**: Tải File excel về nếu chưa có.
![Download template](../assets/extracted_images/chien_dich_cskh/image20.png)
![Upload file button](../assets/extracted_images/chien_dich_cskh/image21.png)
  - Click vào biểu tượng Upload để đẩy file lên.
![Cấu hình upload file](../assets/extracted_images/chien_dich_cskh/image22.png)
  - Nhấn nút **Lưu** để bắt đầu tạo chiến dịch.
![Lưu Chiến dịch](../assets/extracted_images/chien_dich_cskh/image23.png)

- **Bước 4**: Sau khi lưu xong, nhấn vào nút “play” để bắt đầu gửi chiến dịch.
![Nút Play](../assets/extracted_images/chien_dich_cskh/image24.png)
![Gửi chiến dịch](#](../assets/extracted_images/chien_dich_cskh/image25.png)
