# 📱 Sms Brandname

Dịch vụ gửi tin nhắn chăm sóc khách hàng và quảng cáo với tên thương hiệu riêng.

### 📋 Quy trình đăng ký

1. **Gửi hồ sơ:** Khách hàng cung cấp giấy phép kinh doanh.
2. **Khai báo Brandname:** TriAnh làm việc với các nhà mạng (Viettel, Mobi, Vina).
3. **Tích hợp:** Sử dụng API để bắt đầu gửi tin nhắn.

### 💡 Lưu ý quan trọng

> \[!TIP] Tin nhắn Brandname có độ dài tối đa **160 ký tự** cho tin không dấu.

### 🛠 Code mẫu gửi tin (CURL)

```bash
curl -X POST [https://api.trianh.vn/v1/sms/send](https://api.trianh.vn/v1/sms/send) \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d "brandname=TRIANH" \
  -d "phone=0901234567" \
  -d "message=Chao mung ban den voi TriAnh Solutions!"
```
