from app import create_app, db
from app.fetch_weather import fetch_weather, fetch_weather_for_all_locations
from app.models import db, store_weather_data, get_city_weather

app = create_app()

is_debug = False

with app.app_context():
    db.create_all()

    store_weather_data()
    fetch_weather_for_all_locations()

    print(get_city_weather('Barrie'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
