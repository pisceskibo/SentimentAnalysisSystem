# Libraries
import csv
import random
import os

# Tập mẫu dữ liệu thô về bình luận ô tô
samples = [
    # Positive
    ("Xe đi rất đầm chắc, cách âm tốt vượt trội trong tầm giá.", "positive"),
    ("Thiết kế ngoại thất quá đẹp, nhìn sang trọng như xe châu Âu.", "positive"),
    ("Tiết kiệm nhiên liệu cực kỳ, chạy dịch vụ hay gia đình đều ổn.", "positive"),
    ("Màn hình giải trí mượt, loa nghe hay, đáng tiền.", "positive"),
    ("Hệ thống treo êm ái, đi qua gờ giảm tốc không bị xóc nảy.", "positive"),
    ("Động cơ turbo tăng tốc bốc, cảm giác lái thể thao rất phấn khích.", "positive"),
    ("Nội thất bọc da cao cấp, không gian ngồi hàng ghế sau cực kỳ rộng rãi.", "positive"),
    ("Hệ thống an toàn chủ động ADAS hoạt động rất nhạy và chuẩn xác.", "positive")

    # Negative
    ("Vỏ xe hơi mỏng, đi tốc độ cao nghe tiếng lốp vọng vào cabin rất khó chịu.", "negative"),
    ("Điều hòa mát chậm quá, trưa nắng ngồi hàng ghế sau nóng chảy mỡ.", "negative"),
    ("Xe hay bị lỗi vặt về cảm biến, mang ra hãng bảo hành suốt phát mệt.", "negative"),
    ("Động cơ hơi yếu, mỗi lần muốn vượt xe tải trên cao tốc là hụt hơi.", "negative"),
    ("Chi phí bảo dưỡng của hãng quá đắt đỏ, dịch vụ chăm sóc khách hàng kém.", "negative"),
    ("Nhựa nội thất nhìn rẻ tiền, chạy qua đường xấu là nghe tiếng lọc cọc.", "negative"),
    ("Đèn pha nguyên bản theo xe tối quá, đi đêm trời mưa tầm nhìn rất hạn chế." "negative"),
    ("Hộp số giật cục khi đi trong phố đông người, trải nghiệm kém mượt mà.", "negative")

    # Neutral
    ("Xe này nhìn cũng bình thường, không có gì quá nổi bật.", "neutral"),
    ("Giá lăn bánh tầm 700 triệu thì cũng là một lựa chọn để cân nhắc.", "neutral"),
    ("Tôi đang phân vân xe này với một dòng xe khác cùng phân khúc.", "neutral"),
    ("Xe mới mua nên chưa có đánh giá gì nhiều, cần trải nghiệm thêm.", "neutral"),
    ("Thông số kỹ thuật thấy ghi giống bản cũ, không thay đổi mấy.", "neutral"),
    ("Mức tiêu hao nhiên liệu đường hỗn hợp tầm bao nhiêu lít thế các bác?", "neutral"),
    ("Hãng mới công bố giá niêm yết rồi, không biết khi nào xe về đại lý.", "neutral"),
    ("Phụ tùng dòng xe này bên ngoài có dễ thay thế và sẵn hàng không nhỉ?", "neutral")
]

modifiers = ["", "Nhìn chung ", "Thực sự thì ", "Ôi dào, ", "Đánh giá khách quan: ", "Nói chung là "]

# Sinh thêm dữ liệu random
def generate_mock_data(output_path, total_records):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["text", "sentiment"])
        
        count = 0
        while count < total_records:
            sample_text, sentiment = random.choice(samples)
            mod = random.choice(modifiers)
            full_text = f"{mod}{sample_text}"
            
            # Tránh trùng lặp máy móc tuyệt đối bằng cách thêm các từ ngẫu nhiên
            writer.writerow([full_text, sentiment])
            count += 1
            
    print(f"[INFO] Đã tạo thành công {total_records} mẫu dữ liệu tại {output_path}")

if __name__ == "__main__":
    generate_mock_data("datasets/mock_data_vietnamese_cars.csv", total_records=1000)