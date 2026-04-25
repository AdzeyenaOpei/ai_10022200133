from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def log(stage, content):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n[{timestamp}] ---- {stage.upper()} ----")
    print(content)
    print("-" * 60)

def generate_response(prompt):

    # Stage 6 - Log final prompt sent to LLM
    log("STAGE 6 - FINAL PROMPT SENT TO LLM", prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful academic RAG assistant. Answer only from the provided context and be direct."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    # Stage 7 - Log final response
    log("STAGE 7 - FINAL RESPONSE GENERATED", 
        response.choices[0].message.content)

    return response.choices[0].message.content