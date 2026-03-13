# Hướng dẫn gửi Đánh giá Cuộc gọi

Tính năng Đánh giá cuộc gọi cho phép Nhân viên (Agent) chủ động gửi tin nhắn khảo sát chất lượng dịch vụ đến tài khoản Zalo của Khách hàng ngay sau khi kết thúc cuộc gọi trên hệ thống tổng đài TCRM.

## Điều kiện tiên quyết

- [ ] Tài khoản người dùng được cấp quyền truy cập module **Call Center Info**.
- [ ] Hệ thống TCRM đã được tích hợp và kết nối thành công với Zalo OA của doanh nghiệp.

## Hướng dẫn thao tác

### Bước 1: Truy cập Lịch sử cuộc gọi

1. Đăng nhập vào trang quản trị TCRM theo đường dẫn: `<domain>.tcrm.vn`.
![Giao diện chọn tổng đài](../assets/extracted_images/danh_gia_cuoc_goi/image1.png)
2. Tại menu điều hướng bên trái màn hình, nhấp chọn **Call Center Info**.
3. Nhấp chọn mục **Lịch sử cuộc gọi** để tải danh sách các cuộc gọi tương tác với Khách hàng.
![Màn hình Chọn lịch sử cuộc gọi](../assets/extracted_images/danh_gia_cuoc_goi/image2.png)

### Bước 2: Gửi yêu cầu đánh giá

1. Trong danh sách **Lịch sử cuộc gọi**, xác định vị trí cuộc gọi của Khách hàng cần khảo sát.
2. Tại cột **Đánh giá** tương ứng với cuộc gọi đó, nhấp vào biểu tượng **Mũi tên** để mở ô nhập văn bản.
![Nút mở gửi đánh giá](../assets/extracted_images/danh_gia_cuoc_goi/image3.png)
3. Nhập nội dung thông điệp muốn nhắn gửi cho Khách hàng vào ô trống.
4. Nhấp nút **Gửi**.
![Ô Nhập Text Gửi đánh giá](../assets/extracted_images/danh_gia_cuoc_goi/image4.png)

{% hint style="success" %}
Hệ thống sẽ tự động gửi thông báo chứa nội dung đánh giá trực tiếp đến Zalo của Khách hàng. Khách hàng có thể thao tác chọn điểm số và gửi phản hồi ngay trên ứng dụng Zalo của họ.
{% endhint %}
![Giao diện tin nhắn phía Khách hàng Zalo](../assets/extracted_images/danh_gia_cuoc_goi/image5.png)
![Khách hàng phản hồi từ Zalo](../assets/extracted_images/danh_gia_cuoc_goi/image6.png)

## Hướng dẫn theo dõi Kết quả đánh giá

Sau khi Khách hàng thực hiện phản hồi trên Zalo, hệ thống sẽ tự động ghi nhận lại kết quả. Quản trị viên và Agent có thể tra cứu theo 2 cách sau:

**Cách 1: Xem tra cứu nhanh (Agent)**

Kết quả đánh giá chi tiết của Khách hàng sẽ được cập nhật và hiển thị trực tiếp tại cột **Đánh giá** ngay trên màn hình **Lịch sử cuộc gọi**.
![Màn hình hiển thị kết quả đánh giá](../assets/extracted_images/danh_gia_cuoc_goi/image8.png)

**Cách 2: Xem thống kê tổng hợp (Supervisor/Admin)**

1. Tại thanh menu chính, nhấp chọn **Báo cáo**.
2. Nhấp chọn mục **Báo cáo chiến dịch**.
3. Chọn tiếp **Báo cáo chiến dịch đánh giá từ Zalo**.
4. Màn hình phân tích sẽ hiển thị toàn bộ danh sách khách hàng đã đánh giá và thống kê tỷ lệ hài lòng.
![Màn hình Báo cáo chiến dịch](../assets/extracted_images/danh_gia_cuoc_goi/image7.png)
{% hint style="info" %}
Tính năng Báo cáo chiến dịch giúp người Quản lý (Supervisor) dễ dàng đo lường chất lượng phục vụ của từng Agent theo khoảng thời gian thực.
{% endhint %}
