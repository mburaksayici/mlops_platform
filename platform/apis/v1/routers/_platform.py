from __future__ import annotations

from fastapi import APIRouter

platform_router = APIRouter(
    prefix='/platform',
    tags=['platform'],
    responses={404: {'description': 'Not found'}},
)


class PlatformRouter:
    """
    Router class for future enhancement.
    """
    @platform_router.get('/routers')
    async def platform_status(status_code=200):
        return {'status': status_code}
