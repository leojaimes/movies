
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class MovieBase(BaseModel):
    name: str
    category: CategoryBase

