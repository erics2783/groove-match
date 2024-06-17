import os
import openai
from openai import OpenAI

# Initialize the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

class OpenAiApi:

    def generate_response(self, system_prompt, user_prompt, model="gpt-3.5-turbo"):
        client = OpenAI()

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return completion.choices[0].message.content

