from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

question = input("Ask your question: ")

final_prompt = f"""
Answer the following question clearly and accurately.

Question:
{question}

Answer:
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": final_prompt}
    ]
)

print("\nAnswer:")
print(response.choices[0].message.content)