# Voice Brandname

Voice Brandname cho phép phát thương hiệu (tên công ty) hoặc thông điệp thương hiệu trước khi cuộc gọi được kết nối tới khách hàng, giúp tăng nhận diện và độ tin cậy.

## Ứng dụng
- Nhắc thanh toán tự động
- Xác nhận đơn hàng, giao hàng
- Thông báo khuyến mãi có UID thương hiệu

## Quy trình hoạt động
1. Chuẩn bị file audio (MP3/WAV) hoặc dùng TTS (text-to-speech).
2. Đăng ký brandname/miền gọi với nhà mạng (nếu cần).
3. Tạo chiến dịch outbound qua dashboard hoặc API.

## API mẫu
```
POST /v1/voice/send
Headers: Authorization: Bearer <API_KEY>
Body:
{
  "to": "+849xxxxxxxx",
  "caller_id": "+84xxxxxxx",
  "audio_url": "https://assets.example.com/brand.mp3",
  "priority": "normal"
}
```

---
[Previous](../solutions/ccms.md) • [Next](../solutions/ivr.md)
