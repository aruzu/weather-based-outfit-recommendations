from openai import OpenAI
import os

class VisualizationAgent:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)

    def generate_image(self, city, weather_info):
        # Use OpenAI's DALL·E to generate an image of the clothing
        prompt = f"Create an image of a lovely couple at the street of {city} at the following weather forecast: {weather_info}"
        response = self.client.images.generate(
            model="dall-e-3",
            #model="dall-e-2",
            prompt=prompt,
            n=1,
            quality="standard",
            size="1024x1024"
            #size="512x512"
        )
        image_url = response.data[0].url
        return image_url