# Weather Forecast Application

The Weather Forecast application is a graphical user interface (GUI) tool that provides weather forecast information for a specified location. It utilizes the WeatherAPI service to retrieve weather data and presents it in a user-friendly manner using graphs and charts.

## Requirements

To run the Weather Forecast application, you need to have the following installed:

- Python 3
- `requests` library
- `tkinter` library
- `matplotlib` library

You can install the required libraries using the following command:

pip install requests tkinter matplotlib



## Usage

1. Obtain an API key from the [WeatherAPI](https://www.weatherapi.com/) website. (Note: The API key used in the provided code may not be valid anymore.)
2. Copy the provided code into a Python file or create a new Python file and paste the code.
3. Replace the placeholder API key in the `api_key` variable with your own API key.
4. Save the file and run it using the Python interpreter.
5. The Weather Forecast GUI will appear.
6. Choose whether you want to plan a vacation or not by clicking the "Yes" or "No" button.
7. Depending on your choice, you will be directed to either the daily or monthly weather forecast GUI.
8. Enter the desired city and select the unit system (km/c or miles/f).
9. Click the "Show" button to display the weather forecast.
10. The weather information will be shown in graphs and charts.

Note: The provided code assumes a screen resolution of 1000x800 pixels. You can adjust the window size in the `window_width` and `window_height` variables if needed.

## Features

- Weather forecast for a specific day: Displays temperature, wind speed, atmospheric pressure, precipitation, humidity, and feeling temperature for each hour of the day.
- Weather forecast for a specific month: Displays maximum and minimum temperatures and precipitation for each day of the selected month.

## Limitations

- The WeatherAPI service has usage limitations, including a limited number of API calls per day. Make sure to check the limitations and usage terms on the WeatherAPI website.
- The provided code retrieves weather forecast data from the WeatherAPI service. If the service is unavailable or the API key is invalid, the application may not work properly.
- The graphical representation of weather data is limited to basic line charts. Additional visualization options could be implemented for a more comprehensive weather analysis.

