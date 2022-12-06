from bunnet import Document
from bunnet import Indexed


class ModelCard(Document):
    name: str                          # You can use normal types just like in pydantic
    model_id: str
    model_path: str
