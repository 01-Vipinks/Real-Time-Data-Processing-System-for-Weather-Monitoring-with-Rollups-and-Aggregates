# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system will utilize data from the OpenWeatherMap API.

## Table of Contents
* Features
* Technologies
* Setup Instructions
* Dockerization
* Project Structure
* Usage
* Contributing
* License

## Features
* Fetch real-time weather data from the OpenWeatherMap API
* Display weather information such as temperature, feels-like temperature, and weather conditions
* Store data in a database to reduce redundant API requests
* Simple frontend for city input and data display

## Technologies
* Frontend: HTML, CSS, JavaScript (Vanilla JS)
* Backend: Python (Flask)
* Database: SQLite (or PostgreSQL with Docker)
* Containerization: Docker, Docker Compose

## Setup Instructions
1. Prerequisites
Make sure you have the following installed:

* Python 3.x  
* Flask  
* Flask-SQLAlchemy  
* Requests  
* Docker  
* Docker Compose  

## Installation
* Clone the repository: git clone https://github.com/your-username/weather-app.git
* Navigate to the repository directory: cd weather-app
* Install dependencies: pip install -r requirements.txt
* Build the Docker image: docker build -t weather-app .
* Run the application: docker-compose up

## Usage
* Open a web browser and navigate to http://localhost:5000
* Enter a city name in the form and click the "Get Weather" button
* The app will retrieve the weather data from the OpenWeatherMap API and display it on the page

## API Endpoints
* /weather: Retrieves weather data for a given city
* /weather/<city>: Retrieves weather data for a specific city

## Database
&nbsp;The app uses a SQLite database to store weather data. The database is created automatically when the app is run for the first time.

## Frontend
&nbsp;The frontend is built using HTML, CSS, and JavaScript. The app uses a simple form to allow users to enter a city name and retrieve weather&nbsp;data.

## Backend
&nbsp;The backend is built using Flask, a lightweight Python web framework. The app uses Flask-SQLAlchemy to interact with the SQLite database.

## Implementation of additional features
### Forecast for Next 5 Days
Provide a 5-day weather forecast with daily summaries. The OpenWeatherMap API offers a forecast endpoint that returns weather data for every 3-hour interval. You can use this data to summarize the forecast for each day.  
##### Implementation  
* API Request: Update your get_weather function to fetch the 5-day forecast if the forecast flag is set.  
* Backend Route: Add a new /forecast endpoint in app.py  

### Temperature Unit Toggle (°C/°F)  
Allow users to toggle between Celsius and Fahrenheit.  
#### Implementation  
* Frontend Toggle Button: Add a button in index.html for the toggle  
* JavaScript Toggle Logic: In script.js, implement the toggle feature  

### Historical Weather Data (With Graphs)  
Use a JavaScript library like Chart.js to plot temperature trends over time for a given city.  
#### Implementation  
* Extend Database Schema: Store temperature history for each city by adding a new table WeatherHistory  
* Log Weather Data on Each Request: After retrieving weather data, log it in WeatherHistory  
* Plot Data with Chart.js: On the frontend, use Chart.js to create a line graph of temperatures. You can fetch the historical data and populate the chart with it.  

## Contributing  
If you'd like to contribute to this project, please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your feature: git checkout -b feature-name  
3. Commit your changes: git commit -m 'Add feature'  
4. Push to the branch: git push origin feature-name  
5. Submit a pull request.

## License  
This project is licensed under the MIT License.  
