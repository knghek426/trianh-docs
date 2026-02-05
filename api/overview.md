# Hướng dẫn tích hợp API

## Xác thực
Sử dụng header: `Authorization: Bearer <API_KEY>`

## Base URLs
- Sandbox: `https://sandbox-api.trianh.vn/v1`
- Production: `https://api.trianh.vn/v1`

## Endpoints chính
- `POST /sms/send` — gửi SMS
- `GET /sms/status/{id}` — trạng thái SMS
- `POST /zalo/zns/send` — gửi ZNS

## Rate limit
Thông thường 60 reqs/phút (tuỳ gói). Liên hệ sales để tăng quota.

---
[Previous](../messaging/zalo-oa.md) • [Next](../api/sdk.md)
