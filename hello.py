import requests
from IPython.display import JSON

def get_specific_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    r = response.json()
    return r["current_weather"]['temperature']

print(get_specific_weather(37.5665, 126.9780)) # 서울의 위도와 경도
