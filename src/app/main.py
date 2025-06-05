from app.api.routes import irrigation_handler
from litestar import Litestar, get


@get("/")
async def root_handler() -> dict:
    return {"message": "Litestar is working!"}


app = Litestar(route_handlers=[root_handler, irrigation_handler])
