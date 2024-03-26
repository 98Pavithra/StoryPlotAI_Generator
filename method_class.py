import os
import openai
from dotenv import load_dotenv

class MethodClass:
    # Constants
    MODEL_NAME = "gpt-3.5-turbo-instruct"

    # Load OpenAI API key from environment variable
    @staticmethod
    def get_openai_key():
        return os.environ.get("OPENAI_API_KEY")

    # Generate story plot using OpenAI API
    @staticmethod
    def generate_story_plot(prompt):
        openai.api_key = MethodClass.get_openai_key()
        try:
            response = openai.Completion.create(
                engine=MethodClass.MODEL_NAME,
                prompt=prompt,
                max_tokens=600,
                temperature=0.7,
            )
            
            story_plot = response.choices[0].text.strip()
            return story_plot
        except openai.OpenAIError as error:
            return "An error occurred while generating the story plot."