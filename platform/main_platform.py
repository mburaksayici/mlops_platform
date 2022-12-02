from __future__ import annotations

from apis import PlatformDriver
from fastapi import APIRouter


app = APIRouter()


def main():
    # create fastapi application
    platform_driver = PlatformDriver()
    platform_driver.setup(app)
    platform_driver.register_router(app)
    platform_driver.run(app)


if __name__ == '__main__':
    main()
