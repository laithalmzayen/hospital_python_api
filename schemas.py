from pydantic import BaseModel


class StaffModel(BaseModel):
    name: str
    role: str
