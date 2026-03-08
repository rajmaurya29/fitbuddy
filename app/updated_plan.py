import os
import requests
from dotenv import load_dotenv

load_dotenv()

def update_workout_plan(original_plan: str, feedback: str):
    """Update workout plan based on user feedback using AI"""
    
    prompt = f"""
    Here is the original workout plan:
    {original_plan}
    
    The user has provided the following feedback:
    {feedback}
    
    Please update the workout plan based on this feedback while maintaining:
    - The 7-day structure
    - Proper warm-up and cooldown
    - Safe and effective exercises
    - Clear formatting
    
    Provide the complete updated plan.
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
                "max_tokens": 2000
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error updating workout plan: {str(e)}"
