from weather_agent import WeatherAgent
from clothing_advisor_agent import ClothingAdvisorAgent
from visualization_agent import VisualizationAgent
from flask import Flask, render_template, request

app = Flask(__name__)  # Initialize the Flask app

class ContextSingleton:
    _instance = None
    _data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ContextSingleton, cls).__new__(cls)
        return cls._instance

    def initialize(self, **kwargs):
        self._data.update(kwargs)

    def get_context(self):
        return self._data

context = ContextSingleton()


@app.route('/', methods=['GET', 'POST'])  # Define a route for the home page
def main():
    city = request.form.get('city') if request.method == 'POST' else ""
    
    # If city is not provided, render the template without fetching weather data
    if not city:
        return render_template('index.html', context={})
    
    # Weather Agent
    weather_agent = WeatherAgent()
    weather_info = weather_agent.get_weather(city)

    date = weather_agent.date
    updated_at = weather_agent.updated_at

    # Clothing Advisor Agent
    clothing_advisor = ClothingAdvisorAgent()
    clothing_recommendation = clothing_advisor.recommend_clothing(weather_info)
    print(clothing_recommendation)
    
    # Visualization Agent
    visualization_agent = VisualizationAgent()
    image_url = visualization_agent.generate_image(city, weather_info)

    # Initialize context
    context.initialize(city=city, clothing_recommendation=clothing_recommendation, weather_info=weather_info, image_url=image_url, date=date, updated_at=updated_at)
    print(f"Generated image URL: {image_url}")

    # Render the template with the context
    print("Context: ", context.get_context())
    return render_template('index.html', **context.get_context())


if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode

