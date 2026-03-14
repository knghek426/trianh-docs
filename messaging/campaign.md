# Chiến dịch Tự động (Gateway)

_Hướng dẫn này dùng để các đơn vị sẽ tạo chiến dịch gửi tin thông báo cho Khách hàng sử dụng app SAWACO._

## 1. Tạo Mẫu tin và Mẫu tin Gateway trên trang TCRM của đơn vị

### a) Tạo mẫu tin trong danh sách mẫu tin

*   **Bước 1**: Vào **Quản lý** -> **Cài đặt** -> **Chức năng mới** -> **Danh sách mẫu tin**

    ![Truy cập Danh sách mẫu tin](<../.gitbook/assets/image1 (6).png>)
*   **Bước 2**: Click vào nút hình dấu ![Icon Thêm](<../.gitbook/assets/image2 (6).png>) để tạo mẫu tin

    ![Chọn nút Thêm mẫu tin](<../.gitbook/assets/image3 (5).png>)
* **Bước 3**: Gồm có các thông tin cần điền vào template như sau:
  * **Mã template**: Điền tên của template.
  * **VMG Template ID**: Điền id muốn đặt.
  * **Chủ đề**: Điền chủ đề cần gửi vào đây.
  * **Loại gửi**: CSKH App.
  * **Nguồn liên hệ**: Thông báo.
  * **Nội dung**: Điền thông tin nội dung của tin nhắn và gán biến vào nội dung dưới dạng ví dụ `{tenkh}`, `{sodanhbo}`.
  *   **File**: Click vào ![Icon Chọn Tệp](<../.gitbook/assets/image4 (5).png>) để add file vào template.

      ![Điền các thông tin cơ bản](<../.gitbook/assets/image5 (6).png>)
  *   **Tổ chức và Người dùng**: Chọn theo đơn vị.

      ![Chọn Tổ chức và Người dùng](<../.gitbook/assets/image6 (5).png>)
  *   **Chuẩn bị file excel như sau**:

      ![File excel chứa các trường tùy biến](<../.gitbook/assets/image7 (5).png>)
* **Bước 5**: Cấu hình biến của file excel sau khi đã tạo xong template
  *   Click vào tên template vừa mới tạo.

      ![Template vừa tạo trong danh sách](<../.gitbook/assets/image8 (4).png>)
  *   Bấm vào nút cấu hình.

      ![Nút cấu hình](<../.gitbook/assets/image9 (3).png>)
  *   Mặc định là các biến sẽ là ignore, nhấn vào để gán lại cho đúng biến.

      ![Cấu hình biến Excel](<../.gitbook/assets/image10 (3).png>)
  * Sau đó nhấn ![Icon Save Config](<../.gitbook/assets/image11 (4).png>) để lưu lại.

### b) Tạo Mẫu tin Gateway để gửi chiến dịch

*   **Bước 1**: Click vào **Quản lý** -> **Cài đặt** -> **Mẫu Email & SMS** -> **Mẫu tin Gateway**

    ![Truy cập Mẫu tin Gateway](<../.gitbook/assets/image12 (7).png>)
*   **Bước 2**: Click vào hình dấu ![Icon Thêm](<../.gitbook/assets/image13 (6).png>) để thêm mới mẫu Gateway.

    ![Danh sách Mẫu tin Gateway](<../.gitbook/assets/image14 (6).png>)
* **Bước 3**: Gồm những thông tin như ( Có thể tham khảo hình ở dưới):
  * **Tên mẫu tin**: Tên hiển thị bên ngoài
  *   **Mẫu tin**: Lấy giá trị ở các mẫu tin có sẵn. (VD: template cskh mình đang tạo mẫu tin)

      ![Thông tin Gateway 1](<../.gitbook/assets/image15 (4).png>)
  *   Chọn các biến để mapping với mẫu tin cskh.

      ![Thông tin Gateway 2](<../.gitbook/assets/image16 (4).png>)
  *   Chọn gửi từ CSKH App.

      ![Thông tin Gateway 3](<../.gitbook/assets/image17 (4).png>)
*   **Bước 4**: Sau khi thiết lập xong cấu hình gửi tin thì lưu cấu hình lại.

    ![Lưu Mẫu tin Gateway](<../.gitbook/assets/image18 (4).png>)

## 2. Tạo và gửi chiến dịch CSKH tại trang TCRM của đơn vị

*   **Bước 1**: Click vào **Khách hàng** -> **Chiến dịch tự động** -> **Quản lý chiến dịch**.

    ![Truy cập Quản lý chiến dịch](<../.gitbook/assets/image19 (3).png>)
* **Bước 2**: Click vào nút dấu ![Icon Thêm chiến dịch](<../.gitbook/assets/image20 (3).png>) để tạo chiến dịch
* **Bước 3**: Có các thông tin cần chọn như sau:
  * **Loại**: Chọn loại tin cần gửi ( ở đây là Gateway ).
  * **Biểu mẫu**: Chọn biểu mẫu cần gửi.
  * **Dowload template**: Tải File excel về nếu chưa có.
  * Sau đó Click vào File Import để đẩy file lên.
  *   Nhấn nút ![Icon Lưu](<../.gitbook/assets/image23 (4).png>) để bắt đầu tạo chiến dịch.

      ![Cấu hình tạo chiến dịch](<../.gitbook/assets/image21 (3).png>)
*   **Bước 4**: Sau khi lưu xong, nhấn vào nút “play” để bắt đầu gửi chiến dịch.

    ![Nút Gửi chiến dịch](<../.gitbook/assets/image24 (4).png>)

    ![Gửi chiến dịch trực tiếp](<../.gitbook/assets/image25 (3).png>)
