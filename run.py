from app import create_app, db
from app.fetch_weather import fetch_weather
from app.models import db, store_weather_data, get_city_weather

app = create_app()

is_debug = False

with app.app_context():
    db.create_all()

    print("Debug mode: %s" % is_debug)
    if is_debug:
        store_weather_data()
    else:
        fetch_weather()

    # 最后，我们可以获取并打印一些数据以检查它们是否正确地存储在了数据库中
    print(get_city_weather('Barrie'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
