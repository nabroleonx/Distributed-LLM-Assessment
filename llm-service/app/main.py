from fastapi import FastAPI

from .api import endpoints
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(endpoints.router)
