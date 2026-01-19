"""
Authentication API routes
"""

from fastapi import APIRouter, HTTPException, status
from loguru import logger
import uuid

from app.models.user import UserCreate, UserLogin, UserResponse, User
from app.services.auth_service import (
    get_password_hash,
    verify_password,
    create_access_token
)
from app.services.database import supabase

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user_data: UserCreate):
    """Register a new user"""
    try:
        # Check if user already exists
        existing = supabase.table('users').select('*').eq('email', user_data.email).execute()
        
        if existing.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create user
        user_id = str(uuid.uuid4())
        hashed_password = get_password_hash(user_data.password)
        
        new_user = {
            'id': user_id,
            'email': user_data.email,
            'name': user_data.name,
            'password': hashed_password
        }
        
        response = supabase.table('users').insert(new_user).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user"
            )
        
        # Create access token
        access_token = create_access_token(data={"sub": user_id})
        
        user = User(**response.data[0])
        
        return UserResponse(
            user=user,
            access_token=access_token
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Signup error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/login", response_model=UserResponse)
async def login(credentials: UserLogin):
    """Login user"""
    try:
        # Find user
        response = supabase.table('users').select('*').eq('email', credentials.email).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        user_data = response.data[0]
        
        # Verify password
        if not verify_password(credentials.password, user_data['password']):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Create access token
        access_token = create_access_token(data={"sub": user_data['id']})
        
        user = User(**user_data)
        
        return UserResponse(
            user=user,
            access_token=access_token
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
