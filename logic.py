from datetime import datetime
import requests


class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_forecast_month(self, location, month):
        # Retrieve weather forecast for a specific location and month
        current_month = datetime.now().month
        if current_month >= month:
            year = 2024
        else:
            year = 2023
        date = [f"{year}-{month}-{i}" for i in range(1, 32, 1)]
        weather = {}
        for day in date:
            url = f"http://api.weatherapi.com/v1/future.json?key={self.api_key}&q={location}&dt={day}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Extract relevant weather information
                date = data['forecast']['forecastday'][0]['date']
                maxtemp_c = data['forecast']['forecastday'][0]['day']['maxtemp_c']
                maxtemp_f = data['forecast']['forecastday'][0]['day']['maxtemp_f']
                mintemp_c = data['forecast']['forecastday'][0]['day']['mintemp_c']
                mintemp_f = data['forecast']['forecastday'][0]['day']['mintemp_f']
                totalprecip_mm = data['forecast']['forecastday'][0]['day']['totalprecip_mm']
                totalprecip_in = data['forecast']['forecastday'][0]['day']['totalprecip_in']
                weather[date] = (maxtemp_c, maxtemp_f, mintemp_c, mintemp_f, totalprecip_mm, totalprecip_in)
        return weather

    def get_forecast_day(self, location):
        # Retrieve weather forecast for a specific location for the next day
        weather = {}
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={location}&days=1&aqi=no&alerts=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for hour in data["forecast"]['forecastday'][0]['hour']:
                time = hour['time']
                temp_c = hour['temp_c']
                temp_f = hour['temp_f']
                wind_mph = hour['wind_mph']
                wind_kph = hour['wind_kph']
                pressure_mb = hour['pressure_mb']
                pressure_in = hour['pressure_in']
                precip_mm = hour['precip_mm']
                precip_in = hour['precip_in']
                humidity = hour['humidity']
                feelslike_c = hour['feelslike_c']
                feelslike_f = hour['feelslike_f']
                weather[time] = (temp_c, temp_f, wind_kph, wind_mph, pressure_mb, pressure_in, precip_in,
                                 precip_mm, humidity, feelslike_c, feelslike_f)
        return weather


api_key = "112aff8f7d04491cb93204822231906"
weather_forecast = WeatherForecast(api_key)
