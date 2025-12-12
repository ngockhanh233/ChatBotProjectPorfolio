# ChatBot Web API

Dự án ChatBot sử dụng Web API với Flask, sử dụng mô hình Machine Learning để trả lời câu hỏi tự động.

## Cài đặt

1. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```

2. Đảm bảo file `model.pkl` đã được tạo (nếu chưa có, chạy `train.py`):
```bash
python train.py
```

## Chạy API Server

```bash
python app.py
```

API sẽ chạy tại `http://localhost:5000`

## API Endpoints

### 1. Kiểm tra trạng thái
**GET** `/health`

Response:
```json
{
  "status": "healthy",
  "message": "API đang hoạt động bình thường"
}
```

### 2. Chat với bot
**POST** `/api/chat`

Request Body:
```json
{
  "message": "đặt hàng như thế nào"
}
```

hoặc

```json
{
  "question": "đặt hàng như thế nào"
}
```

Response thành công:
```json
{
  "success": true,
  "question": "đặt hàng như thế nào",
  "answer": "Bạn có thể đặt hàng trực tiếp trên website hoặc gọi tổng đài để được hỗ trợ."
}
```

Response lỗi:
```json
{
  "error": "Thiếu câu hỏi",
  "message": "Vui lòng cung cấp trường 'message' hoặc 'question'"
}
```

## Ví dụ sử dụng

### Sử dụng curl:
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "đặt hàng như thế nào"}'
```

### Sử dụng Python:
```python
import requests

response = requests.post('http://localhost:5000/api/chat', 
                        json={'message': 'đặt hàng như thế nào'})
print(response.json())
```

### Sử dụng JavaScript (fetch):
```javascript
fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ message: 'đặt hàng như thế nào' })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Cấu trúc dự án

- `app.py` - File chính chứa Flask API
- `chat_logic.py` - Logic xử lý chat, gọi model
- `model.py` - Module load và train model
- `train.py` - Script để train model từ data.txt
- `data.txt` - Dữ liệu training (câu hỏi và câu trả lời)
- `model.pkl` - File model đã được train

## Biến môi trường

- `PORT`: Port để chạy server (mặc định: 5000)
- `MODEL_FILE`: Đường dẫn đến file model (mặc định: model.pkl)

## Lưu ý

- Đảm bảo file `model.pkl` tồn tại trước khi chạy API
- Nếu thay đổi `data.txt`, cần train lại model bằng `train.py`

