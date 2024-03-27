import os
import openai
from dotenv import load_dotenv

class MethodClass:
    # Constants
    MODEL_NAME = "gpt-3.5-turbo-instruct"

    # Load OpenAI API key from environment variable
    @staticmethod
    def get_openai_key():
        load_dotenv()  # Load environment variables from .env file
        return os.getenv("OPENAI_API_KEY")

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
        except openai.error.OpenAIError as error:
            return "An error occurred while generating the story plot."

    # Generate story plot with scenes using OpenAI API
    @staticmethod
    def generate_story_plot_with_scenes(prompt):
        openai.api_key = MethodClass.get_openai_key()
        try:
            response = openai.Completion.create(
                engine=MethodClass.MODEL_NAME,
                prompt=prompt,
                max_tokens=1200,  # Increased token limit for longer output
                temperature=0.7,
            )
            story_output = response.choices[0].text.strip()
            # Split story into scenes based on line breaks
            scenes = story_output.split('\n\n')
            story_plot = scenes[0]  # First scene is usually the plot summary
            return story_plot, scenes[1:]  # Return plot summary and scenes
        except openai.error.OpenAIError as error:
            return "An error occurred while generating the story plot.", []
