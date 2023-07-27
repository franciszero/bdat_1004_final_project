from flask import Blueprint, render_template
from app.models import WeatherData
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = WeatherData.query.all()
    jstr = [ob.serialize for ob in data]
    html = render_template('index.html', weather_data=jstr)
    return html
