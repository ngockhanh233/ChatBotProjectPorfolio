web: gunicorn main:app --bind 0.0.0.0:$PORT
release: python train.py
web: gunicorn app:app --preload