import requests
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
                vis_km = hour['vis_km']
                vis_miles = hour['vis_miles']
                weather[time] = (temp_c, temp_f, wind_kph, wind_mph, pressure_mb, pressure_in, precip_in,
                                 precip_mm, humidity, feelslike_c, feelslike_f, vis_km, vis_miles)
        return weather

    def build_giu(self):
        root = tk.Tk()
        window_width = 800
        window_height = 600
        root.geometry(f"{window_width}x{window_height}")
        root.title("Weather")

        lable = tk.Label(root, text="Chcesz zaplanować urlop?", font=("Arial", 25, 'bold'))
        lable.place(x=190, y=100)

        button1 = tk.Button(root, text="Nie", font=("Arial", 20))
        button1.place(x=210, y=250, width=150, height=50)

        button2 = tk.Button(root, text="Tak", font=("Arial", 20))
        button2.place(x=430, y=250, width=150, height=50)

        root.mainloop()


api_key = "112aff8f7d04491cb93204822231906"
location = "Wroclaw"

weather_forecast = WeatherForecast(api_key)
weather_forecast.build_giu()
