import os
import openai
from openai import OpenAI

class OpenAiApi:
    def __init__(self, api_key):
        self.__api_key = api_key

    def generate_response(self, system_prompt, user_prompt, model="gpt-3.5-turbo"):
        client = OpenAI(api_key=self.__api_key)

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return completion.choices[0].message.content

