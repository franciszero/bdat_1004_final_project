import os
import time
from threading import Thread

import schedule

from app import create_app
from app.fetch_weather import fetch_weather_for_all_locations
from app.models import db, store_weather_data, get_city_weather

app = create_app()

with app.app_context():
    db.create_all()

    store_weather_data()  # generate random test data
    fetch_weather_for_all_locations()  # fetch real world data from weather API

    print(get_city_weather('Barrie'))


def run_scheduler(a_p_p):
    with a_p_p.app_context():
        print("Scheduled task fetch_weather_for_all_locations executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))
        schedule.every(4).hours.do(fetch_weather_for_all_locations)  # Fetch weather data regularly
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    # Start the scheduler in a separate thread
    scheduler_thread = Thread(target=run_scheduler, args=(app,))
    scheduler_thread.start()

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
