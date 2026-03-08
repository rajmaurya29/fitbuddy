from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./fitbuddy.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    username = Column(String)
    age = Column(Integer)
    weight = Column(Integer)
    goal = Column(String)
    intensity = Column(String)
    original_plan = Column(Text)
    updated_plan = Column(Text, nullable=True)
    nutrition_tip = Column(Text)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_user(user_id: str, username: str, age: int, weight: int, goal: str, intensity: str):
    db = SessionLocal()
    try:
        user = User(
            user_id=user_id,
            username=username,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()

def save_plan(user_id: str, workout_plan: str, nutrition_tip: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user:
            user.original_plan = workout_plan
            user.nutrition_tip = nutrition_tip
            db.commit()
            return True
        return False
    finally:
        db.close()

def update_plan(user_id: str, updated_plan: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user:
            user.updated_plan = updated_plan
            db.commit()
            return True
        return False
    finally:
        db.close()

def get_original_plan(user_id: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        return user.original_plan if user else None
    finally:
        db.close()

def get_user(user_id: str):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.user_id == user_id).first()
    finally:
        db.close()

def get_all_users():
    db = SessionLocal()
    try:
        return db.query(User).all()
    finally:
        db.close()

def delete_user(user_id: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
    finally:
        db.close()
