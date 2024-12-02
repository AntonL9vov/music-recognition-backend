from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def getFastApi(origins: list[str]):
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
