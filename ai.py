from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def chat_response(prompt: str):
    with client.responses.stream(
        model='gpt-3.5-turbo',
        max_output_tokens=50,
        temperature=0.7,
        input= prompt,
    ) as stream:
        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta  # send chunk