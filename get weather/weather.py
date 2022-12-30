import requests
from pprint import pprint
from datetime import datetime
import os
os.system('clear')

city = input('City: ')

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5bb44d0fa8e39e2339c9019d833d826&units=metric"
response = requests.get(url)

data = response.json()


city_description = data['weather'][0]
if city_description['main'] == 'Smoke':
    city_description_main = f'\U0001f324 {city_description["main"]}'

elif city_description['main'] == 'Clouds':
    city_description_main = f'\U0001F325 {city_description["main"]}'

elif city_description['main'] == 'Clear':
    city_description_main = f'\U00002600 {city_description["main"]}'

elif city_description['main'] == 'Tornado':
    city_description_main = f'\U0001F32A {city_description["main"]}'

elif city_description['main'] == 'Dust':
    city_description_main = f'\U0001F300 {city_description["main"]}'

elif city_description['main'] == 'Sand':
    city_description_main = f'\U0001F300 {city_description["main"]}'

elif city_description['main'] == 'Fog':
    city_description_main = f'\U0001F32B {city_description["main"]}'

elif city_description['main'] == 'Haze':
    city_description_main = f'\U0001F32B {city_description["main"]}'

elif city_description['main'] == 'Mist':
    city_description_main = f'\U0001F32B {city_description["main"]}'

elif city_description['main'] == 'Snow':
    city_description_main = f'\U000026C4 {city_description["main"]} Можно идти делать снеговика'

elif city_description['main'] == 'Rain':
    city_description_main = f'\U0001F327 {city_description["main"]} Сиди дома не высововайся'

elif city_description['main'] == 'Drizzle':
    city_description_main = f'\U0001F326 {city_description["main"]}'

elif city_description['main'] == 'Thunderstorm':
    city_description_main = f'\U0001F329 {city_description["main"]}'

else:
    city_description_main = city_description["main"]

city_name = data["name"]
city_temp = data["main"]['temp']
city_feels_like = data["main"]['feels_like']
city_humidity = data["main"]['humidity']
city_pressure = data["main"]['pressure']
city_wind = data['wind']['speed']
city_sunset = datetime.fromtimestamp(data["sys"]['sunset'])
city_sunrise = datetime.fromtimestamp(data["sys"]['sunrise'])
city_lingth_of_the_day = datetime.fromtimestamp(data["sys"]['sunset']) - datetime.fromtimestamp(data["sys"]['sunrise'])


information_weather = f"""
Погода в городе: {city_name}
Описание погоды: {city_description_main}
Температура: {city_temp}C
Ощушается: {city_feels_like}C
Влажность: {city_humidity}%
Давление воздуха: {city_pressure} гПа
Ветер: \U0001F32C{city_wind} м/с
Восход солнца: {city_sunrise}
Продолжительность дня: {city_lingth_of_the_day}
Закат солнца: {city_sunset}
"""
print(information_weather)