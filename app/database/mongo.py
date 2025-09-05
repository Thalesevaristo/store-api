from pymongo import AsyncMongoClient

from app.core.config import settings


class MongoClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self._client: AsyncMongoClient | None = None

    def connect(self) -> AsyncMongoClient:
        if self._client is None:
            self._client = AsyncMongoClient(self.url)
        return self._client

    async def close(self) -> None:
        if self._client is not None:
            await self._client.close()
            self._client = None


db_client = MongoClient(settings.DATABASE_URL)
