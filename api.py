from fastapi import FastAPI, fastAPI
from app import App

app= FastAPI()

@app.get("/FRANI")
def hola():

    miApp=App()

    return{miApp.ingresardatos()}