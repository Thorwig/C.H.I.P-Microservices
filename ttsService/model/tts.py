from pathlib import Path
from openai import OpenAI
client = OpenAI()


def get_audio(message):

    speech_file_path = "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=message
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path
