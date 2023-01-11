from __future__ import annotations

from fastapi import APIRouter

model_router = APIRouter(
    prefix='/model',
    tags=['model'],
    #responses={404: {'description': 'Not found'}},
)


class ModelRouter:
    """
    Router class for future enhancement.
    """
    @model_router.get('/predict')
    async def platform_status(status_code=200):
        return {'status': status_code}

    @model_router.get('/batch_predict')
    async def platform_status(status_code=200):
        return {'status': status_code}
