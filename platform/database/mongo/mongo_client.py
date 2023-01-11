"""
MongoClient class that connects/checks the mongodb.

New:
ODMantic is more popular, async, allows wrapping over PyMongo or Asyncio clients.

Old:
Preference is on simple PyMongo+Beanie:
- Using PyMongo with Pydantic models is a way, but requires boilerplate code. It's one of the experience I've had before.
- MongoEngine requires connection per DB, also limiting the wrapper over PyMongo
- Beanie's syntax is easier to understand over mongoengine. Allows you to wrap over pymongo as well.
"""
from __future__ import annotations

import logging

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


class ODManticClient:
    """
    A shallow MongoClient class that can be extended for replicaset configs.
    Switching from bunnet to odmantic.
    Each service should have single connection, each service should use the same mongo connection.
    """

    def __init__(self, host, usr, pwd, port):
        self.host_url = f'mongodb://{usr}:{pwd}@{host}:{port}'

    def _test_connect(self, engine):
        pass

    def connect(self, local=False):
        client = AsyncIOMotorClient(self.host_url)
        engine = AIOEngine(client=client)
        self._test_connect(engine)
        return engine
