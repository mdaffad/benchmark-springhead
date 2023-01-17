import logging
from time import time_ns

from app.bootstrap import Bootstrap, bootstrap
from app.config import settings
from app.controllers import main_router
from fastapi import FastAPI

logger = logging.getLogger()

app = FastAPI()
app.include_router(main_router)


def init_logger(level):
    logger.setLevel(level)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d %(levelname)s %(pathname)s:%(lineno)d: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


@app.on_event("startup")
async def startup():
    init_logger(settings.log_level)

    logger = logging.getLogger(__name__)
    start_time = time_ns()
    app.state.bootstrap: Bootstrap = await bootstrap()
    end_time = time_ns()
    logger.info(f"elapsed statefun bootstrap: {end_time-start_time}")
    logger.info("Bootstrap is done")
