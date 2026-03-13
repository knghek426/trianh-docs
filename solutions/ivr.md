# Dịch vụ IVR

### 🎙️ Dịch vụ IVR — Tương tác thoại tự động

**IVR (Interactive Voice Response)** là hệ thống trả lời điện thoại tự động, cho phép xây dựng kịch bản menu thoại tương tác: phát lời thoại, nhận phím bấm (DTMF), phân luồng cuộc gọi theo bộ phận/thời gian, thu thập dữ liệu và lưu thẳng vào CRM.

📞 Hotline tư vấn: **1900 27 27 77**

***

### I. Tổng quan

**IVR** là hệ thống điện toán hóa giúp doanh nghiệp hướng dẫn người gọi đến đúng bộ phận hỗ trợ thông qua danh sách lựa chọn bằng giọng nói hoặc bấm phím. TriAnh Solutions cung cấp hệ thống IVR có **tính mở cao**, sẵn sàng tùy biến theo những yêu cầu đặc thù nhất từ doanh nghiệp.

#### Lịch sử cập nhật

| Ngày       | Người Cập Nhật | Version | Mô tả             |
| ---------- | -------------- | ------- | ----------------- |
| 13/03/2026 | TriAnh Docs    | Ver 1.0 | Khởi tạo tài liệu |

***

### II. Tính năng

| Tính năng                    | Mô tả                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| 🔊 **Play Audio / TTS**      | Phát file âm thanh (MP3/WAV) hoặc dùng Text-to-Speech để đọc nội dung động         |
| ⌨️ **Nhận phím bấm (DTMF)**  | Thu thập lựa chọn của người gọi thông qua bàn phím điện thoại                      |
| 🔀 **Routing thông minh**    | Chuyển cuộc gọi theo giờ làm việc, theo skill agent, theo bộ phận, theo số gọi đến |
| 📬 **Voicemail**             | Cho phép khách để lại tin nhắn thoại khi ngoài giờ hoặc không có agent             |
| 🗄️ **Lưu dữ liệu vào CRM**  | Dữ liệu input (DTMF) được ghi thẳng vào TCRM qua Webhook — tự động hóa hoàn toàn   |
| ⏰ **Routing theo thời gian** | Tự động chuyển sang kịch bản khác ngoài giờ hành chính hoặc ngày lễ                |

***

### III. Ví dụ kịch bản IVR

```
📞 Khách hàng gọi vào → IVR chào và phát menu:
  "Xin chào! Quý khách vui lòng bấm phím:
  [1] Tư vấn bán hàng
  [2] Hỗ trợ kỹ thuật
  [3] Kế toán & Thanh toán
  [0] Gặp tổng đài viên"

→ Bấm [1]: Chuyển tới nhóm Sales (skill-based routing)
→ Bấm [2]: Chuyển tới nhóm Support
→ Bấm [3]: Chuyển tới nhóm Kế toán
→ Bấm [0]: Xếp hàng chờ agent rảnh gần nhất
→ Ngoài giờ: Tự động kích hoạt kịch bản ngoài giờ → Voicemail
```

***

### IV. Ứng dụng thực tiễn

TriAnh Solutions đang triển khai IVR thành công trong các lĩnh vực:

* 🎓 **Giáo dục** — Thông báo lịch thi, điểm số, nhắc học phí
* 🏥 **Y tế** — Đặt lịch khám, nhắc lịch tái khám, tra cứu kết quả
* 🔮 **Tư vấn chuyên biệt** — Phong thủy, bóng đá, thông tin tổng hợp
* 🏢 **Doanh nghiệp** — CSKH, xác nhận đơn hàng, nhắc thanh toán, OTP thoại

_📸 \[Hình ảnh giao diện thiết lập kịch bản IVR — sẽ bổ sung sau]_

***

### V. Hướng dẫn thiết lập nhanh

1. **Tạo Node IVR mới** trên dashboard CCMS → đặt tên kịch bản.
2. **Thêm các bước (Step):**
   * `PlayAudio` → chọn file audio hoặc nhập nội dung TTS
   * `Choice` → cấu hình các phím bấm và đích đến
   * `Transfer` → chuyển tới nhóm agent hoặc số nội bộ
   * `Voicemail` → kích hoạt cho các trường hợp ngoài giờ
3. **Thiết lập Routing theo thời gian** (Time-based Routing) nếu cần.
4. **Lưu và Activate** kịch bản — có hiệu lực ngay lập tức.
5. **Test** bằng cách gọi vào đầu số thử nghiệm.

***

[← Voice Brandname](voice-brandname.md)  |  [Tổng quan TCRM →](../tcrm/overview.md)
