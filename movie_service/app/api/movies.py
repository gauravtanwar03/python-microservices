from typing import List
from fastapi import Header, APIRouter

from app.api.models import Movie

fake_movie_db = [
    {
        "name": "Avengers: End Game",
        "plot": "Avengers tries to undo the snap done by Thanos, their greatest enemy!",
        "genres": ["Action", "Superhero", "SciFi", "Adventure"],
        "casts": ["Robert Downey Junior"],
    }
]

movies = APIRouter()


@movies.get("/", response_model=List[Movie])
async def index():
    return fake_movie_db


@movies.post("/", status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {"id": len(fake_movie_db) - 1}


@movies.put("/{id}")
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")


@movies.delete("/{id}")
async def delete_movie(id: int):
    movie_length = len(fake_movie_db)
    if 0 <= id <= movie_length:
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")
