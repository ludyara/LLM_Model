import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

from sentence_transformers import SentenceTransformer

def llm_model():
    # 1. Загрузка размеченных данных
    df = pd.read_csv("reviews.csv", sep=';')

    # преобразуем метки в числа
    df["label_num"] = df["label"].map({
        "positive": 1,
        "negative": 0
    })

    # 2. Деление с сохранением пропорций классов
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label_num"],
        test_size=0.2,
        stratify=df["label_num"],  # ВАЖНО!
        random_state=42
    )

    # 3. Embeddings
    model = SentenceTransformer("all-MiniLM-L6-v2")

    X_train_emb = model.encode(X_train.tolist(), show_progress_bar=True)
    X_test_emb = model.encode(X_test.tolist(), show_progress_bar=True)

    # 4. Классификатор (обучение с учителем)
    clf = LogisticRegression()
    clf.fit(X_train_emb, y_train)

    # 5. Оценка
    y_pred = clf.predict(X_test_emb)

    print("\nРезультаты на тесте:\n")
    print(classification_report(y_test, y_pred))