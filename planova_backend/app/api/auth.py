from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from datetime import timedelta
from jose import jwt, JWTError

from app.core.security import (
    get_password_hash, create_access_token, verify_password
)
from app.core.deps import get_db
from app.services import user_service
from app.utils.email_utils import send_confirmation_email  # Utility function for sending emails
#
import os
from dotenv import load_dotenv

# load local vars with override
load_dotenv(override=True)
#
SECRET_KEY = os.getenv("SECRET_KEY", "NaN")
ALGORITHM = os.getenv("ALGORITHM", "NaN")
BAKEND_URL_AUTH = os.getenv("BAKEND_URL_AUTH", "NaN")
FRONT_END_URL = os.getenv("FRONT_END_URL", "NaN")

router = APIRouter()


# ----------- Request Schemas -----------

class RegisterUser(BaseModel):
    username: str
    password: str
    email: EmailStr


class ResendEmailRequest(BaseModel):
    username: str
    email: EmailStr


class LoginUser(BaseModel):
    username: str
    password: str


# ----------- Register Route -----------

@router.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_db)):
    # Check if username is already taken
    existing_user = user_service.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    # Check if email is already taken
    existing_email = user_service.get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash the password and create a new user (inactive by default)
    hashed_password = get_password_hash(user.password)
    new_user = user_service.create_user(db, user.username, hashed_password, user.email)

    # Create an email confirmation token
    token_data = {"sub": user.email, "scope": "email_confirmation"}
    email_token = create_access_token(token_data, expires_delta=timedelta(hours=1))

    # Generate the confirmation URL for email verification
    confirm_url = f"{BAKEND_URL_AUTH}/confirm-email?token={email_token}"

    # Send confirmation email with the URL
    send_confirmation_email(user.email, confirm_url)

    return {
        "msg": "User registered successfully. Please confirm your email.",
    }


# ----------- Login Route -----------

@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):
    # Lookup user by username
    db_user = user_service.get_user_by_username(db, user.username)

    # If user not found or password invalid:
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Check if email is confirmed (user is active)
    if not db_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please confirm your email before logging in"
        )

    # Everything is ok — generate access token
    access_token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=timedelta(hours=1)
    )

    return {"access_token": access_token, "token_type": "bearer"}


# ----------- Confirm Email Route -----------

@router.get("/confirm-email")
def confirm_email(token: str, db: Session = Depends(get_db)):
    try:
        # Decode and validate the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Check if the token scope is for email confirmation
        if payload.get("scope") != "email_confirmation":
            raise HTTPException(status_code=400, detail="Invalid token scope")

        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=400, detail="Token does not contain email")
    except JWTError:
        # Token is invalid or expired
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    # Find user by email
    user = user_service.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_active:
        # If user is already active, redirect to frontend page
        return RedirectResponse(url=f"{FRONT_END_URL}/whois/home")

    # Activate user account
    user.is_active = True
    db.commit()

    # After successful confirmation, redirect to frontend page (e.g. home or login)
    return RedirectResponse(url=f"{FRONT_END_URL}/whois/login?confirmed=true")


# ----------- Resend Confirmation Email Route -----------

@router.post("/resend-confirmation")
def resend_confirmation(req: ResendEmailRequest, db: Session = Depends(get_db)):
    # Look up user by email or username
    user = None
    if req.email:
        user = user_service.get_user_by_email(db, req.email)
    elif req.username:
        user = user_service.get_user_by_username(db, req.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_active:
        raise HTTPException(status_code=400, detail="User already confirmed")

    # Create a new confirmation token
    token_data = {"sub": user.email, "scope": "email_confirmation"}
    email_token = create_access_token(token_data, expires_delta=timedelta(hours=1))

    confirm_url = f"{BAKEND_URL_AUTH}confirm-email?token={email_token}"

    # Send confirmation email again
    send_confirmation_email(user.email, confirm_url)

    return {"msg": "Confirmation email resent"}
