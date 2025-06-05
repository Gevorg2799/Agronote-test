from typing import List, Protocol

from app.models.weather_orm import Weather


class IWeatherRepository(Protocol):
    def get_all(self) -> List[Weather]: ...

    def get_by_location(self, location: str) -> Weather | None: ...
