import logging
from time import time_ns

import requests
from fastapi import FastAPI
from springhead.controllers import main_router
from springhead.core import Bootstrap, bootstrap, settings

from .dummy import custom_process_logger
from .schemas import SpringheadTimeCreateRequest

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
    app.state.bootstrap: Bootstrap = await bootstrap(
        specification_path="./app/specifications.yml",
        custom_functions={"springhead/dummy": custom_process_logger},
        side_car_address="http://sidecar/springhead/",
        type_test_case="all-combination",
        benchmark_mode=True,
    )  # type: ignore
    end_time = time_ns()
    bootstrap_object = app.state.bootstrap
    if bootstrap_object.benchmark_mode:
        elapsed_time = end_time - start_time
        requests.post(
            bootstrap_object.side_car_address,
            json=SpringheadTimeCreateRequest(
                time_ns=elapsed_time,
                type_test_case=bootstrap_object.type_test_case,
                type_timer="bootstrap",
            ).dict(),
        )
        logger.info(f"elapsed springhead bootstrap: {end_time-start_time}")

    logger.info("Bootstrap is done")
