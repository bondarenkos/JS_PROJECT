import requests

api_key = "112aff8f7d04491cb93204822231906"
location = "London"
date=["2023-09-22", "2023-09-23", "2023-09-24", "2023-09-25", "2023-09-26", "2023-09-27"]

for d in range(1,30,1):
    url = f"http://api.weatherapi.com/v1/future.json?key=112aff8f7d04491cb93204822231906&q=Wroclaw&dt=2023-09-{d}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(f"2023-09-{d} {data['forecast']['forecastday'][0]['day']['maxtemp_c']} {data['forecast']['forecastday'][0]['day']['mintemp_c']}")
        print(data['forecast']['forecastday'][0]['hour'])
        for h in data['forecast']['forecastday'][0]['hour']:
            print(h['time'], h['temp_c'])
    else:
        print("Ошибка при получении прогноза погоды.")
