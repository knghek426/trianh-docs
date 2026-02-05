# Dịch vụ IVR

IVR (Interactive Voice Response) cho phép xây dựng kịch bản thoại tương tác tự động: menu, thu thập thông tin, chuyển agent, voicemail.

## Tính năng
- Play audio / TTS
- Choice (nhấn phím), chuyển hàng đợi, voicemail
- Routing theo giờ làm việc & theo skill agent
- Ghi lại dữ liệu input (DTMF) và lưu vào CRM qua Webhook

## Hướng dẫn nhanh
1. Tạo Node IVR mới trên dashboard.
2. Thêm step: PlayAudio -> Choice -> Transfer/Voicemail.
3. Lưu và Activate kịch bản.

## Ví dụ kịch bản
- 1: Bán hàng -> Transfer tới nhóm Sales
- 2: Hỗ trợ kỹ thuật -> Transfer tới Support
- 0: Gặp tổng đài viên

---
[Previous](../solutions/voice-brandname.md) • [Next](../tcrm/overview.md)
