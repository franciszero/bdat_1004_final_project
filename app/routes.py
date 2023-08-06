from flask import Blueprint, render_template, jsonify
from app.models import WeatherData
from flask import request
from sqlalchemy import desc, asc
from datetime import datetime, timedelta

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    city = request.args.get('city', default=None, type=str)
    if city is None:
        city = "Barrie"

    # Query all cities from database
    all_cities = WeatherData.query.with_entities(WeatherData.city).distinct().all()
    cities = [c.city for c in all_cities]

    # read data from database
    # weather_data = WeatherData.query.filter_by(city=city).order_by(desc(WeatherData.date)).all()
    days_ago_14 = datetime.now() - timedelta(days=14)
    weather_data = WeatherData.query.filter_by(city=city).filter(WeatherData.date >= days_ago_14).order_by(
        asc(WeatherData.date)).all()

    # return an HTML page to web browser
    html = render_template('index.html', weather_data=weather_data, cities=cities, city=city)
    return html


@main.route('/get_weather_data', methods=['GET'])
def get_weather_data():
    city = request.args.get('city', default=None, type=str)
    if city is None:
        city = "Barrie"

    # Query data from database for the given city
    days_ago_14 = datetime.now() - timedelta(days=14)
    weather_data = WeatherData.query\
        .filter_by(city=city)\
        .filter(WeatherData.date >= days_ago_14)\
        .order_by(asc(WeatherData.date))\
        .all()

    # Here, I'm assuming you have a separate HTML template to display just the weather data
    html = render_template('weather_data.html', weather_data=weather_data)
    chart_data = [{'date': w.date.strftime('%Y-%m-%d'), 'temperature': w.temperature} for w in weather_data]

    return jsonify({
        'html': html,
        'chartData': chart_data
    })
