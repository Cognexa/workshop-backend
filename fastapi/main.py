#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import random

app = FastAPI()


# Define a Pydantic model for POST data validation
class DataModel(BaseModel):
    name: str
    age: int


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/get")
async def get_example():
    return {"message": "This is a GET response!"}


@app.post("/post")
async def post_example(data: DataModel):
    return data


@app.get("/hello")
async def hello():
    return {"message": "Hello World!"}


@app.get("/async/{num}")
async def async_test(num: int):
    import asyncio

    # async wait 1-2 second - simulating a slow DB query
    await asyncio.sleep(5 + random.random())
    return f":{num}:"
