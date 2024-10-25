CREATE DATABASE weather;

CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    feels_like FLOAT,
    weather_condition VARCHAR(50)
);
