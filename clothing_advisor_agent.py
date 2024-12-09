from openai import OpenAI
import os

class ClothingAdvisorAgent:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)

    def recommend_clothing(self, weather_info):
        # Use OpenAI to generate clothing recommendations
        system_prompt = "You are AI assistant for suggesting suitable clothing based on the weather information."
        prompt = f"Based on the following weather information: '{weather_info}', suggest suitable clothing."
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content