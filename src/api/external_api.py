import httpx
from fastapi import APIRouter, HTTPException


from src.services.external_api import ExternalAPIService

router = APIRouter()


@router.get("/")
async def get_external_data(url: str):
    """Fetches data asynchronously from an external service."""
    try:
        data = await ExternalAPIService.fetch_data(url)
        return {"data": data}
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code, detail="Failed to fetch external data"
        )
