"""
Protocol that every model needs to have.
"""
from __future__ import annotations

from typing import Protocol
from typing import runtime_checkable

# Protocol is used instead of base classes so that users wont need to deal with super().init .


@runtime_checkable
class ModelProtocol(Protocol):

    def preprocess():
        pass

    def load():
        pass

    def predict():
        pass

    def postprocess():
        pass
