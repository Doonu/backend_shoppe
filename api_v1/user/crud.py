from typing import Optional

from fastapi import Form, Depends
from pydantic import EmailStr
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.auth.utils import hash_password
from core.models import User, db_helper


async def get_users(session: AsyncSession) -> list[User]:
    state = select(User).order_by(User.id)
    result: Result = await session.execute(state)
    users = result.scalars().all()
    return list(users)


async def get_item_users(session: AsyncSession, user_id: int) -> Optional[User]:
    return await session.get(User, user_id)


async def get_item_users_by_email(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    email: EmailStr = Form(),
) -> Optional[User]:
    state = select(User).where(User.email == email)
    user = await session.scalars(state)
    return next(user, None)


async def create_user(email: EmailStr, password: str, session: AsyncSession) -> User:
    user = User(email=email, password=hash_password(password_user=password))
    session.add(user)
    await session.commit()
    return user
