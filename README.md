# ChatBot Web API

A ChatBot project using Web API with Flask, utilizing Machine Learning models to automatically answer questions.

## Installation

1. Install the dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure the `model.pkl` file is created (if not, run `train.py`):
```bash
python train.py
```

## Running the API Server

### Development (Local)
```bash
python app.py
```

### Production (Railway/Heroku)
```bash
python main.py
```

The API will run at `http://localhost:5000` (or the port specified in the PORT environment variable)

## API Endpoints

### 1. Home
**GET** `/`

Response:
```json
{
  "message": "ChatBot API is running",
  "endpoints": {
    "/api/chat": "POST - Send question and receive answer",
    "/health": "GET - Check API status"
  }
}
```

### 2. Health Check
**GET** `/health`

Response:
```json
{
  "status": "healthy",
  "message": "API is operating normally"
}
```

### 3. Chat with Bot
**POST** `/api/chat`

Request Body:
```json
{
  "message": "What is your name?"
}
```

or

```json
{
  "question": "What is your name?"
}
```

Success Response:
```json
{
  "success": true,
  "question": "What is your name?",
  "answer": "I'm Thu Hang, how can I help you?"
}
```

Error Response:
```json
{
  "error": "Missing question",
  "message": "Please provide the 'message' or 'question' field"
}
```

## Usage Examples

### Using curl:
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is your current position?"}'
```

### Using Python:
```python
import requests

response = requests.post('http://localhost:5000/api/chat',
                        json={'message': 'What skills do you have?'})
print(response.json())
```

### Using JavaScript (fetch):
```javascript
fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ message: 'Tell me about your projects?' })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Project Structure

- `main.py` - Main entry point for deployment (Railway/Heroku)
- `app.py` - Main Flask API with CORS support
- `chat_logic.py` - Chat processing logic, calls model
- `model.py` - Module to load and train model
- `train.py` - Script to train model from data.txt
- `test_model.py` - Direct model testing script
- `test_api.py` - API endpoints testing script
- `data.txt` - Training data (questions and answers)
- `model.pkl` - Trained model file
- `Procfile` - Deployment configuration for Heroku/Railway
- `requirements.txt` - Python dependencies

## Environment Variables

- `PORT`: Port to run the server (default: 5000)
- `MODEL_FILE`: Path to the model file (default: model.pkl)

## Testing

### Test Model Directly
```bash
python test_model.py
```

### Test API Endpoints
```bash
python test_api.py
```

## Deployment

The project is configured for deployment on cloud platforms:

- **Railway**: Uses `main.py` as entry point
- **Heroku**: Uses `Procfile` with gunicorn
- **Local**: Run `python app.py` for development

## Dependencies

- **Flask>=3.0.0**: Main web framework
- **flask-cors>=4.0.0**: CORS support for frontend
- **scikit-learn>=1.3.0**: Machine Learning
- **numpy>=1.24.0**: Numerical processing
- **scipy>=1.11.0**: Scientific computing
- **requests>=2.31.0**: HTTP requests
- **gunicorn>=21.2.0**: WSGI server for production

## Notes

- API supports CORS to allow calls from frontend
- Ensure `model.pkl` file exists before running the API
- If `data.txt` is changed, retrain the model using `train.py`
- Use `main.py` for production deployment
- Use `app.py` only for local development

