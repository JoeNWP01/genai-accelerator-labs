import os
from openai import OpenAI
from dotenv import load_dotenv

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



completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
