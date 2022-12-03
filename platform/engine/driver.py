"""
Model Driver that utilises the uploaded models
"""
from __future__ import annotations

import importlib

from platform.base import ModelProtocol


class ModelDriver:
    def __init__(self):
        pass

    @staticmethod
    def _import_model(model_path):
        self.user_model = importlib.import_module(model_path)
        assert isinstance(self.user_model, ModelProtocol)

    def run(self, image_urls):

        pass
