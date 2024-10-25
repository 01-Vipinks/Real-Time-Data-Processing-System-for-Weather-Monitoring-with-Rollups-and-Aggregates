import requests
from db import connect_db

API_KEY = "f12f8b6480291ba2d76f7d0baf1a2a08"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather_data(city):
    params = {'q': city, 'appid': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def fetch_and_process_weather(city):
    weather_data = fetch_weather_data(city)
    temp = kelvin_to_celsius(weather_data['main']['temp'])
    feels_like = kelvin_to_celsius(weather_data['main']['feels_like'])
    condition = weather_data['weather'][0]['main']
    
    # Save to database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather_data (city, temperature, feels_like, weather_condition)
        VALUES (%s, %s, %s, %s)
    """, (city, temp, feels_like, condition))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {
        "city": city,
        "temperature": temp,
        "feels_like": feels_like,
        "condition": condition
    }
