from flask import Blueprint, render_template, jsonify
from app.models import CityWeather

weather = Blueprint('weather', __name__)

@weather.route('/')
def index():
    city_weathers = CityWeather.query.order_by(CityWeather.date.desc()).limit(10).all()
    return render_template('index.html', city_weathers=city_weathers)

@weather.route('/api/weather')
def get_all_weather():
    city_weathers = CityWeather.query.all()
    return jsonify([cw.serialize for cw in city_weathers])

@weather.route('/api/weather/<start_date>/<end_date>')
def get_weather_by_range(start_date, end_date):
    city_weathers = CityWeather.query.filter(CityWeather.date.between(start_date, end_date)).all()
    return jsonify([cw.serialize for cw in city_weathers])

@weather.route('/api/weather/<int:id>')
def get_weather_by_id(id):
    city_weather = CityWeather.query.get(id)
    return jsonify(city_weather.serialize) if city_weather else ('', 404)
