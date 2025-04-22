import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Load API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
# Zero-shot prompting: just give it a message
response = model.generate_content("Hey there")

# Print the response
print(response.text)
