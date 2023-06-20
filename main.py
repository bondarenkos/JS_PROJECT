import requests
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WeatherForecast:
    def __init__(self, api_key):
        self.radio = None
        self.root = tk.Tk()
        self.label = None
        self.button = None
        self.entry = None
        self.radio_var = tk.StringVar()
        self.radio_var.set('km c')
        self.window_width = 800
        self.window_height = 600
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.title("Weather")
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
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lable = tk.Label(self.root, text="Want to plan a vacation?", font=("Arial", 25, 'bold'))
        self.lable.place(x=190, y=100)

        self.button = tk.Button(self.root, text="No", font=("Arial", 20), command=self.weather_day)
        self.button.place(x=210, y=250, width=150, height=50)

        self.button = tk.Button(self.root, text="Yes", font=("Arial", 20), command=self.show_weather_month)
        self.button.place(x=430, y=250, width=150, height=50)

        self.root.mainloop()

    def weather_day(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.button = tk.Button(self.root, text="Menu", font=("Arial", 15), command=self.build_giu)
        self.button.place(x=640, y=10, width=150, height=50)

        self.button = tk.Button(self.root, text="Show", font=("Arial", 15), command=self.show_weather_day)
        self.button.place(x=480, y=10, width=150, height=50)

        self.label = tk.Label(self.root, text="City: ", font=("Arial", 15))
        self.label.place(x=10, y=25)

        self.radio = tk.Radiobutton(self.root, text="km c", variable=self.radio_var, value='km', font=("Arial", 15))
        self.radio.place(x=350, y=10)

        self.radio = tk.Radiobutton(self.root, text="milles f", variable=self.radio_var, value='milles',
                                    font=("Arial", 15))
        self.radio.place(x=350, y=40)

        self.entry = tk.Entry(self.root, font=("Arial", 15))
        self.entry.place(x=100, y=25, width=220)

    def show_weather_day(self):
        location = self.entry.get()

        data = self.get_forecast_day(location)

        time = [d[-5] for d in list(data.keys())]
        temp = [data.get(d)[0] for d in data]
        wind = [data.get(d)[2] for d in data]
        pressure = [data.get(d)[4] for d in data]
        precip = [data.get(d)[7] for d in data]
        humidity = [data.get(d)[8] for d in data]
        feelslike = [data.get(d)[9] for d in data]
        vis = [data.get(d)[10] for d in data]
        print(time)
        print(temp)
        print(wind)
        print(pressure)
        print(precip)
        print(humidity)
        print(feelslike)
        print(vis)

    def show_weather_month(self):
        for widget in self.root.winfo_children():
            widget.destroy()


api_key = "112aff8f7d04491cb93204822231906"
location = "Wroclaw"

weather_forecast = WeatherForecast(api_key)
weather_forecast.build_giu()
