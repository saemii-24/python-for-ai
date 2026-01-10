import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")


url = f"https://archive-api.open-meteo.com/v1/archive?latitude=37.5665&longitude=126.9780&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FSeoul"

response = requests.get(url)
data = response.json()

#==================================

daily_time_data = data['daily']['time']
df = pd.DataFrame({
    'data':daily_time_data,
    'max_temp': data['daily']['temperature_2m_max'],
    
    
    'min_temp': data['daily']['temperature_2m_min']})

# string을 datetime으로 변환
df['data'] = pd.to_datetime(df['data'])

#==================================

plt.figure(figsize=(10, 6)) # 그래프 크기 설정
plt.plot(df['data'], df['max_temp'], marker='o', label='Max Temperature (°C)', color='r')
plt.plot(df['data'], df['min_temp'], marker='o', label='Min Temperature (°C)', color='b')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Seoul Daily Max and Min Temperatures (Past Week)')
plt.legend() # 범레 표시


plt.xticks(rotation=45) # 날짜 겹치지 않도록 글씨 45도 회전
plt.tight_layout() #제목, 축, 라벨이 잘리지 않게 자동 정렬

plt.savefig('seoul_temperatures.png')
plt.show()

#==================================

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/seoul_temperatures.csv', index=False)
print("Data saved to 'data/seoul_temperatures.csv' and plot saved to 'seoul_temperatures.png'")