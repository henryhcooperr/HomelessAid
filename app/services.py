import os
import logging
import openai
from .utils import parse_resources

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def find_resources(problem, location):
    system_message = """
    You are a specialized assistant for supporting homeless individuals in the specified area.
    You are going to get a problem, and a location
    You will respond in the form of a list of resources that can help the individual with their problem in the specified location.
    In this form:
    Name: ....
    Address: .... 
    Hours: ....
    Phone: ....
    """

    user_message = f"Problem: {problem}. Location: {location}"
    print(f"Received problem: {problem}, location: {location}")  # Debug print

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        text = response.choices[0]['message']['content']


        return parse_resources(text)
        
    except Exception as e:
        logger.error(f"Failed to retrieve resources due to an error: {e}")
        return []
