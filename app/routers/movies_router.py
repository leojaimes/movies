from typing import List
from fastapi  import APIRouter
from app.models.movies_models import MovieBase, CategoryBase
router = APIRouter()

@router.get("/movies", tags=["Movies"], response_model=List[MovieBase] )
def getMovies():
    return [
        MovieBase(
            category = CategoryBase(
                name= "Category 1"
            ),
            name="El retorno de la IA "
        )
    ]