from fastapi import Depends
from fastapi import APIRouter

from .responses import Response
from .responses import make_response

router = APIRouter(prefix='/transactions')

@router.get('/latest', response_model=Response)
async def latest(limit: int = 10):

    return make_response(message='business', data={
        'transactions': [
           
        ]
    })
