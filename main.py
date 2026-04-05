from Parsing import parse_reviews, save_to_csv
from LLM_model import llm_model

if __name__ == "__main__":
    # сайт с отзывами
    # URL = "https://otzovik.com/reviews/kompaniya_biznes-yurist_russia_sankt-peterburg/3"

    # Парсим сайт чтобы вытащить текст отзывов
    # reviews = parse_reviews(URL, max_pages=3)
    # сохраняем в csv
    # save_to_csv(reviews)

    # Производим обучение модели и выводим результат
    llm_model()