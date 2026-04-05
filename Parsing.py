import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_reviews(url, max_pages=5):
    reviews = []

    for page in range(1, max_pages + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)

        if response.status_code != 200:
            print(f"Ошибка на странице {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Ищем отзывы по структуре
        review_tags = soup.find_all("h3")

        for tag in review_tags:
            a_tag = tag.find("a", class_="review-title")
            if a_tag:
                text = a_tag.get_text(strip=True)
                if text:
                    reviews.append({
                        "text": text,
                        "label": "positive"  # по умолчанию
                    })

        print(f"Страница {page} обработана")

    return reviews


def save_to_csv(reviews, filename="reviews.csv"):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Сохранено {len(df)} отзывов в {filename}")
