import os
from dotenv import load_dotenv

load_dotenv()

# os.environ 환경변수의 dict처럼 사용
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")


print(f"Using database: {api_key}")


def calcuate_total(item):
    total = 0
    for item in item:
        total += item["price"] * item.get("quantity", 1)
    return total


items = [
    {"name": "apple", "price": 1.2, "quantity": 10},
    {"name": "banana", "price": 0.5, "quantity": 5},
    {"name": "orange", "price": 0.8},
]
