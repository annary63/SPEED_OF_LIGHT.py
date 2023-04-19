SPEED_OF_LIGHT = 299792458 # скорость света в м/с
SUN_DISTANCE = 149600000000 # расстояние от Земли до Солнца в м

# вычисление времени, за которое свет достигнет Земли
time_to_reach_earth = SUN_DISTANCE / SPEED_OF_LIGHT
print(f"Время, за которое свет достигнет Земли: {time_to_reach_earth} секунд")

# вычисление времени, за которое свет пройдет 100 км в воздухе
distance_in_air = 100000 # 100 км в метрах
time_in_air = distance_in_air / SPEED_OF_LIGHT
print(f"Время, за которое свет пройдет {distance_in_air} м в воздухе: {time_in_air} секунд")
