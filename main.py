"""
File chính để chạy dự án ChatBot Web API.
Tự động train model và khởi động API server.
"""

from model import train_model
from app import app
import os

if __name__ == "__main__":
    print("=" * 50)
    print("ChatBot Web API - Tự động train và khởi động")
    print("=" * 50)
    
    # Bước 1: Train model
    print("\n[1/2] Đang train model từ data.txt...")
    try:
        train_model(data_file="data.txt", model_file="model.pkl")
        print("✅ Train model thành công!")
    except Exception as e:
        print(f"❌ Lỗi khi train model: {e}")
        print("Đảm bảo file data.txt tồn tại và có định dạng đúng (câu hỏi|||câu trả lời)")
        exit(1)
    
    # Bước 2: Khởi động API server
    print("\n[2/2] Đang khởi động API server...")
    print("API sẽ chạy tại http://localhost:5000")
    print("Nhấn Ctrl+C để dừng server\n")
    
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    except KeyboardInterrupt:
        print("\n\nĐã dừng server.")
    except Exception as e:
        print(f"\n❌ Lỗi khi khởi động server: {e}")
