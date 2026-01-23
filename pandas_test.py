import pandas as pd
import re
from konlpy.tag import Okt

data = {
    "review": [
        "앱이 너무 느리고 자꾸 튕겨요",
        "업데이트 이후로 훨씬 좋아졌어요 ㅎ",
        "디자인은 예쁜데 사용하기 불편함 -_-",
        "완전 최악입니다 다시는 안 씀 ^^;;;;",
        "속도도 빠르고 기능도 만족스러워요",
    ]
}

df = pd.DataFrame(data)
print(df)

# 특무누자 제거, 불필요한 공백 제거


def clean_text(text):
    text = re.sub(r"[^가-힣\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


df["cleaned_review"] = df["review"].apply(clean_text)
print(df)

# 형태소 분석 및 명사 추출
okt = Okt()


def tokenize(text):
    return [word for word, post in okt.pos(text) if post in ["Noun", "Adjective"]]


df["tokens"] = df["cleaned_review"].apply(tokenize)
print(df(["reviews", "tokens"]))
