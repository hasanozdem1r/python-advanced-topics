"""
This script is created to show basics of FastApi
"""
# package imports
from typing import List
from fastapi import FastAPI

# app initialize
app = FastAPI()

dummy_data: List[int] = [i for i in range(100)]


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id": course_id}


@app.get("/my/page/items/")
async def read_item(page: int = 0, limit: int = 0, skip: int = 1):
    return dummy_data[page * 10:page * 10 + limit:skip]


"""
Imports
    pip install fastapi
    pip install uvicorn
Running application
    uvicorn fast_api_practice:app --reload
"""
