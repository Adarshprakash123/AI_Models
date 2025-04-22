import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
 
 
openai_client = OpenAI(api_key=openai_api_key)

# Configure Gemini
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Function to call Gemini
def call_gemini(prompt):
    response = gemini_model.generate_content(prompt)
    return response.text

# Intent detector
def detect_task(user_input):
    if "summarize" in user_input.lower():
        return "summarization"
    elif "generate" in user_input.lower() or "code" in user_input.lower():
        return "code_generation"
    else:
        return "both"

# Router function
def route_query(task_type, user_input):
    outputs = []

    if task_type == "summarization":
        outputs.append({ "step": "analyse", "content": "Detected summarization task. Routing to GPT-4." })
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{ "role": "user", "content": user_input }]
        )
        outputs.append({ "step": "result", "content": response.choices[0].message.content })

    elif task_type == "code_generation":
        outputs.append({ "step": "analyse", "content": "Detected code generation task. Routing to Gemini-1.5-flash." })
        response = call_gemini(user_input)
        outputs.append({ "step": "result", "content": response })

    elif task_type == "both":
        outputs.append({ "step": "analyse", "content": "Detected complex task. Using both GPT-4 and Gemini." })
        summary = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{ "role": "user", "content": user_input }]
        )
        code = call_gemini(user_input)
        outputs.append({ "step": "result", "content": f"Summary:\n{summary.choices[0].message.content}\n\nCode:\n{code}" })

    return outputs

# Example usage
user_input = "Summarize coding"
task = detect_task(user_input)
result = route_query(task, user_input)

for step in result:
    print(json.dumps(step, indent=2))
