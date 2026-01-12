import pandas as pd
import os
from helpers import calculate_total, format_currency

df = pd.read_csv('data/sales.csv')
print(df)

df['total_price'] = df['quantity'] * df['price']
print(df)

totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

df['total_price_2'] = totals



#output 폴더 만들기
os.makedirs('output', exist_ok=True)
df.to_excel('output/sales_with_total.xlsx', index=False)

excel_df = pd.read_excel('output/sales_with_total.xlsx')
print(excel_df)

