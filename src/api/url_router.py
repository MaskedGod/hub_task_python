from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

from src.services.url_shortener import URLShortenerService
from src.repositories.url_repository import URLRepository
from src.db.database import DependsSession
from src.db.schemas import URLRequest

router = APIRouter()


@router.post("/")
async def shorten_url(
    request: URLRequest, session: DependsSession
):
    """Shorten a URL or return an existing short URL."""
    repository = URLRepository(session)
    service = URLShortenerService(repository)

    original_url = request.url
    print(original_url)
    if not original_url:
        return {"error": "URL is required"}, 400

    short_url = await service.shorten_url(original_url)
    return JSONResponse(content={"short_url": short_url}, status_code=201)


@router.get("/{short_id}")
async def redirect_to_original_url(
    short_id: str, session: DependsSession
):
    """Redirect to the original URL using its short ID."""
    repository = URLRepository(session)
    original_url = await repository.get_original_url(short_id)

    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url=original_url, status_code=307)
