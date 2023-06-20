import requests


class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_forecast_month(self, location, date):
        weather = {}
        for day in date:
            url = f"http://api.weatherapi.com/v1/future.json?key={self.api_key}&q={location}&dt={day}"
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

    def get_forecast_day(self, location):
        weather = {}
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={location}&days=1&aqi=no&alerts=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for hour in data["forecast"]['forecastday'][0]['hour']:
                print(hour)
                time = hour['time']
                temp_c = hour['temp_c']
                temp_f = hour['temp_f']
                wind_mph = hour['condition']['wind_mph']
                wind_kph = hour['condition']['mintemp_f']
                pressure_mb = hour['condition']['totalprecip_mm']
                pressure_in = hour['condition']['totalprecip_in']
                precip_mm = hour['condition']['avgvis_km']
                precip_in = hour['condition']['avgvis_miles']
                humidity = hour['condition']['humidity']
                feelslike_c = hour['condition']['feelslike_c']
                feelslike_f = hour['condition']['feelslike_f']
                vis_km = hour['condition']['vis_km']
                vis_miles = hour['condition']['vis_miles']
                weather[time] = (temp_c, temp_f, wind_kph, wind_mph, pressure_mb, pressure_in, precip_in,
                                 precip_mm, humidity, feelslike_c, feelslike_f, vis_km, vis_miles)
        return weather


api_key = "112aff8f7d04491cb93204822231906"
location = "Wroclaw"

weather_forecast = WeatherForecast(api_key)
# weather_forecast.get_forecast_month(location, date)
weather_forecast.get_forecast_day(location)
