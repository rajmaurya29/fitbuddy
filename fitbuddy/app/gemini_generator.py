import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_workout_gemini(goal: str, intensity: str):
    """Generate a 7-day workout plan using AI"""
    
    prompt = f"""
    Create a detailed 7-day workout plan for someone with the following profile:
    - Fitness Goal: {goal}
    - Workout Intensity: {intensity}
    
    For each day, provide:
    - Day number and focus (e.g., Day 1: Full Body)
    - Warm-up (5-10 minutes)
    - Main workout with specific exercises, sets, and reps
    - Cooldown or recovery tip
    
    Format the response clearly with day-by-day breakdown.
    Make it practical, safe, and achievable.
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
        return f"Error generating workout plan: {str(e)}"
