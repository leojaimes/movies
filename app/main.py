from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import user_router
from app.routers import movies_router
from app.routers import products_router

app = FastAPI()

app.title = "My first Application with FASTAPI"
app.version = "1.0.0"


@app.get("/", tags=["Home"])
def home():
    return HTMLResponse("<h1>API Movies!!</h1>")


app.include_router(user_router.router)
app.include_router(movies_router.router)
app.include_router(products_router.router)
