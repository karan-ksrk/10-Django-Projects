from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "deep Learning FTW!"}
    if model_name.value == "resnet":
        return {"model_name": model_name, "message": "deep Learning FTW!"}
    if model_name == ModelName.lenet.value:
        return {"model_name": model_name, "message": "deep Learning FTW!"}

####Path parameters containing paths
@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}