from fastapi import APIRouter

from api.endpoints.v1.departments import router as departments_router

api_router_v1 = APIRouter(prefix='/v1')

api_router_v1.include_router(departments_router)
