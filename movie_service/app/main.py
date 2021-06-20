from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_movie_db = [
    {
        "name": "Avengers: End Game",
        "plot": "Avengers tries to undo the snap done by Thanos, their greatest enemy!",
        "genres": ["Action", "Superhero", "SciFi", "Adventure"],
        "casts": ["Robert Downey Junior"],
    }
]


class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


@app.get("/", response_model=List[Movie])
async def index():
    return fake_movie_db
