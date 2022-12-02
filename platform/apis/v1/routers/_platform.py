from __future__ import annotations

from fastapi import APIRouter

platform_router = APIRouter()


class PlatformRouter:
    """
    Router class for future enhancement.
    """
    @platform_router.get('/platform/routers')
    async def platform_status(status_code=200):
        return {'status': status_code}
