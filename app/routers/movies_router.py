from typing import List
from fastapi import APIRouter
from app.models.movies_models import MovieBase, CategoryBase

router = APIRouter()


@router.get("/movies", tags=["Movies"], response_model=List[MovieBase])
def getMovies():
    return [
        MovieBase(
            id=1,
            title="El retorno de la IA ",
            overview="En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
            year="2009",
            rating=7.8,
            category=CategoryBase(name="Action"),
        )
    ]
