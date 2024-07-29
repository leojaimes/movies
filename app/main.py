from fastapi import FastAPI
from app.routers import user_router
from app.routers import movies_router

app = FastAPI()

app.title = "My first Application with FASTAPI"
app.version = "1.0.0"


@app.get("/", tags=["Home"])
def home():
    return {"hello": "a todos!!"}


app.include_router(user_router.router)
app.include_router(movies_router.router)
