from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class MovieBase(BaseModel):
    id: int
    title: str
    overview: str
    year: str
    rating: float
    category: CategoryBase
