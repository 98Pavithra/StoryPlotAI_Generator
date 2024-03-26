import os
import openai
from dotenv import load_dotenv

class MethodClass:
    # Constants
    MODEL_NAME = "gpt-3.5-turbo-instruct"

    # Load OpenAI API key from environment variable
    @staticmethod
    def get_openai_key():
        key = os.environ.get("OPENAI_API_KEY")
        print(f"Retrieved API Key: {key}")  # Print retrieved key for debugging
        return key

    # Generate story plot using OpenAI API
    @staticmethod
    def generate_story_plot(prompt):
        openai.api_key = MethodClass.get_openai_key()
        try:
            response = openai.Engine("gpt-3.5-turbo-instruct").create_completion(  # Use updated API
                prompt=prompt,
                max_tokens=600,
                n=1,
                stop=None,
                temperature=0.7
            )
            print(f"Generated Prompt: {prompt}")  # Print prompt for debugging
            print(f"OpenAI Response: {response}")  # Print API response for debugging
            story_plot = response.choices[0].text.strip()
            return story_plot
        except openai.error.OpenAIError as error:
            print(f"OpenAI Error: {error}")  # Print specific error message
            # Consider retrying or logging for further analysis
            return "An issue occurred while generating the story plot. Please try again later."  # Informative message