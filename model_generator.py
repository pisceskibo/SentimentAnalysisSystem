# Libraries
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Tạo model file
def generate_ai_model(data_path, model_output_path):
    # 1. Đọc dữ liệu
    df = pd.read_csv(data_path)
    
    # 2. Tiền xử lý dữ liệu cơ bản
    df['text'] = df['text'].str.lower().str.strip()
    
    # 3. Chia tập dữ liệu Train/Validation theo tỷ lệ 80/20 hợp lý
    X_train, X_val, y_train, y_val = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42, stratify=df['sentiment'])
    
    # 4. Trích xuất đặc trưng bằng TF-IDF N-gram đối với tiếng việt
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_val_tfidf = vectorizer.transform(X_val)
    
    # 5. Logistic Regression
    model = LogisticRegression(C=1.0, max_iter=1000)
    model.fit(X_train_tfidf, y_train)
    
    # 6. Đánh giá kết quả trên tập Validation
    y_pred = model.predict(X_val_tfidf)
    print("=== KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH ===")
    print(f"Accuracy: {accuracy_score(y_val, y_pred):.4f}")
    print("\nChi tiết chỉ số trên từng nhãn (Classification Report):")
    print(classification_report(y_val, y_pred))
    
    # 7. Đóng gói lưu trữ Model file
    payload = {
        'vectorizer': vectorizer,
        'model': model
    }
    with open(model_output_path, 'wb') as f:
        pickle.dump(payload, f)
    print(f"[INFO] Đã lưu model thành công tại: {model_output_path}")

if __name__ == "__main__":
    generate_ai_model("datasets/mock_data_vietnamese_cars.csv", "ai_models/tfidf_sentiment_model.pkl")