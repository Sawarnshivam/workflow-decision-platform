from fastapi import FastAPI
from api.request_api import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Workflow Decision Platform Running"}