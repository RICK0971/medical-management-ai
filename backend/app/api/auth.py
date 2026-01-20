"""
Authentication API routes
"""

from fastapi import APIRouter, HTTPException, status, Depends
from loguru import logger
import uuid

from app.models.user import UserCreate, UserLogin, UserResponse, User
from app.services.auth_service import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user
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
            'password_hash': hashed_password  # Changed from 'password' to 'password_hash'
        }
        
        response = supabase.table('users').insert(new_user).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user"
            )
        
        # Create access token
        access_token = create_access_token(data={"sub": user_id})
        
        # Create User object (map password_hash to password for the model)
        user_dict = response.data[0].copy()
        user_dict['password'] = user_dict.pop('password_hash')
        user = User(**user_dict)
        
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
            detail=str(e)
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
        
        # Verify password (use password_hash from database)
        password_hash = user_data.get('password_hash') or user_data.get('password')
        if not verify_password(credentials.password, password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Create access token
        access_token = create_access_token(data={"sub": user_data['id']})
        
        # Create User object (map password_hash to password for the model)
        user_dict = user_data.copy()
        if 'password_hash' in user_dict:
            user_dict['password'] = user_dict.pop('password_hash')
        user = User(**user_dict)
        
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
            detail=str(e)
        )

@router.get("/me", response_model=User)
async def get_me(current_user: dict = Depends(get_current_user)):
    """Get current user"""
    try:
        response = supabase.table('users').select('*').eq('id', current_user['id']).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        user_dict = response.data[0].copy()
        if 'password_hash' in user_dict:
            user_dict['password'] = user_dict.pop('password_hash')
        
        return User(**user_dict)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
