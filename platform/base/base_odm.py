"""
Base class that odm objects need to have.
"""
from abc import ABCMeta
from abc import abstractmethod

from bunnet import Document
from bunnet import Indexed
from bunnet import init_bunnet


class BaseODM(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, mongo_client, odm_map):
        self.mongo_client = mongo_client

    @abstractmethod
    def set_odm_model(self, odm_model):
        self.odm_model = odm_model

    @abstractmethod
    def init_connect(self, db_name):
        init_bunnet(
            database=self.mongo_client[db_name], document_models=[
                self.odm_model,
            ],
        )
