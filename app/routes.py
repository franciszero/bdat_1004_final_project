from flask import Blueprint, render_template, jsonify, redirect, url_for
from app.models import WeatherData
from flask import request
from sqlalchemy import desc

main = Blueprint('main', __name__)


# @main.route('/', methods=['GET'])  # e.g.: http://localhost:5001/?city=Barrie
# def index():
#     city = request.args.get('city', default=None, type=str)
#     if city is None:
#         city = "Barrie"
#
#     # read data from database
#     weather_data = WeatherData.query.filter_by(city=city).order_by(desc(WeatherData.date))
#     # return an HTML page to web browser
#     html = render_template('index.html', weather_data=weather_data)  # weather_data is the param that used in charts.js
#     return html


@main.route('/', methods=['GET', 'POST'])
def index():
    # If city is chosen from the dropdown, redirect to the URL with the chosen city.
    if request.method == 'POST':
        selected_city = request.form.get('city')
        return redirect(url_for('main.index', city=selected_city))
    else:
        city = request.args.get('city', default=None, type=str)
        if city is None:
            city = "Barrie"
        # read data from database
        weather_data = WeatherData.query.filter_by(city=city).order_by(desc(WeatherData.date)).all()

        # get all distinct cities for the dropdown list
        city_list = [c[0] for c in WeatherData.query.with_entities(WeatherData.city).distinct().all()]

        return render_template('index.html', weather_data=weather_data, city_list=city_list, selected_city=city)
