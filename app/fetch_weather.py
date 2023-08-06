import requests
import json
from app.models import WeatherData
from app import db
import time
from datetime import datetime


url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    "X-RapidAPI-Key": "062977c2b0msh1d566ef2fe25d47p11b9cajsnd30579cb0c74",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

params = [
    {"q": "44.389355,-79.690331"},  # Barrie
    {"q": "43.6532,-79.3832"},      # Toronto
    {"q": "49.2827,-123.1207"},     # Vancouver
    {"q": "51.0447,-114.0719"},     # Calgary
    {"q": "44.6488,-63.5752"}       # Halifax
]


def fetch_weather_for_all_locations():
    print("Scheduled task fetch_weather_for_all_locations executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    for location in params:
        fetch_weather(location)


def fetch_weather(location):
    response = requests.get(url, headers=headers, params=location)
    data = response.json()
    city = data['location']['name']
    temperature = data['current']['temp_c']
    a = data['location']['localtime']
    date = datetime.strptime(a, '%Y-%m-%d %H:%M').date()
    # date = time.strftime('%Y-%m-%d', b)

    # block duplicate data committing
    existing_record = WeatherData.query.filter_by(city=city, date=date)
    if existing_record.count() == 0:  # if no today temperature
        print("fetch weather_reports: %s %s %.1f" % (city, date, temperature))
        record = WeatherData(city=city, date=date, temperature=temperature)
        db.session.add(record)  # add a new record for today's weather
        db.session.commit()
