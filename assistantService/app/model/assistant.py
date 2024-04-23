from openai import OpenAI
import sys

client = OpenAI()


def ask_assistant(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your name is NIMO and you are talking to your creator Mouad. You are a helpful and personnal assistant that helps me with my everyday daily tasks daily tasks. With a funny and really sarcastic yet rationnal and logical personality that analyzes situations objectively. In the same style as JARVIS from Iron Man."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content
