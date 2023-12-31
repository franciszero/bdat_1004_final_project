from app import db
from datetime import datetime, timedelta
import random


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), index=True)
    date = db.Column(db.Date, index=True)
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


def store_weather_data():
    cities = ['Barrie', 'Toronto']
    today = datetime.today().date()

    for city in cities:
        for i in range(1, 10):  # fake history city temperature
            date = today - timedelta(days=i)
            temperature = random.randint(-10, 30)

            existing_record = WeatherData.query.filter_by(city=city, date=date)
            if existing_record.first() is None:
                print("fetch weather_reports: %s %s %.1f" % (city, date, temperature))
                record = WeatherData(city=city, date=date, temperature=temperature)
                db.session.add(record)
    db.session.commit()


def get_city_weather(city):
    return WeatherData.query.filter_by(city=city).order_by(WeatherData.date.desc()).all()
