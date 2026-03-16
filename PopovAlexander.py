from typing import Optional

from pydantic import BaseModel, Field

# Base user schema for routers input
class UserSchema(BaseModel):
    id: int
    nickname: str = Field(min_length=5, max_length=20)
    money: int = Field(ge=0)
    clan_id: Optional[int]


class UserLoginSchema(BaseModel):
    login: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=8, max_length=100)

# Schema for user registration
class UserRegisterSchema(UserLoginSchema):
    nickname: str = Field(min_length=5, max_length=20)
