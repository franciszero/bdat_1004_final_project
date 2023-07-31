import requests
import json
from app.models import WeatherData
from app import db
import time


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
    for location in params:
        fetch_weather(location)

def fetch_weather(location):
    try:
        response = requests.get(url, headers=headers, params=location)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        city = data['location']['name']
        temperature = data['current']['temp_c']
        a = data['location']['localtime']
        b = time.strptime(a, '%Y-%m-%d %H:%M')
        date = time.strftime('%Y-%m-%d', b)

        # Create a unique identifier based on the city, date, and coordinates
        # unique_id = f"{city}-{date}-{coordinates}"

        # Check if the record already exists in the database based on the unique identifier
        existing_record = WeatherData.query.filter_by(city=city, date=date)

        if existing_record.count() == ():
            print(f"Fetch weather report: {city}, {date}, {temperature}°C")
            # Assuming you have a 'unique_id' field in the WeatherData model
            record = WeatherData(city=city, date=date, temperature=temperature)
            db.session.add(record)  # add a new record for today's weather
            db.session.commit()
        else:
            print(f"Data already exists for {city}, {date}, {location}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get weather data: {e}")

    # Assuming you call the function fetch_weather() from another part of your application