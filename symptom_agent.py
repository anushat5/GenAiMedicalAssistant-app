# agents/symptom_agent.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def diagnose_symptoms(symptoms: str) -> str:
    prompt = (
        f"You are an experienced medical assistant. A patient describes: {symptoms}. "
        f"Based on this, suggest the most likely condition. Keep your response to 1-2 sentences."
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
