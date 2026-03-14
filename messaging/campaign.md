# Chiến dịch Tự động (Gateway)

_Hướng dẫn nãy dùng để các đơn vị sẽ tạo chiến dịch gửi tin thông báo cho Khách hàng (ví dụ sử dụng app SAWACO)._

## 1. Tạo Mẫu tin và Mẫu tin Gateway trên trang TCRM của đơn vị

### a) Tạo mẫu tin trong danh sách mẫu tin

* **Bước 1**: Vào **Quản lý** -> **Cài đặt** -> **Chức năng mới** -> **Danh sách mẫu tin** ![Quản lý Cài đặt](<../.gitbook/assets/image1 (3).png>) ![Danh sách mẫu tin](<../.gitbook/assets/image2 (3).png>)
* **Bước 2**: Click vào nút hình dấu **+** để tạo mẫu tin ![Tạo mẫu tin](<../.gitbook/assets/image3 (2).png>)
* **Bước 3**: Gồm có các thông tin cần điền vào template như sau:
  * **Mã template**: Điền tên của template.
  * **VMG Template ID**: Điền id muốn đặt.
  * **Chủ đề**: Điền chủ đề cần gửi vào đây.
  * **Loại gửi**: CSKH App.
  * **Nguồn liên hệ**: Thông báo.
  * **Nội dung**: Điền thông tin nội dung của tin nhắn và gán biến vào nội dung dưới dạng ví dụ `{tenkh}`, `{sodanhbo}`.
  * **File**: Click vào để add file vào template.
  * **Tổ chức và Người dùng**: Chọn theo đơn vị. ![Điền thông tin Template 1](<../.gitbook/assets/image4 (4).png>) ![Điền thông tin Template 2](<../.gitbook/assets/image5 (5).png>) ![Điền thông tin Template 3](<../.gitbook/assets/image6 (4).png>) ![Điền thông tin Template 4](<../.gitbook/assets/image7 (4).png>)
  * **Chuẩn bị file excel như sau**: ![File excel mẫu 1](<../.gitbook/assets/image8 (3).png>) ![File excel mẫu 2](<../.gitbook/assets/image9 (1).png>)
* **Bước 5**: Cấu hình biến của file excel sau khi đã tạo xong template
  * Click vào tên template vừa mới tạo.
  * Bấm vào nút **cấu hình**.
  * Mặc định là các biến sẽ là ignore, nhấn vào để gán lại cho đúng biến. ![Cấu hình biến Excel 1](<../.gitbook/assets/image10 (2).png>)
  * Sau đó nhấn **Lưu** để lưu lại. ![Lưu cấu hình biến Excel](<../.gitbook/assets/image11 (2).png>)

### b) Tạo Mẫu tin Gateway để gửi chiến dịch

* **Bước 1**: Click vào **Quản lý** -> **Cài đặt** -> **Mẫu Email & SMS** -> **Mẫu tin Gateway** ![Mẫu tin Gateway](<../.gitbook/assets/image12 (2).png>)
* **Bước 2**: Click vào nút tạo để tạo mẫu Gateway ![Tạo Gateway](<../.gitbook/assets/image13 (2).png>)
* **Bước 3**: Điền các thông tin giống với lúc tạo mẫu tin ở danh sách mẫu tin. **Template CSKH** chọn template vừa mới tạo, **Người dùng**: Chọn người dùng cần thấy để gửi chiến dịch. ![Thông tin Gateway](<../.gitbook/assets/image14 (2).png>)
* **Bước 4**: Nhấn nút **Lưu** để tạo mẫu tin Gateway thành công. ![Lưu Gateway](<../.gitbook/assets/image15 (1).png>)

## 2. Tạo và gửi chiến dịch CSKH tại trang TCRM của đơn vị

* **Bước 1**: Click vào **Khách hàng** -> **Chiến dịch tự động** -> **Quản lý chiến dịch**. ![Quản lý chiến dịch](<../.gitbook/assets/image16 (1).png>)
* **Bước 2**: Click vào nút dấu **+** để tạo chiến dịch ![Tạo chiến dịch](<../.gitbook/assets/image17 (1).png>)
* **Bước 3**: Có các thông tin cần chọn như sau:
  * **Loại**: Chọn loại tin cần gửi (ở đây là **Gateway**). ![Cấu hình chiến dịch 1](<../.gitbook/assets/image18 (1).png>)
  * **Biểu mẫu**: Chọn biểu mẫu cần gửi. ![Cấu hình chiến dịch 2](../.gitbook/assets/image19.png)
  * **Dowload template**: Tải File excel về nếu chưa có. ![Download template](../.gitbook/assets/image20.png) ![Upload file button](../.gitbook/assets/image21.png)
  * Click vào biểu tượng Upload để đẩy file lên. ![Cấu hình upload file](<../.gitbook/assets/image22 (1).png>)
  * Nhấn nút **Lưu** để bắt đầu tạo chiến dịch. ![Lưu Chiến dịch](<../.gitbook/assets/image23 (1).png>)
* **Bước 4**: Sau khi lưu xong, nhấn vào nút “play” để bắt đầu gửi chiến dịch. ![Nút Play](<../.gitbook/assets/image24 (1).png>) !\[Gửi chiến dịch]\(#]\(../assets/extracted\_images/chien\_dich\_cskh/image25.png)
