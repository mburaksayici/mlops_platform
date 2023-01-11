from __future__ import annotations

from apis import ModelExecutorDriver
from fastapi import APIRouter
from fastapi import FastAPI


app = FastAPI()


def main():
    # create fastapi application
    model_executor_driver = ModelExecutorDriver()
    model_executor_driver.setup(app)
    model_executor_driver.register_router(app)
    model_executor_driver.run(app)


if __name__ == '__main__':
    main()
