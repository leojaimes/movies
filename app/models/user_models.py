from typing import Optional
from pydantic import BaseModel
from datetime import datetime
 
class UserBase(BaseModel):
    name: str
    email: str
    dateOfBirth: Optional[datetime] = None 
