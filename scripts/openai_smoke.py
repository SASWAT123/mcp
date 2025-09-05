import os
from openai import OpenAI

key = os.getenv("OPENAI_API_KEY")
assert key, "Set OPENAI_API_KEY in .env"

client = OpenAI()
resp = client.responses.create(
    model="gpt-4o-mini",  # small, cheap model for smoke
    input="Say 'ok' if you can read this.",
)
print(resp.output_text)
