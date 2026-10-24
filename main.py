from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello DSC5003 zzzworld!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{item_id}/name/{name}")
def read_item_name(item_id: int, name: str):
    return {"item_id": item_id, "name": name}