from datetime import datetime

from pydantic import BaseModel


class WeatherDTO(BaseModel):
    location: str
    temperature: float
    timestamp: datetime
