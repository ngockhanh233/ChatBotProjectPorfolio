"""
Main entrypoint for ChatBot Web API (for deployment on Railway).
Loads the model and starts the API server.
"""

from app import app
import os

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 ChatBot Web API — Starting server...")
    print("=" * 60)

    try:
        port = int(os.environ.get("PORT", 5000))
        print(f"🌍 API running on: http://localhost:{port}")
        print("Press Ctrl+C to stop.\n")
        app.run(host="0.0.0.0", port=port, debug=False)
    except Exception as e:
        print(f"❌ Server failed to start: {e}")
