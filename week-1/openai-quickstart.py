from pydoc import text
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

"""
This script demonstrates how to generate a response using the OpenAI API.
"""

# --------------------------------------------------------------
# Load environment variables
# --------------------------------------------------------------

load_dotenv()

# --------------------------------------------------------------
# Initialize OpenAI client
# --------------------------------------------------------------

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BedTimeStory(BaseModel):
    story: str
    word_count: int
# --------------------------------------------------------------
# Generate a response
# --------------------------------------------------------------

# response = client.responses.create(
#     model="gpt-4.1", input="Write a one-sentence bedtime story about a unicorn."
# )
# This is new:
response = client.responses.parse(
    model="gpt-4.1",
    input=[
        {"role": "system", "content": "You are a bedtime storyteller. You will be given a topic and you will need to write a bedtime story about it and count the number of words in the story. The number of words in the story will exclude punctuation characters, blank space, and end-of-line characters"},
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn.",
        },
    ],
    text_format=BedTimeStory,
)

story = response.output_parsed

print(story.story)
print("The number of words in this story is: ", story.word_count)

