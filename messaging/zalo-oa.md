# Zalo OA & ZNS

Zalo OA (Official Account) và ZNS (Zalo Notification Service) dùng để gửi tin nhắn đã phê duyệt tới người dùng Zalo: thông báo đơn hàng, OTP, confirm.

## Các bước tích hợp
1. Tạo Zalo OA tại `https://oa.zalo.me`.
2. Đăng ký template ZNS và chờ phê duyệt.
3. Sử dụng access token OA để gửi tin nhắn qua API.

## Ví dụ payload
```
POST /zalo/zns/send
{
  "recipient": "zalo_user_id",
  "template_id": "TEMPLATE_ID",
  "parameters": {"order_id":"#12345","total":"1,000,000 VND"}
}
```

---
[Previous](../messaging/sms-brandname.md) • [Next](../api/overview.md)
