from pydantic import BaseModel


class URLRequest(BaseModel):
    url: str

    class Config:
        json_schema_extra = {"example": {"url": "https://www.example.com"}}
