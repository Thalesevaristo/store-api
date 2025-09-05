from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers.config import api_router


description = "Store API for stock control."

tags_metadata = [
    {
        "name": "Products",
        "description": "Operations for products.",
    },
]


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    summary="Microservice to simulate a store stock.",
    description=description,
    openapi_tags=tags_metadata,
    redoc_url=None,
    root_path=settings.ROOT_PATH,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"status": "ok"}
