from model import load_model
import os

# Load model khi module được import (chỉ load một lần)
_model_data = None

def _ensure_model_loaded():
    """Đảm bảo model đã được load"""
    global _model_data
    if _model_data is None:
        model_file = os.environ.get('MODEL_FILE', 'model.pkl')
        _model_data = load_model(model_file)
    return _model_data

def get_answer(user_text):
    """
    Lấy câu trả lời cho câu hỏi của người dùng
    
    Args:
        user_text (str): Câu hỏi của người dùng
    
    Returns:
        str: Câu trả lời từ model
    """
    vectorizer, model, answers = _ensure_model_loaded()
    X = vectorizer.transform([user_text])
    dist, idx = model.kneighbors(X)
    return answers[idx[0][0]]
