# Sentiment Analysis System
Hệ thống phân tích cảm xúc bình luận

## 1. Tạo sinh dữ liệu:
+ Tự tạo mock data gồm 1000 bình luận tiếng việt về sản phẩm xe ô tô bao gồm các nhãn `positive`, `negative`, `neural` đa dạng và thực tế.
+ Bộ dữ liệu datasets được lưu dưới dạng CSV trong `datasets/mock_data_vietnamese_cars.csv`

## 2. Lựa chọn và huấn luyện mô hình:
+ Sử dụng kiến trúc TF-IDF kết hợp Logistic Regression.
+ Loại dữ liệu: văn bản bình luận ngắn.
+ Lý do sử dụng:
    * Tối ưu hóa tài nguyên phần cứng: Mô hình huấn luyện cực nhanh mà không cần cấu hình hạ tầng GPU.
    * Tính năng N-gram nắm bắt ngữ cảnh tiếng việt khá tốt, đặc biệt là các biến có tính phân loại.
    * Mô hình Logistic Regression cơ bản, phù hợp cho bài toán với dữ liệu phân loại dựa trên nhãn.

## 3. Chiến lược lựa chọn chỉ số phù hợp:
Bời vì chỉ số Accuracy (độ chính xác tổng thể) dễ bị bóp méo nếu bộ dữ liệu mất cân bằng nhãn, nên chương trình đánh giá dựa trên chỉ số F1-Score (trung bình điều hòa):
+ Precision (Độ chính xác trên từng lớp): tránh việc gán nhãn nhầm (ví dụ: bình luận đang chê (Negative) nhưng lại phân loại nhầm thành khen (Positive), gây ảnh hưởng nghiêm trọng đến báo cáo thị trường).
+ Recall (Độ phủ): Đảm bảo hệ thống gom hết và không bỏ sót các tín hiệu phản hồi tiêu cực từ thị trường để xử lý khủng hoảng truyền thông kịp thời.

## 4. Một số file phục vụ xử lý dữ liệu:
+ File `data_generator.py`: giúp sinh tự động ngẫu nhiên dữ liệu bình luận.
+ File `model_generator.py`: giúp huấn luyện và tạo model file.


# Hướng dẫn cách chạy chương trình:
## 1. Kích hoạt môi trường ảo:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

## 2. Tải thư viện bắt buộc
```bash
pip install -r requirements.txt
```

## 3. Mở 2 Terminal phục vụ chạy chương trình:
```bash
# Phần frontend
cd src/frontend
npm run dev

# Phần backend
cd src/backend
python app.py
```
+ Link frontend (sử dụng): http://localhost:5173/
+ Link backend: http://localhost:5000/