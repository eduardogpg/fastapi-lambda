import os
from mangum import Mangum​
from fastapi import FastAPI
​
stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"
​
app = FastAPI(title="ms-stats", openapi_prefix=openapi_prefix) 
​
from .routers.v1 import router as routers_v1

app.include_router(routers_v1)
handler = Mangum(app)
