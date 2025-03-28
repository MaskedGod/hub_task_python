import hashlib


from src.repositories.url_repository import URLRepository
from src.config.settings import settings


class URLShortenerService:
    def __init__(self, repository: URLRepository):
        self.repository = repository

    async def shorten_url(self, original_url: str) -> str:
        existing_short_url = await self.repository.get_existing_short_url(original_url)
        if existing_short_url:
            return existing_short_url

        short_id = hashlib.md5(original_url.encode()).hexdigest()[:6]
        short_url = f"{settings.BASE_URL}/{short_id}"

        await self.repository.save_url(original_url, short_id, short_url)
        return short_url
