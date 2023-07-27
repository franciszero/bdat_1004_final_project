import requests
import json
from app.models import WeatherData
from app import db
import time

url = "https://weatherapi-com.p.rapidapi.com/current.json"
param1 = {"q": "44.389355,-79.690331"}
param2 = {"q": "44.389355,-79.690331"}
param3 = {"q": "44.389355,-79.690331"}

params = [param1, param2, param3]
headers = {
    "X-RapidAPI-Key": "062977c2b0msh1d566ef2fe25d47p11b9cajsnd30579cb0c74",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


def fetch_weather():
    # cities = ['Toronto', 'Seattle']
    for param in params:
        response = requests.get(url, headers=headers, params=param)
        data = response.json()
        city = data['location']['name']
        temperature = data['current']['temp_c']
        a = data['location']['localtime']
        b = time.strptime(a, '%Y-%m-%d %H:%M')
        date = time.strftime('%Y-%m-%d', b)

        # block duplicate data committing
        existing_record = WeatherData.query.filter_by(city=city, date=date)
        if existing_record.count() == 0:  # if no today temperature
            print("fetch weather_reports: %s %s %.1f" % (city, date, temperature))
            record = WeatherData(city=city, date=date, temperature=temperature)
            db.session.add(record)  # add a new record for today's weather
            db.session.commit()

