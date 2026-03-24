import requests
import json

# Test API
try:
    response = requests.post(
        "http://localhost:5000/api/chat",
        json={"message": "Kinh nghiệm làm việc của bạn là gì?"},
        timeout=5
    )

    print(f"Status Code: {response.status_code}")
    data = response.json()
    print("Question:", data.get("question", "N/A"))
    print("Answer:", data.get("answer", "N/A"))

except Exception as e:
    print(f"Error: {e}")