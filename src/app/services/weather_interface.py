from typing import Optional, Protocol


class IWeatherService(Protocol):
    def get_weather(self, location: str) -> Optional[float]: ...
