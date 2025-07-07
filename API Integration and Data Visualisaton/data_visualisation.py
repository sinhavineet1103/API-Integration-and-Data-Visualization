import requests
import matplotlib.pyplot as plt
import seaborn as sns

# CONFIGURATION

# Replace with your OpenWeatherMap API key
API_KEY = "f328b6925654a08da660d38e137f747c"  # <-- Change this!

# City for weather data
CITY = "Deoghar,INDIA"

# Base URL for OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# FETCH DATA FROM API

def fetch_weather(city, api_key):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'Temperature (°C)': data['main']['temp'],
            'Feels Like (°C)': data['main']['feels_like'],
            'Min Temp (°C)': data['main']['temp_min'],
            'Max Temp (°C)': data['main']['temp_max'],
            'Humidity (%)': data['main']['humidity'],
            'Pressure (hPa)': data['main']['pressure'],
            'Wind Speed (m/s)': data['wind']['speed']
        }
        return weather
    else:
        print("Error fetching data:", data.get("message", "Unknown error"))
        return None

# CREATE VISUALIZATION

def plot_weather(weather_data, city_name):
    sns.set(style="whitegrid")

    keys = list(weather_data.keys())
    values = list(weather_data.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=values, y=keys, palette="viridis")
    plt.title(f" The Current Weather in {city_name}", fontsize=16)
    plt.xlabel("Value")
    plt.ylabel("Parameter")

    for index, value in enumerate(values):
        plt.text(value, index, f"{value}", va='center', fontsize=9)

    plt.tight_layout()
    plt.show()

# MAIN FUNCTION

if __name__ == "__main__":
    weather = fetch_weather(CITY, API_KEY)
    if weather:
        plot_weather(weather, CITY)
