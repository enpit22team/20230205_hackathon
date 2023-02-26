import os
import sys

import openai
from dotenv import load_dotenv

load_dotenv()
prompt = """
    「〇文章」の後に続く内容を「〇形式」の後のJSON形式でまとめてください。
    　"subtopics"は2つ以内、"content"は100文字以内、"summary"は300文字以内にしてください。
    〇形式

    {
        "topic":,
        "speaker":,
        "subtopics":[
            {
                "title":,
                "content":
            }
        ]

        ,
        "summary":
    }


    〇文章

"""


def pick(response:str) -> str:
    response = response.replace("\n", "")
    for i in range(len(response)):
        if response[i] == "{":
            break
    return response[i:]


def summary(query:str) -> str:
    query = prompt + query
    # print(query)
    openai.api_key = os.environ["CHATGPT_KEY"]
    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
    engine=model_engine,
    prompt=query,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )

    response = completion.choices[0].text

    return pick(response)