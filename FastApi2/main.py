from typing import List, Optional

from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(..., min_length=3, max_length=50, regex="[a-z]")):
    results = {"Item_id": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get('/')
async def home(request : Request):
    return templates.TemplateResponse('home.html', {
        "request": request
    })