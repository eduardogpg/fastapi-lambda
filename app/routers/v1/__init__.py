from fastapi import APIRouter

from fastapi import status
from fastapi import Depends
from fastapi import HTTPException

from .responses import Response
from .responses import make_response

from .business import router as business_router
from .transactions import router as transactions_router

router = APIRouter(prefix='/v1')

@router.get('/ping', response_model=Response)
async def ping():
    return make_response(message='ping')


router.include_router(business_router)
router.include_router(transactions_router)
