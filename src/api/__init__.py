from fastapi import APIRouter
from .url_router import router as url_router
from .external_api import router as external_api_router


router = APIRouter()

router.include_router(url_router, prefix="/urls", tags=["URL"])
router.include_router(
    external_api_router, prefix="/external-data", tags=["External data"]
)
