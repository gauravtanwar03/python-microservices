from fastapi import FastAPI, HTTPException
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


@app.post("/", status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {"id": len(fake_movie_db) - 1}


@app.put("/{id}")
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    return HTTPException(status_code=404, detail="Movie with given id not found")
