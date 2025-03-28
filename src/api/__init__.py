from fastapi import APIRouter
from .url_router import router as url_router


router = APIRouter()

router.include_router(url_router, prefix="/urls", tags=["URL"])
