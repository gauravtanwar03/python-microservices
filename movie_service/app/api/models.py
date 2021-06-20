from typing import List, Optional
from pydantic import BaseModel


class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


class MovieOut(BaseModel):
    id: int


class MovieUpdate(BaseModel):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts: Optional[List[str]] = None
