from sqlalchemy import select


from src.db.models import URLModel


class URLRepository:
    def __init__(self, session):
        self.session = session

    async def save_url(self, original_url: str, short_id: str, short_url: str):
        new_url = URLModel(id=short_id, original_url=original_url, short_url=short_url)
        self.session.add(new_url)
        await self.session.commit()

    async def get_original_url(self, short_id: str):
        stmt = select(URLModel).where(URLModel.id == short_id)
        result = await self.session.execute(stmt)
        url_entry = result.scalars().first()
        return url_entry.original_url if url_entry else None

    async def get_existing_short_url(self, original_url: str):
        stmt = select(URLModel.short_url).where(URLModel.original_url == original_url)
        result = await self.session.execute(stmt)
        return result.scalars().first()
