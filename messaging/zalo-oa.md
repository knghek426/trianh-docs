---
description: Hướng dẫn chi tiết quy trình khởi tạo và quản lý Template ZBS trên hệ thống CRM TriAnh.
---

Zalo OA (Official Account) và ZNS (Zalo Notification Service) dùng để gửi tin nhắn đã được Zalo phê duyệt tới người dùng: thông báo giao dịch, OTP, nhắc thanh toán, chăm sóc khách hàng.

Tài liệu này tập trung vào **hướng dẫn tạo Template ZBS trên hệ thống CRM TriAnh**.

***

## Mục lục

* [Zalo OA & ZNS](zalo-oa.md#zalo-oa--zns)
  * [Mục lục](zalo-oa.md#mục-lục)
  * [Tổng quan](zalo-oa.md#tổng-quan)
  * [Lịch sử cập nhật](zalo-oa.md#lịch-sử-cập-nhật)
  * [Quy trình tạo template ZBS – Mẫu tuỳ chỉnh](zalo-oa.md#quy-trình-tạo-template-zbs--mẫu-tuỳ-chỉnh)
    * [Bước 1: Truy cập màn hình tạo template](zalo-oa.md#bước-1-truy-cập-màn-hình-tạo-template)
    * [Bước 2: Tạo template Zalo ZBS](zalo-oa.md#bước-2-tạo-template-zalo-zbs)
    * [Bước 3: Nhập thông tin template](zalo-oa.md#bước-3-nhập-thông-tin-template)
      * [Thông tin cơ bản](zalo-oa.md#thông-tin-cơ-bản)
      * [Nội dung hiển thị](zalo-oa.md#nội-dung-hiển-thị)
      * [Bảng dữ liệu](zalo-oa.md#bảng-dữ-liệu)

***

## Tổng quan

Template **ZBS (Zalo Business Service)** là mẫu tin nhắn Zalo được gửi từ Zalo OA của doanh nghiệp tới khách hàng, yêu cầu **kiểm duyệt trước** từ Zalo. Việc tạo và quản lý template ZBS được thực hiện trực tiếp trên **CRM TriAnh**.

Template ZBS được sử dụng cho:

* Thông báo giao dịch
* Nhắc thanh toán
* Xác nhận đơn hàng
* Thông báo dịch vụ

***

### Bước 1: Truy cập quản trị
Tại giao diện Dashboard CRM, bạn di chuyển theo lộ trình sau:
`Menu chính` > `Cấu hình` > **Mẫu Email, SMS, ZNS**

| Ngày       | Người cập nhật | Version | Mô tả                 |
| ---------- | -------------- | ------- | --------------------- |
| 27/01/2026 | Lý Anh Khoa    | Ver 1.0 | Bắt đầu soạn tài liệu |

***

## Quy trình tạo template ZBS – Mẫu tuỳ chỉnh

### Bước 1: Truy cập màn hình tạo template

Tại giao diện CRM, chọn:

**Mẫu Email, SMS, ZNS** → vào màn hình quản lý template.

![Truy cập màn hình Mẫu Email, SMS, ZNS](../.gitbook/assets/vao-email-template.jpg)

***

### Bước 2: Tạo template Zalo ZBS

* Click vào biểu tượng **Zalo**
* Nhấn nút **Tạo mới** để khởi tạo template ZBS

***

### Bước 3: Nhập thông tin template

#### Thông tin cơ bản

* **Tên mẫu ZBS**: Tên nội bộ để quản lý
* **Nguồn liên hệ**: Chọn Zalo OA tương ứng
* **Loại ZBS**: Tuỳ chỉnh
* **Mục đích gửi ZBS**: Chọn đúng mục đích (giao dịch / thông báo)

#### Nội dung hiển thị

* **Logo**:
* Kích thước yêu cầu: **400 x 96 px**
* Ảnh cần được xử lý sẵn trước khi upload
* **Tiêu đề**:
* Có thể chứa biến
* Biến phải đặt trong dấu `{}`
* Ví dụ: `Xác nhận đơn hàng {order_id}`
* **Văn bản nội dung**:
* Tối thiểu 1 ô văn bản
* Nếu có biến, biến phải đặt trong `{}`

#### Bảng dữ liệu

[Previous](sms-brandname.md) • [Next](../api/overview.md)
