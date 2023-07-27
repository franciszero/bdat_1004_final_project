from app import db
from datetime import datetime, timedelta
import random
import json


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), index=True)
    date = db.Column(db.String(64), index=True)
    temperature = db.Column(db.Float)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'city': self.city,
            'date': self.date,
            'temperature': self.temperature,
        }

    def to_json(self):
        return {
            'id': self.id,
            'city': self.city,
            'date': self.date,
            'temperature': self.temperature,
        }

    def __repr__(self):
        return str({
            'id': self.id,
            'city': self.city,
            'date': self.date,
            'temperature': self.temperature,
        })


# class CityWeather(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     city = db.Column(db.String(50), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     temperature = db.Column(db.Float, nullable=False)
#
#     def __repr__(self):
#         return '<City {} on Date {}>'.format(self.city, self.date)


def get_weather_data():
    cities = ['Toronto', 'Seattle']
    today = datetime.today().date()
    weather_data = []

    for city in cities:
        for i in range(10):
            date = today - timedelta(days=i)
            temperature = random.randint(-10, 30)
            weather_data.append({'city': city, 'date': date, 'temperature': temperature})

    return weather_data


def store_weather_data():
    weather_data = get_weather_data()

    for data in weather_data:
        weather = WeatherData(city=data['city'], date=data['date'], temperature=data['temperature'])
        db.session.add(weather)

    db.session.commit()


def get_city_weather(city):
    return WeatherData.query.filter_by(city=city).order_by(WeatherData.date.desc()).all()
