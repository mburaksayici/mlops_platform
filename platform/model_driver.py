from __future__ import annotations

from apis import ModelDriver
from fastapi import APIRouter
from fastapi import FastAPI


app = FastAPI()


def main():
    # create fastapi application
    model_driver = ModelDriver()
    model_driver.setup(app)
    model_driver.register_router(app)
    model_driver.run(app)


if __name__ == '__main__':
    main()
