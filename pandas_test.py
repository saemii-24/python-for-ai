import pandas as pd
import re

data = {
    "text": [
        "This app is amazing and very useful",
        "Terrible update, 너무 불편해요",
        "I like the design but it crashes often",
        "완전 별로임 다시는 안씀",
    ]
}

df = pd.DataFrame(data)


def clean_text(text):
    text = text.lower()  # 소문자
    text = re.sub(r"[^a-zA-Z가-힣\s]", "", text)  # 특수문자 제거
    return text


df["clean_text"] = df["text"].apply(clean_text)
