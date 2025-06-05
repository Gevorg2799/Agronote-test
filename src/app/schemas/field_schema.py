from pydantic import BaseModel


class FieldSchema(BaseModel):
    id: int
    name: str
