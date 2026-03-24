import sys
sys.stdout.reconfigure(encoding='utf-8')

from chat_logic import get_answer

# Test model trực tiếp - dự án
questions = [
    "Dự án của bạn?",
    "Chi tiết dự án của bạn?",
    "Kể về dự án đi"
]

for question in questions:
    answer = get_answer(question)
    print(f"\nQuestion: {question}")
    print(f"Answer: {answer}")

    # Kiểm tra có mời gặp trực tiếp không
    if "gặp trực tiếp" in answer or "trao đổi" in answer:
        print("✅ Mời gặp trực tiếp thành công!")
    else:
        print("❌ Không mời gặp trực tiếp")