from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

queries = [
    "Who won the election?",
    "What was the target?"
]

for query in queries:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ],
        temperature=0.2,
        max_tokens=300
    )
    print(f"\nQuery: {query}")
    print(f"Pure LLM Response: {response.choices[0].message.content}")
    print("-" * 60)