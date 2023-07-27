from app import app
from app.models import db, store_weather_data, get_city_weather

# 创建一个应用上下文
with app.app_context():
    # 然后，我们可以创建数据库表
    db.create_all()

    # 然后，我们可以调用 store_weather_data 函数来获取并存储天气数据
    store_weather_data()

    # 最后，我们可以获取并打印一些数据以检查它们是否正确地存储在了数据库中
    print(get_city_weather('Toronto'))

