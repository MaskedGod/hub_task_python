import httpx


class ExternalAPIService:
    """Service to fetch data from external APIs asynchronously."""

    @staticmethod
    async def fetch_data(url: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                return {"data": response.text}
