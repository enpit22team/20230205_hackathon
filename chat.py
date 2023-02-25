import os

import openai
from dotenv import load_dotenv

load_dotenv()

with open("sample.md", encoding="utf-8", mode="r") as f:
    prompt = f.read()

openai.api_key = os.environ["CHATGPT_KEY"]
model_engine = "text-davinci-003"

completion = openai.Completion.create(
engine=model_engine,
prompt=prompt,
max_tokens=1024,
n=1,
stop=None,
temperature=0.5,
)

response = completion.choices[0].text
print(response)