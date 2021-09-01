from fastapi import Depends
from fastapi import APIRouter

from .responses import Response
from .responses import bad_request
from .responses import make_response

router = APIRouter(prefix='/business')

@router.get('/total', response_model=Response)
async def total(byStatus: str = ''):
    return make_response(message='business', data={
        'total': 10
    })


@router.get('/latest', response_model=Response)
async def latest(limit: int = 10):

    return make_response(message='business', data={
        'businesses': [
            
        ]
    })
