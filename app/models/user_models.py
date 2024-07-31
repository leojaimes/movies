from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    id: Optional[str]
    name: str
    email: str
    dateOfBirth: Optional[datetime] = None
    password: Optional[str]
