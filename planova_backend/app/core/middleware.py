from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def add_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://81.180.202.99:3000"],  # sau ["*"] pentru toate originile
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
