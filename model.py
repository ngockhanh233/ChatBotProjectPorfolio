import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def train_model(data_file="data.txt", model_file="model.pkl"):
    questions = []
    answers = []

    with open(data_file, "r", encoding="utf8") as f:
        for line in f:
            q, a = line.strip().split("|||")
            questions.append(q)
            answers.append(a)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)

    model = NearestNeighbors(n_neighbors=1, metric="cosine")
    model.fit(X)

    pickle.dump((vectorizer, model, answers), open(model_file, "wb"))
    print("Huấn luyện xong! Model đã lưu vào", model_file)

def load_model(model_file="model.pkl"):
    return pickle.load(open(model_file, "rb"))
