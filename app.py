from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_logic import get_answer
import os

app = Flask(__name__)
CORS(app)  # Cho phép CORS để frontend có thể gọi API

@app.route('/')
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
                "message": "Vui lòng gửi JSON với trường 'message' hoặc 'question'"
            }), 400
        
        # Hỗ trợ cả 'message' và 'question'
        user_text = data.get('message') or data.get('question')
        
        if not user_text:
            return jsonify({
                "error": "Thiếu câu hỏi",
                "message": "Vui lòng cung cấp trường 'message' hoặc 'question'"
            }), 400
        
        if not isinstance(user_text, str) or not user_text.strip():
            return jsonify({
                "error": "Câu hỏi không hợp lệ",
                "message": "Câu hỏi phải là chuỗi không rỗng"
            }), 400
        
        # Lấy câu trả lời từ model
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

