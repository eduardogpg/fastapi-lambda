from fastapi import FastAPI

app = FastAPI(debug=False)

from .routers.v1 import router as routers_v1

app.include_router(routers_v1)
