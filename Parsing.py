from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


def parse_reviews(url, max_pages=3):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)
    time.sleep(15)  # время на капчу

    reviews = []

    # ищем элементы
    elements = driver.find_elements(By.CSS_SELECTOR, "a.review-title")

    print(f"Найдено: {len(elements)} отзывов")

    for el in elements:
        text = el.text.strip()
        if text:
            reviews.append({
                "text": text,
                "label": "positive"
            })

    driver.quit()
    return reviews


def save_to_csv(reviews, filename="reviews.csv"):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Сохранено {len(df)} отзывов в {filename}")
