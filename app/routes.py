from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan
from app.database import save_user, save_plan, update_plan, get_original_plan, get_user, get_all_users, delete_user

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page with input form"""
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: int = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    """Generate workout plan and nutrition tip"""
    
    # Save user to database
    save_user(user_id, username, age, weight, goal, intensity)
    
    # Generate workout plan using Gemini Pro
    workout_plan = generate_workout_gemini(goal, intensity)
    
    # Generate nutrition tip using Gemini Flash
    nutrition_tip = generate_nutrition_tip_with_flash(goal)
    
    # Save plan to database
    save_plan(user_id, workout_plan, nutrition_tip)
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": username,
        "user_id": user_id,
        "age": age,
        "weight": weight,
        "goal": goal,
        "intensity": intensity,
        "workout_plan": workout_plan,
        "nutrition_tip": nutrition_tip
    })

@router.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    """Update workout plan based on user feedback"""
    
    # Get original plan
    original_plan = get_original_plan(user_id)
    
    if not original_plan:
        return templates.TemplateResponse("result.html", {
            "request": request,
            "error": "User not found. Please generate a plan first."
        })
    
    # Update plan based on feedback
    updated_workout_plan = update_workout_plan(original_plan, feedback)
    
    # Generate new nutrition tip
    user = get_user(user_id)
    nutrition_tip = generate_nutrition_tip_with_flash(user.goal)
    
    # Save updated plan
    update_plan(user_id, updated_workout_plan)
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": user.username,
        "user_id": user.user_id,
        "age": user.age,
        "weight": user.weight,
        "goal": user.goal,
        "intensity": user.intensity,
        "workout_plan": updated_workout_plan,
        "nutrition_tip": nutrition_tip,
        "feedback_message": "Your workout plan has been updated based on your feedback!"
    })

@router.get("/view-all-users", response_class=HTMLResponse)
async def view_all_users(request: Request):
    """Admin view to see all users and their plans"""
    users = get_all_users()
    return templates.TemplateResponse("all_users.html", {
        "request": request,
        "users": users
    })

@router.post("/delete-user/{user_id}")
async def delete_user_route(user_id: str):
    """Delete a user from the database"""
    success = delete_user(user_id)
    return {"success": success}
