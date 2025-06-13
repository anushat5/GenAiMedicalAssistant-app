# agents/advice_agent.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def give_advice(condition: str) -> str:
    prompt = (
        f"You are a lifestyle medicine expert. Suggest basic diet, physical activity, and self-care tips "
        f"for a person diagnosed with: {condition}. Make it easy to follow. 4-5 bullet points max."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
