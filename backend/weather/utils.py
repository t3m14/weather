import json
import requests as req
import os

    
def get_coords_by_city_name(city_name: str) -> dict:
    city_name = city_name
    with open(os.path.dirname(os.path.realpath(__file__)) + '/cities.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    for city in data:
        if city['name'].lower().strip() == city_name.lower().strip():
            return city['coords']['lat'], city['coords']['lon']
    return None, None

def get_weather_from_yandex(city_name: str) -> dict:
    lat, lon = get_coords_by_city_name(city_name)
    result = dict()
    if lat == None or lon == None:
        return None
    request_url = f"https://api.weather.yandex.ru/v1/forecast?lat={lat}&lon={lon}&lang=ru"
    response = req.get(request_url, headers={'X-Yandex-API-Key': os.environ.get('YANDEX_API_KEY')})
    # response = req.get(request_url, headers={'X-Yandex-API-Key': '866075f9-31fb-4627-a540-8afff7b921ce'})
    result['url'] = response.json()["info"]["url"]
    result["wind_speed"] = response.json()["fact"]['wind_speed']
    result['city_name'] = response.json()['geo_object']['locality']['name']
    result["temparature"] = response.json()["fact"]['temp']
    result["pressure"] = response.json()["fact"]['pressure_mm']
    return result

w = get_weather_from_yandex('Москва')
print(w)