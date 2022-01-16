# main.py
# Import FastAPI
import models
import uvicorn

import api

from fastapi import FastAPI

from database import db_engine

models.Base.metadata.create_all(bind=db_engine)

# Initialize the app
app = FastAPI()

app.include_router(api.router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return "Projekt na zaliczenie Algorytmy i Struktury Danych - Python \n Cezary Krawczyk WIT 2021/22"

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, workers=2, reload=True)