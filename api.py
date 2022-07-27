from msilib.schema import tables
from fastapi import FastAPI
from app import App

app= FastAPI()

tables= []
@app.get("/FRANI")
def hola():

    miApp=App()

    return{miApp.ingresardatos()}

@app.get('/tables')
def get_tablas():
    miApp=App()
    return{miApp.ingresardatos()}

