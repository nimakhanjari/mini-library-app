import json
import os

FILE_PATH = "data/books.json"


def load_books():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)
