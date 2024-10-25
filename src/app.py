from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_data.db'
db = SQLAlchemy(app)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.Float, nullable=False)
    feels_like = db.Column(db.Float, nullable=False)
    main = db.Column(db.String(100), nullable=False)
    dt = db.Column(db.DateTime, nullable=False)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        weather_data = WeatherData.query.filter_by(city=city).first()
        if weather_data:
            return jsonify({
                'temp': weather_data.temp,
                'feels_like': weather_data.feels_like,
                'main': weather_data.main,
                'dt': weather_data.dt.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            with open('config.json') as f:
                config = json.load(f)
            api_key = config['api_key']
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
            data = response.json()

            if response.status_code == 200:
                weather_data = WeatherData(
                    city=city,
                    temp=data['main']['temp'],
                    feels_like=data['main']['feels_like'],
                    main=data['weather'][0]['main'],
                    dt=datetime.now()
                )
                db.session.add(weather_data)
                db.session.commit()
                return jsonify({
                    'temp': weather_data.temp,
                    'feels_like': weather_data.feels_like,
                    'main': weather_data.main,
                    'dt': weather_data.dt.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                return jsonify({'error': 'Could not retrieve weather data'}), 500
    return jsonify({'error': 'Invalid city'}), 400

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
