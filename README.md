# CV Nguyễn Duy Quyền

14 mẫu CV giữ thiết kế của repo gốc, cập nhật nội dung và ảnh chân dung theo CV PDF được cung cấp.

- Mở `index.html` để xem, chọn mẫu và tải PDF tương ứng.
- Các mẫu HTML có tiền tố `nguyen-duy-quyen-cv`.
- Thư mục `pdf/` chứa 14 bản PDF tương ứng.
- Nội dung được chuyển sang tiếng Việt, giữ nguyên mốc thời gian và thông tin kinh nghiệm trong PDF nguồn. GitHub dùng tài khoản chủ repo: `duyquyen96`.

## Cập nhật nội dung

Chỉnh dữ liệu dùng chung ở đầu `build_cv_styles.py`, sau đó chạy:

```bash
python3 build_cv_styles.py
```

Cần Google Chrome/Chromium hoặc wkhtmltopdf để xuất PDF. Các file tạm nằm trong `work/` và được Git bỏ qua.

Chỉ tạo lại HTML, không xuất PDF:

```bash
python3 -c "import build_cv_styles as cv; cv.main(export_pdf=False)"
```

Chỉ xuất lại PDF:

```bash
python3 build_cv_styles.py --pdf-only
```

## Font chữ

Cả 14 mẫu dùng Source Sans 3 (Adobe), các độ đậm 400 / 600 / 700.
Font và giấy phép SIL Open Font License được lưu tại `assets/fonts/`.
Bản PDF nhúng font để hiển thị tiếng Việt nhất quán khi xem hoặc in.
