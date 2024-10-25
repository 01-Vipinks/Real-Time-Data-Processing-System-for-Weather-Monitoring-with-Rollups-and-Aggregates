import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def connect_db():
    conn = psycopg2.connect(
        host="db",  # Docker PostgreSQL service name
        database="weather",
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(50),
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            temperature FLOAT,
            feels_like FLOAT,
            weather_condition VARCHAR(50)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def get_weather_history(city):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data WHERE city=%s ORDER BY date DESC LIMIT 10", (city,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
