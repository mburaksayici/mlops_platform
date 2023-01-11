from __future__ import annotations

import uvicorn
from config import APIConfig

from .routers import model_router


class ModelDriver:
    def __init__(self):
        self.api_config = APIConfig()

    def setup(self, app) -> None:
        """
        FastAPI setup on exceptions and tokens.
        # TO DO : Add token https://fastapi.tiangolo.com/tutorial/security/first-steps/
        """
        pass

    def register_router(self, app):
        app.include_router(model_router)

    def run(self, app):
        """
        The main executing function which runs the uvicorn server
        with the app instance and user configuration.
        """
        # run uvicorn server.
        uvicorn.run(app, port=self.api_config.MODELDRIVER_PORT, host='0.0.0.0')
