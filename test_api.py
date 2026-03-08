#!/usr/bin/env python3
"""Test the Groq API integration"""

from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash

print("Testing Workout Generation...")
workout = generate_workout_gemini("weight loss", "medium")
print(f"✅ Workout generated: {len(workout)} characters")
print(f"Preview: {workout[:200]}...\n")

print("Testing Nutrition Tip Generation...")
tip = generate_nutrition_tip_with_flash("weight loss")
print(f"✅ Nutrition tip generated: {len(tip)} characters")
print(f"Tip: {tip}\n")

if "Error" not in workout and "Error" not in tip:
    print("🎉 All tests passed! Your FitBuddy app is working perfectly with Groq API!")
else:
    print("❌ Some tests failed. Check the errors above.")
