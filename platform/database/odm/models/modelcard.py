from odmantic import Model


class ModelCard(Model):
    name: str                          # You can use normal types just like in pydantic
    model_id: str
    model_path: str
