from flask import Blueprint, render_template, jsonify
from app.models import WeatherData
from flask import request
from sqlalchemy import desc

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    city = request.args.get('city', default=None, type=str)
    if city is None:
        city = "Barrie"
    weather_data = WeatherData.query.filter_by(city=city).order_by(desc(WeatherData.date))
    html = render_template('index.html', weather_data=weather_data)
    return html
