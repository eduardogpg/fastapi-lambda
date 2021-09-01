from fastapi import HTTPException

from .responses import Response
from .responses import PayLoadResponse

def make_response(status_code=200, success=True, message='', data=None):
    return Response(
        code=status_code,
        payload=PayLoadResponse(
            success=success,
            message=message,
            data=data,
        )
    )


def bad_request(detail):
    raise HTTPException(status_code=404, detail=detail)
