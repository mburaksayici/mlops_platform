from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv('.env.docker')


class APIConfig:
    """API Configurations"""
    PLATFORM_PORT = 8000
    MODELDRIVER_PORT = 8001


class MongoConfig:
    MONGO_INITDB_HOST = os.getenv('MONGO_INITDB_HOST')
    MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    MONGO_INITDB_PORT = os.getenv('MONGO_INITDB_PORT')
