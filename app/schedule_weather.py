import time
import schedule
import sys
import os

# Add the path of the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Now you can import fetch_weather module
from fetch_weather import fetch_weather_for_all_locations



# Schedule the weather fetching function to run every 60 seconds for 24 hours
for i in range(24 * 60):  # 24 hours * 60 minutes
    schedule.every(60).seconds.do(fetch_weather_for_all_locations, location)
    time.sleep(60)
