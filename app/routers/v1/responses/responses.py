
from typing import Union
from typing import Optional
from pydantic import BaseModel

class PayLoadResponse(BaseModel):
    success: str
    message: str
    data: Union[None, dict]


class Response(BaseModel):
    code: int
    payload: PayLoadResponse
