from __future__ import annotations

import uvicorn
from config import APIConfig

from .routers import platform_router


class PlatformDriver:
    def __init__(self):
        self.api_config = APIConfig()

    def setup(self, app) -> None:
        """
        FastAPI setup on exceptions and tokens.
        """
        pass

    def register_router(self, app):
        app.include_router(platform_router)

    def run(self, app):
        """
        The main executing function which runs the uvicorn server
        with the app instance and user configuration.
        """
        # run uvicorn server.
        uvicorn.run(app, port=self.api_config.PLATFORM_PORT, host='0.0.0.0')
