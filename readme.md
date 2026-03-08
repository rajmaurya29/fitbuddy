# FitBuddy - AI Workout Generator

An AI-powered fitness application that generates personalized workout plans and nutrition tips using Google's Gemini AI models.

## Features

- **Personalized Workout Plans**: Generate custom workout routines based on fitness goals and intensity preferences
- **AI-Powered Recommendations**: Uses Gemini Pro for workout generation and Gemini Flash for nutrition tips
- **Adaptive Plans**: Update workout plans based on user feedback
- **User Management**: Store and track user profiles, goals, and workout history
- **Admin Dashboard**: View all users and their workout plans

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **AI Models**: Google Gemini Pro & Gemini Flash
- **Frontend**: Jinja2 Templates, HTML/CSS
- **Deployment**: Render (configured with Procfile and render.yaml)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fitbuddy
```

2. Create a virtual environment:
```bash
python -m venv fitbuddy-env
source fitbuddy-env/bin/activate  # On Windows: fitbuddy-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables (create `.env` file):
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The app will be available at `http://localhost:8000`

## Usage

1. **Generate Workout**: Enter your details (username, age, weight, fitness goal, intensity level)
2. **View Plan**: Get AI-generated workout plan and nutrition tips
3. **Submit Feedback**: Provide feedback to refine your workout plan
4. **Admin View**: Access `/view-all-users` to see all registered users

## API Endpoints

- `GET /` - Home page with input form
- `POST /generate-workout` - Generate personalized workout plan
- `POST /submit-feedback` - Update plan based on user feedback
- `GET /view-all-users` - Admin view of all users
- `POST /delete-user/{user_id}` - Delete user from database

## Project Structure

```
fitbuddy/
├── app/
│   ├── main.py                    # FastAPI application entry point
│   ├── routes.py                  # API route handlers
│   ├── database.py                # Database models and operations
│   ├── gemini_generator.py        # Gemini Pro workout generation
│   ├── gemini_flash_generator.py  # Gemini Flash nutrition tips
│   └── updated_plan.py            # Plan update logic
├── templates/                     # HTML templates
├── static/                        # Static files (images, CSS, JS)
├── requirements.txt               # Python dependencies
├── Procfile                       # Deployment configuration
└── fitbuddy.db                    # SQLite database

```

## Deployment

Configured for deployment on Render. The `Procfile` and `render.yaml` contain deployment settings.

