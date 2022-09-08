from fastapi import FastAPI, Request

from typing import Union, List
from pydantic import BaseModel, HttpUrl


class Parent(BaseModel):
    id: int
    slug: str
    title: str


class Item(BaseModel):
    id: int
    slug: str
    title: str
    parent: Parent


class Geo(BaseModel):
    lat: float
    lng: float


class Community(BaseModel):
    id: int
    title: str
    slug: str
    parent_id: int
    parent: str
    is_del: bool = False
    state: Union[str, None] = None
    geo: Geo
    # lat: float
    # lng: float
