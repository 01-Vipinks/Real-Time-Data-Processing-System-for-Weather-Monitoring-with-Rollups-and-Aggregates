import React, { useState, useEffect } from 'react';
import { getWeather, getWeatherHistory } from '../api';

function Weather({ city }) {
    const [weather, setWeather] = useState(null);
    const [history, setHistory] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const weatherData = await getWeather(city);
            setWeather(weatherData);
            const historyData = await getWeatherHistory(city);
            setHistory(historyData);
        }

        fetchData();
    }, [city]);

    return (
        <div>
            <h2>Weather in {city}</h2>
            {weather && (
                <div>
                    <p>Temperature: {weather.temperature}°C</p>
                    <p>Feels Like: {weather.feels_like}°C</p>
                    <p>Condition: {weather.condition}</p>
                </div>
            )}

            <h3>Weather History:</h3>
            <ul>
                {history.map((record, index) => (
                    <li key={index}>{record[1]}: {record[2]}°C (Feels Like {record[3]}°C) - {record[4]}</li>
                ))}
            </ul>
        </div>
    );
}

export default Weather;
