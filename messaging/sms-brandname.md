# SMS Brandname

SMS Brandname cho phép gửi tin nhắn với tên thương hiệu (sender name) thay cho số điện thoại — phù hợp cho OTP, thông báo giao dịch, marketing.

## Tính năng
- Gửi hàng loạt (bulk) và gửi cá nhân
- Tình trạng gửi (DELIVERED / FAILED / QUEUED)
- Báo cáo & thống kê chi tiết
- API và SDK hỗ trợ

## Mẫu request (curl)
```bash
curl -X POST "https://api.trianh.vn/v1/sms/send" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"from":"TRIANH","to":["849xxxxxxxx"],"message":"Ma OTP cua ban la 123456"}'
```

## Lưu ý
- Brandname cần hợp lệ theo quy định nhà mạng.
- Một số trường hợp yêu cầu chứng thực pháp nhân.

---
[Previous](../tcrm/user-guide.md) • [Next](../messaging/zalo-oa.md)
