from litestar import post
from pydantic import BaseModel

from app.services.irrigation import calculate_optimal_irrigation


class IrrigationRequest(BaseModel):
    soil: dict
    weather: dict
    crop: dict


class IrrigationResponse(BaseModel):
    amount: float


@post("/irrigation")
async def irrigation_handler(data: IrrigationRequest) -> IrrigationResponse:
    amount = calculate_optimal_irrigation(data.soil, data.weather, data.crop)
    return IrrigationResponse(amount=amount)
