"""
Script test API ChatBot
Sử dụng script này để test API sau khi đã chạy server
"""

import requests
import json

API_URL = "http://localhost:5000"

def test_health():
    """Test endpoint health check"""
    print("=" * 50)
    print("Test Health Check")
    print("=" * 50)
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        print()
        return response.status_code == 200
    except Exception as e:
        print(f"Lỗi: {e}")
        print("Đảm bảo API server đang chạy (python app.py)")
        print()
        return False

def test_chat(message):
    """Test endpoint chat"""
    print("=" * 50)
    print(f"Test Chat: '{message}'")
    print("=" * 50)
    try:
        response = requests.post(
            f"{API_URL}/api/chat",
            json={"message": message},
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        print()
        return response.status_code == 200
    except Exception as e:
        print(f"Lỗi: {e}")
        print("Đảm bảo API server đang chạy (python app.py)")
        print()
        return False

if __name__ == "__main__":
    print("\n🧪 Bắt đầu test API ChatBot\n")
    
    # Test health check
    if not test_health():
        print("❌ Health check thất bại. Dừng test.")
        exit(1)
    
    # Test các câu hỏi mẫu
    test_messages = [
        "đặt hàng như thế nào",
        "quên mật khẩu",
        "tên của bạn là gì",
        "số điện thoại hỗ trợ"
    ]
    
    print("\n" + "=" * 50)
    print("Test Chat với các câu hỏi mẫu")
    print("=" * 50 + "\n")
    
    for msg in test_messages:
        test_chat(msg)
    
    print("\n✅ Hoàn thành test!")

