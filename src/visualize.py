import matplotlib.pyplot as plt
import pandas as pd
from db import connect_db

def fetch_weather_data(city):
    conn = connect_db()
    df = pd.read_sql(f"SELECT date, temperature, feels_like FROM weather_data WHERE city = '{city}' ORDER BY date", conn)
    conn.close()
    return df

def plot_temperature_trend(city):
    df = fetch_weather_data(city)
    df['date'] = pd.to_datetime(df['date'])
    plt.plot(df['date'], df['temperature'], label="Temperature")
    plt.plot(df['date'], df['feels_like'], label="Feels Like", linestyle='--')
    plt.title(f"Temperature Trend in {city}")
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    city = "Delhi"
    plot_temperature_trend(city)

if __name__ == '__main__':
    main()
