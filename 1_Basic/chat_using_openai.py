from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        { "role": "user", "content": "Hey There" } # Zero Shot Prompting
    ]
)

print(result.choices[0].message.content)

# Zero-shot prompting is when you ask the model to perform a task without giving it any examples — just clear instructions or a simple message.