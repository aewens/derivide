from derivide import Derivide

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse, JSONResponse

from typing import Any, NewType, Union, Dict, List

KeyedDict = Dict[str, Any]
db = Derivide("flatfile", "/tmp/derivide.db")
app = FastAPI()

class Entry(BaseModel):
    path: str

class PutEntry(Entry):
    path: str
    value: Union[KeyedDict, list, str, bool, int, float]

@app.get("/api")
async def get_headers(req: Request):
    return dir(req)

@app.get("/api/raw/{attr}")
async def get_headers(attr: str, req: Request):
    return getattr(req, attr, None)

@app.get("/api/headers")
async def get_headers(req: Request):
    return req.headers

@app.get("/api/cookies")
async def get_cookies(req: Request):
    return req.cookies

@app.post("/api/cookies")
async def set_cookies(req: Request, res: Response):
    #res.set_cookie(**kwargs)
    return dict()

@app.get("/api/db")
async def get_db():
    with db:
        return db.all()

@app.post("/api/db/get")
async def get_db(entry: Entry):
    entries = tuple(entry.path.split("."))
    with db:
        return db.get(*entries)

@app.post("/api/db/put")
async def put_db(entry: PutEntry):
    entries = tuple(entry.path.split("."))
    with db:
        return db.put(*entries, value=entry.value)

@app.delete("/api/db/drop")
async def drop_db(entry: Entry):
    entries = tuple(entry.path.split("."))
    with db:
        return db.drop(*entries)
