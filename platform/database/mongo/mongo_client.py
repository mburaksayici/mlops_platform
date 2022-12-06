"""
MongoClient class that connects/checks the mongodb.

Preference is on simple PyMongo+Beanie:
- Using PyMongo with Pydantic models is a way, but requires boilerplate code. It's one of the experience I've had before.
- MongoEngine requires connection per DB, also limiting the wrapper over PyMongo
- Beanie's syntax is easier to understand over mongoengine. Allows you to wrap over pymongo as well.
"""
from __future__ import annotations

import logging

import pymongo as pm
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError


class MongoClient:
    """
    A shallow MongoClient class that can be extended for replicaset configs.
    """

    def __init__(self, host, usr, pwd, port):
        self.host_url = f'mongodb://{usr}:{pwd}@{host}:{port}'

    def _test_connect(self, conn):
        try:
            conn.server_info()  # force connection on a request as the
            # connect=True parameter of MongoClient seems
            # to be useless here
        except ServerSelectionTimeoutError as err:
            logging.info(f'Mongo Connection Error  :: {err}')
            raise

    def connect(self, local=False):
        if local:
            conn = pm.MongoClient(self.host_url)
        else:
            conn = pm.MongoClient(self.host_url)

        self._test_connect(conn)
        return conn
