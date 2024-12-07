from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid

class UserClass(BaseModel):
    id: int = 0
    name: str = None

_USER_LIST = []

app = FastAPI()

@app.get("/init")
def init():
    global _USER_LIST
    ls = []
    for i in range(1, 18):
        u = UserClass()
        u.id = i
        u.name = f'name_{i}'
        ls.append(u)
    _USER_LIST = ls
    return _USER_LIST

@app.get("/list")
def id_list():
    return _USER_LIST

@app.post("/create")
def new_user(user: UserClass):
    global _USER_LIST
    print(f"User:{user.id}--{user.name}")
    _USER_LIST.append(user)
    return{"message":f"User:{user.id}--{user.name}"}

@app.delete("/del")
def del_by_id(id: int):
    global _USER_LIST
    for user in _USER_LIST:
        if user.id == id:
            _USER_LIST.remove(user)
            print(f"del user = {user.name}")
            return user
    return{"message -- NOT FOUND"}

@app.put("/edit")    
def edit_user(user: UserClass):
    global _USER_LIST
    for u in _USER_LIST:
        if u.id == user.id:
            index = _USER_LIST.index(u)
            _USER_LIST[index] = user
            return _USER_LIST[index]
            #_USER_LIST.index(user)
