import os
import re
import json
from datetime import datetime
import pandas as pd

DATA_DIR = "raw_data"
OUTPUT_DIR = "output"

def parse_date(date_str):
    """날짜 문자열을 YYYY-MM-DD 형식으로 변환"""
    # "12/01/2025" -> "2025-12-01"
    match = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_str)
    if match:
        month, day, year = match.groups()
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return None

def parse_reviews_from_file(file_path, rating):
    """파일에서 데이터 파싱"""
    # with = 끝나면 자동으로 자원 정리 (파일 열고 자동으로 닫음
    # 파일을 r = read 열겠다. encoding='utf-8' = utf-8 인코딩으로 열겠다.
    with open(file_path, 'r', encoding='utf-8') as f:
        # if line.strip() 빈 줄 제거, 뒤 쪽 내용은 빈 줄이 아닌 경우에만 for문 실행하라는 의미
        lines = [line.strip() for line in f.readlines() if line.strip()] 
    
    reviews = []
    i = 0
    
    while i < len(lines):
        # 날짜 파싱
        date_str = lines[i]
        date = parse_date(date_str)
        
        if date is None:
            i += 1
            continue
        
        # 제목 (건너뛰기)
        if i + 1 < len(lines):
            title = lines[i + 1]  # 제목은 사용하지 않음
        else:
            i += 1
            continue
        
        # 리뷰 내용 수집 (다음 날짜가 나올 때까지 모든 줄)
        review_lines = []
        j = i + 2
        
        while j < len(lines):
            # 다음 줄이 날짜인지 확인
            if parse_date(lines[j]) is not None:
                break
            review_lines.append(lines[j])
            j += 1
        
        # 리뷰 내용이 없으면 스킵
        if not review_lines:
            i = j
            continue
        
        # 여러 줄을 공백으로 연결
        review = " ".join(review_lines)
        
        reviews.append({
            "date": date,
            "review": review,
            "rating": rating,
        })
        
        # 다음 리뷰로 이동
        i = j
    
    return reviews

def analyze_all_reviews():
    """모든 리뷰 파일 분석"""
    all_reviews = []
    
    files = [
        f for f in os.listdir(DATA_DIR)
        if f.startswith("score") and f.endswith(".txt")
    ]
    
    for file in sorted(files):
        # 파일명에서 rating 추출 (예: score1.txt -> 1)
        match = re.search(r'score(\d+)\.txt', file)
        if match:
            rating = int(match.group(1))
            file_path = os.path.join(DATA_DIR, file)
            reviews = parse_reviews_from_file(file_path, rating)
            all_reviews.extend(reviews)
            print(f"✓ {file}: {len(reviews)}개 리뷰 파싱 완료")
    
    return all_reviews

def save_results(reviews):
    """결과를 JSON과 Excel 파일로 저장"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # JSON 저장
    json_file = os.path.join(OUTPUT_DIR, "reviews.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        #json.dump(파이썬객체, 파일객체)
        # ensure_ascii=False = 한글 깨짐 방지
        # indent=2 = 보기 좋게 들여쓰기
        json.dump(reviews, f, ensure_ascii=False, indent=2) 
    # Excel 저장
    df = pd.DataFrame(reviews)
    excel_file = os.path.join(OUTPUT_DIR, "reviews.xlsx")
    df.to_excel(excel_file, index=False, engine='openpyxl')
    
    print(f"\n📁 결과 저장 완료:")
    print(f"   - JSON: {json_file}")
    print(f"   - Excel: {excel_file}")
    print(f"📊 총 {len(reviews)}개 리뷰 파싱 완료")
