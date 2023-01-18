from __future__ import annotations

from dataclasses import dataclass
from logging import getLogger

import app.handlers  # noqa
from app.adapters.stateful_functions import stateful_functions
from pydantic import AnyHttpUrl
from statefun import RequestReplyHandler

logger = getLogger(__name__)


@dataclass
class Bootstrap:
    handler: RequestReplyHandler
    side_car_address: AnyHttpUrl = "http://sidecar:8889/springhead/"  # type: ignore
    type_test_case: str = "all-combination"
    benchmark_mode: bool = False


async def bootstrap(
    side_car_address: AnyHttpUrl = "http://sidecar:8889/springhead/",  # type: ignore
    type_test_case: str = "all-combination",
    benchmark_mode: bool = False,
) -> Bootstrap:
    logger.debug(stateful_functions._functions)
    handler = RequestReplyHandler(stateful_functions)
    return Bootstrap(
        handler=handler,
        side_car_address=side_car_address,
        type_test_case=type_test_case,
        benchmark_mode=benchmark_mode,
    )
