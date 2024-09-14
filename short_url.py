import json
import os
import string
import random
import motor
from motor import motor_asyncio
from fastapi import FastAPI, Request, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates
import aiofiles
from starlette.responses import RedirectResponse



app = FastAPI()

templates = Jinja2Templates(directory="templates")

client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb://{os.getenv('MONGO_USERNAME', 'root')}:{os.getenv('MONGO_PASSWORD', 'example')}@{os.getenv('MONGO_HOST', 'localhost')}:{os.getenv('MONGO_PORT', '27017')}/")
#client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://root:example@127.0.0.1:27017/')



@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")



@app.post("/")
async def get_url(url: Annotated[str, Form()]):
    short_url = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    new_doc = {"short_url": short_url, "long_url": url}
    await client["url_shortener"]["urls"].insert_one(new_doc)

    return {"result": short_url}


@app.get("/{short_url}")
async def say_hello(short_url: str):
    url_document = await client["url_shortener"]["urls"].find_one({"short_url": short_url})
    res_url = url_document["long_url"]
    return RedirectResponse(res_url)

