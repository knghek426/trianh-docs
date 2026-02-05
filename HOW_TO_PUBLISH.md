# Hướng dẫn push lên GitHub và đồng bộ với GitBook

1. Chuẩn bị repo local (ví dụ folder `trianh-docs` chứa `README.md` và `SUMMARY.md`):
```bash
git init
git add .
git commit -m "Initial commit: TriAnh docs"
```
2. Tạo repo trên GitHub, add remote và push:
```bash
git remote add origin git@github.com:<your-org>/trianh-docs.git
git branch -M main
git push -u origin main
```
3. Kết nối GitBook: https://app.gitbook.com → Import from GitHub → Chọn repository → Chọn root là `/` (nếu để file ở gốc) hoặc `/docs`.
4. Kiểm tra sidebar và nội dung. GitBook sử dụng `SUMMARY.md` để build sidebar và cung cấp tính năng Next/Previous tự động.

5. (Tùy chọn) Thiết lập GitHub Actions để build hoặc deploy static site.

**Ghi chú:** đổi `SUMARY.md` (nếu có) thành `SUMMARY.md` để GitBook nhận diện đúng.
