# Sentiment Analysis System
Hệ thống phân tích cảm xúc bình luận

## 1. Tạo sinh dữ liệu:
+ Tự tạo mock data gồm 1000 bình luận tiếng việt về sản phẩm xe ô tô bao gồm các nhãn `positive`, `negative`, `neural` đa dạng và thực tế.
+ Bộ dữ liệu datasets được lưu dưới dạng CSV trong `datasets/mock_data_vietnamese_cars.csv`

## 2. Huấn luyện mô hình:
+ Sử dụng kiến trúc TF-IDF kết hợp Logistic Regression.
+ Loại dữ liệu: văn bản ngắn