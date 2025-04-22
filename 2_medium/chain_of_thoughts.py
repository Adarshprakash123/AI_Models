import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define system prompt
system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is interested in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}
"""


# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Make sure this model is available in your account
    system_instruction=system_prompt
)

# Start a chat session
chat = model.start_chat(history=[])

# Ask user for input
user_input = input("Enter your query: ")

while True:
    response = chat.send_message(user_input)
    text = response.text
    print(text)

    # Check if final step is "result"
    try:
        step_json = json.loads(text)
        if step_json.get("step") == "result":
            break
        user_input = input("Continue? (press Enter to proceed): ")
    except Exception as e:
        print("Error parsing response:", e)
        break
