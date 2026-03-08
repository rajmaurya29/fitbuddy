import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_nutrition_tip_with_flash(goal: str):
    """Generate a concise nutrition tip using AI"""
    
    prompt = f"""
    Provide a concise, practical nutrition tip for someone whose fitness goal is: {goal}
    
    Keep it brief (2-3 sentences), actionable, and focused on:
    - Protein intake
    - Hydration
    - Recovery nutrition
    - General healthy eating habits
    
    Make it specific and helpful.
    """
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 500
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating nutrition tip: {str(e)}"
