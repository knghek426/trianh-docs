# 📱 Dịch vụ SMS Brandname

Dịch vụ gửi tin nhắn chăm sóc khách hàng và quảng cáo với tên thương hiệu riêng.

### 📋 Quy trình đăng ký
1. **Gửi hồ sơ:** Khách hàng cung cấp giấy phép kinh doanh.
2. **Khai báo Brandname:** TriAnh hỗ trợ khai báo với nhà mạng.
3. **Triển khai:** Hướng dẫn khách hàng sử dụng.

### 💡 Lưu ý quan trọng
> [!TIP]
> Tin nhắn Brandname có độ dài tối đa **160 ký tự** cho tin không dấu.

### 🛠 Code mẫu gửi tin (CURL)
```bash
curl -X POST [https://YOUR_DOMAIN/apismsservice/send](https://YOUR_DOMAIN/apismsservice/send) \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d "brandname=TRIANH" \
  -d "phone=0901234567" \
  -d "message=Chao mung ban den voi TriAnh Solutions!"