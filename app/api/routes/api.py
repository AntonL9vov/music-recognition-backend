from fastapi import APIRouter
from app.api.routes import tracks

router = APIRouter()
router.include_router(tracks.router, tags=["tracks"], prefix="/tracks")
