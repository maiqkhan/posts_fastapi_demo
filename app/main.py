from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings
from . import models
from .database import engine
from .routers import posts, users, auth, vote


#models.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentails=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


