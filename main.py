import requests


class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_forecast_month(self, location, date):
        weather = {}
        for d in date:
            url = f"http://api.weatherapi.com/v1/future.json?key={self.api_key}&q={location}&dt={d}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                date = data['forecast']['forecastday'][0]['date']
                maxtemp_c = data['forecast']['forecastday'][0]['day']['maxtemp_c']
                maxtemp_f = data['forecast']['forecastday'][0]['day']['maxtemp_f']
                mintemp_c = data['forecast']['forecastday'][0]['day']['mintemp_c']
                mintemp_f = data['forecast']['forecastday'][0]['day']['mintemp_f']
                maxwind_mph = data['forecast']['forecastday'][0]['day']['maxwind_mph']
                maxwind_kph = data['forecast']['forecastday'][0]['day']['maxwind_kph']
                totalprecip_mm = data['forecast']['forecastday'][0]['day']['totalprecip_mm']
                totalprecip_in = data['forecast']['forecastday'][0]['day']['totalprecip_in']
                avgvis_km = data['forecast']['forecastday'][0]['day']['avgvis_km']
                avgvis_miles = data['forecast']['forecastday'][0]['day']['avgvis_miles']
                avghumidity = data['forecast']['forecastday'][0]['day']['avghumidity']
                weather[date] = (maxtemp_c, maxtemp_f, mintemp_c, mintemp_f, maxwind_mph, maxwind_kph,
                                 totalprecip_mm, totalprecip_in, avgvis_km, avgvis_miles, avghumidity)
        return weather


api_key = "112aff8f7d04491cb93204822231906"
location = "Wroclaw"
date = []
year = 2023
month = 7
for day in range(1, 5, 1):
    date.append(f'{year}-{month}-{day}')
weather_forecast = WeatherForecast(api_key)
weather_forecast.get_forecast_month(location, date)
data = {}
data['13'] = (1, 2, 3, 4)
data['3'] = ("2", 2, 3, 4)
print(list(data.values()))
