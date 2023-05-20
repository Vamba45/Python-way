from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
import cv2

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index.html")

@app.post("/")
# def hello(name = Body(embed=True)):
def post(data=Body()):
    name = data["name"]
    age = data["age"]
    photo = data["photo"]

    #код для обработки модели

    return {"message": f"{name}, ваш возраст - {age}, фото - {photo}"}

def predict_pollen(img_path):
    cls_names = []
    key = 0

    return cls_names[key]