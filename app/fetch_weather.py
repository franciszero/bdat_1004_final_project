import requests
import json
from app.models import WeatherData
from app import db
import time

url = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q": "44.389355,-79.690331"}
headers = {
    "X-RapidAPI-Key": "062977c2b0msh1d566ef2fe25d47p11b9cajsnd30579cb0c74",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


def fetch_weather():
    # cities = ['Toronto', 'Seattle']
    # for city in cities:
    #     # response = requests.get(f'https://api.weather.gov/gridpoints/{city}/10,10/forecast')
    #     # data = json.loads(response.text)
    #     # for forecast in data['current']['temp_c'][:10]:
    #     #     record = WeatherData(city=city, date=forecast['startTime'][:10], temperature=forecast['temperature'])
    #     #     db.session.add(record)
    #     # db.session.commit()

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    city = data['location']['name']
    temperature = data['current']['temp_c']
    a = data['location']['localtime']
    b = time.strptime(a, '%Y-%m-%d %H:%M')
    date = time.strftime('%Y-%m-%d', b)

    # block duplicate
    existing_record = WeatherData.query.filter_by(city=city, date=date)
    if existing_record.first() is None:
        print("fetch weather_reports: %s %s %.1f" % (city, date, temperature))
        record = WeatherData(city=city, date=date, temperature=temperature)
        db.session.add(record)
        db.session.commit()

