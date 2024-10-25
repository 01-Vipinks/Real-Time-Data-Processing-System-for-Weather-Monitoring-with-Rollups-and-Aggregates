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

&nbsp;Python 3.x
&nbsp;Flask
&nbsp;Flask-SQLAlchemy
&nbsp;Requests
&nbsp;Docker
&nbsp;Docker Compose

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
&nbsp;The frontend is built using HTML, CSS, and JavaScript. The app uses a simple form to allow users to enter a city name and retrieve weather data.

## Backend
&nbsp;The backend is built using Flask, a lightweight Python web framework. The app uses Flask-SQLAlchemy to interact with the SQLite database.

## Implementation of additional features
