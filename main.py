from fastapi import FastAPI
from routers.api import router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Math Microservice API")
app.include_router(router)