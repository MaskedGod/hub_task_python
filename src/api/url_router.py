from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse


from src.services.url_shortener import URLShortenerService
from src.repositories.url_repository import URLRepository
from src.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/")
async def shorten_url(request: dict, session: AsyncSession = Depends(get_session)):
    """Shorten a URL or return an existing short URL."""
    repository = URLRepository(session)
    service = URLShortenerService(repository)

    original_url = request.get("url")
    if not original_url:
        return {"error": "URL is required"}, 400

    short_url = await service.shorten_url(original_url)
    return {"short_url": short_url}


@router.get("/{short_id}")
async def redirect_to_original_url(
    short_id: str, session: AsyncSession = Depends(get_session)
):
    """Redirect to the original URL using its short ID."""
    repository = URLRepository(session)
    original_url = await repository.get_original_url(short_id)

    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url=original_url, status_code=307)
