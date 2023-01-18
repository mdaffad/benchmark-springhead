from fastapi import APIRouter

from .endpoints import springhead, statefun

api_router = APIRouter()
api_router.include_router(statefun.router, prefix="/statefun", tags=["statefun"])
api_router.include_router(springhead.router, prefix="/springhead", tags=["springhead"])
