import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')  # Make sure your .env file has API_KEY, not api_key

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")  # Using the latest model name

prompt = """"
        Example : {{
  "Name": "Subhash Chandra Verma",
  "Style":"Tone": friendly bakwaas faaltu, making complex topics very complex, phrases like 'chaliye samajte hain'
  "joke": "Biwi se behas = Zindagi tahas-nahas"
}}

        """

print("Hitesh sir here (type exit to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Hanji! milte hai fir kabhi")
        break
    
    full_prompt = f"{prompt}\nQuestion: {user_input}\nHitesh's response:"

    try:
        response = model.generate_content(full_prompt)
        print("\nHitesh Sir:", response.text, "\n")
    except Exception as e:
        print("Error:", e)