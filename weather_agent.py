import requests
import datetime
import os

class WeatherAgent:
    def __init__(self):
        # Load API key from .env once during initialization
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    def get_weather(self, city):
        # Fetch weather data from OpenWeatherMap API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        # Check if the response contains the expected data
        if 'main' in data:
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            
            timestamp = data['dt']
            self.date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d %B %Y')
            self.updated_at = datetime.datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S')   

            return f"The temperature in {city} is {temperature}°C with {weather_description}."
        else:
            # Handle the case where the API response does not contain 'main'
            if 'message' in data:
                return f"Error: {data['message']}"
            else:
                return "Error: Unable to fetch weather data."