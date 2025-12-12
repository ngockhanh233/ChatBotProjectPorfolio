import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

questions = []
answers = []

with open("data.txt", "r", encoding="utf8") as f:
    for line in f:
        line = line.strip()

        # Bỏ qua dòng trống
        if not line:
            print("⚠ Bỏ qua dòng trống")
            continue

        # Kiểm tra có dấu phân tách hay không
        if "|||" not in line:
            print("⚠ Dòng sai định dạng, không có '|||':", line)
            continue

        parts = line.split("|||")

        # Dòng phải có đúng 2 phần (câu hỏi và câu trả lời)
        if len(parts) != 2:
            print("⚠ Dòng sai định dạng (thừa hoặc thiếu '|||'):", line)
            continue

        q, a = parts
        q = q.strip()
        a = a.strip()

        if q == "" or a == "":
            print("⚠ Bỏ qua dòng thiếu nội dung:", line)
            continue

        questions.append(q)
        answers.append(a)

# Đảm bảo có dữ liệu hợp lệ
if len(questions) == 0:
    raise ValueError("❌ Không có dữ liệu hợp lệ trong data.txt")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = NearestNeighbors(n_neighbors=1, metric="cosine")
model.fit(X)

pickle.dump((vectorizer, model, answers), open("model.pkl", "wb"))

print("✅ Huấn luyện xong! Đã lưu model.pkl")
print(f"📌 Tổng số câu hỏi hợp lệ: {len(questions)}")
