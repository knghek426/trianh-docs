<div style="border:1px solid #e8f5e9; background:#f0fff4; padding:20px; border-radius:12px;">
<h2 style="margin-top:0">⚙️ Hướng dẫn tích hợp API</h2>
<p>TriAnh Solutions cung cấp bộ <strong>REST API đầy đủ</strong> cho phép doanh nghiệp tích hợp các tính năng nhắn tin (SMS, ZNS/ZBS), thoại (Voice) và dữ liệu CRM vào hệ thống hiện có của mình một cách nhanh chóng và linh hoạt.</p>
<p style="margin-bottom:0">📞 Hỗ trợ kỹ thuật: <strong>1900 27 27 77</strong> &nbsp;|&nbsp; 📧 <strong>support@trianh.vn</strong></p>
</div>

---

## I. Tổng quan

**API TriAnh** sử dụng kiến trúc **RESTful**, xác thực bằng **Bearer Token**, trả về dữ liệu dạng **JSON**. Hỗ trợ hai môi trường: Sandbox (phát triển & test) và Production (thực tế).

### Lịch sử cập nhật
| Ngày | Người Cập Nhật | Version | Mô tả |
| :--- | :--- | :--- | :--- |
| 13/03/2026 | TriAnh Docs | Ver 1.0 | Khởi tạo tài liệu |

---

## II. Xác thực (Authentication)

Tất cả API request đều yêu cầu header xác thực:

```http
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

> API Key được cấp khi đăng ký dịch vụ. Liên hệ **support@trianh.vn** để được cấp key và hướng dẫn sử dụng.

---

## III. Base URLs

| Môi trường | Base URL |
| :--- | :--- |
| 🧪 Sandbox | `https://sandbox-api.trianh.vn/v1` |
| 🚀 Production | `https://api.trianh.vn/v1` |

---

## IV. Endpoints chính

### 1. SMS Brandname

| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `POST` | `/sms/send` | Gửi tin nhắn SMS |
| `GET` | `/sms/status/{message_id}` | Kiểm tra trạng thái tin nhắn |
| `GET` | `/sms/report` | Báo cáo chiến dịch SMS |

**Gửi SMS:**
```bash
curl -X POST "https://api.trianh.vn/v1/sms/send" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "src": "TRIANH",
    "to": ["849xxxxxxxx"],
    "message": "Ma OTP cua ban la 123456. Hieu luc trong 5 phut."
  }'
```

### 2. Zalo ZNS / ZBS

| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `POST` | `/zalo/zbs/send` | Gửi tin nhắn ZBS theo template |
| `GET` | `/zalo/template/list` | Danh sách template ZBS đã được duyệt |
| `GET` | `/zalo/zbs/status/{message_id}` | Kiểm tra trạng thái gửi ZBS |

**Gửi ZBS:**
```bash
curl -X POST "https://api.trianh.vn/v1/zalo/zbs/send" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "oa_id": "<OA_ID>",
    "phone": "849xxxxxxxx",
    "template_id": "<TEMPLATE_ID>",
    "template_data": {
      "ten_khach": "Nguyen Van A",
      "so_don_hang": "DH001"
    }
  }'
```

### 3. Voice / IVR

| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `POST` | `/voice/call` | Khởi tạo cuộc gọi outbound |
| `GET` | `/voice/call/{call_id}` | Trạng thái cuộc gọi |
| `GET` | `/voice/recording/{call_id}` | Lấy link ghi âm |

### 4. Contact (TCRM)

| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `GET` | `/crm/contacts` | Danh sách contact |
| `POST` | `/crm/contacts` | Tạo contact mới |
| `PUT` | `/crm/contacts/{id}` | Cập nhật thông tin contact |
| `POST` | `/crm/contacts/{id}/notes` | Thêm ghi chú vào contact |

---

## V. Rate Limit

| Gói dịch vụ | Giới hạn |
| :--- | :--- |
| Mặc định | **60 requests/phút** |
| Gói nâng cao | Liên hệ Sales để tăng quota |

Khi vượt quá Rate Limit, API trả về:
```json
{
  "error": "rate_limit_exceeded",
  "message": "Too many requests. Please retry after 60 seconds.",
  "retry_after": 60
}
```

---

## VI. Mã lỗi phổ biến

| Mã lỗi | Ý nghĩa | Hướng xử lý |
| :--- | :--- | :--- |
| `400` | Bad Request | Kiểm tra lại body request và định dạng |
| `401` | Unauthorized | Kiểm tra lại API Key |
| `403` | Forbidden | Tài khoản không có quyền thực hiện action này |
| `404` | Not Found | ID không tồn tại |
| `429` | Rate Limit Exceeded | Chờ và thử lại sau |
| `500` | Internal Server Error | Liên hệ support@trianh.vn |

---

## VII. Webhook (Callback)

TriAnh hỗ trợ **Webhook** để nhận thông báo realtime về trạng thái tin nhắn, cuộc gọi:

```json
// Payload mẫu khi gửi SMS thành công
{
  "event": "sms.delivered",
  "message_id": "MSG_20260113_001",
  "to": "849xxxxxxxx",
  "timestamp": "2026-01-13T14:30:00+07:00"
}
```

> Cấu hình Webhook URL tại phần **Cài đặt → Tích hợp → Webhook** trên giao diện TCRM.

---

[← ZBS Template (Zalo)](../messaging/zalo-oa.md)
