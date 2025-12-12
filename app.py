from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_logic import get_answer, load_model

app = Flask(__name__)
CORS(app)  # Allow CORS for frontend

# Load model once when server starts
try:
    load_model("model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "ChatBot API đang hoạt động",
        "endpoints": {
            "/api/chat": "POST - Gửi câu hỏi và nhận câu trả lời",
            "/health": "GET - Kiểm tra trạng thái API"
        }
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "message": "API đang hoạt động bình thường"
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Thiếu dữ liệu",
                "message": "Gửi JSON: {'message': '...'}"
            }), 400

        user_text = data.get("message") or data.get("question")

        if not user_text or not isinstance(user_text, str):
            return jsonify({
                "error": "Câu hỏi không hợp lệ",
                "message": "Trường 'message' phải là chuỗi"
            }), 400

        answer = get_answer(user_text.strip())

        return jsonify({
            "success": True,
            "question": user_text.strip(),
            "answer": answer
        })

    except Exception as e:
        return jsonify({
            "error": "Lỗi xử lý",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    # Only for local development
    app.run(host="0.0.0.0", port=5000, debug=True)
