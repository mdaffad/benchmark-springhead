from __future__ import annotations

from dataclasses import dataclass
from logging import getLogger

import app.handlers  # noqa
from app.adapters.stateful_functions import stateful_functions
from statefun import RequestReplyHandler

logger = getLogger(__name__)


@dataclass
class Bootstrap:
    handler: RequestReplyHandler


async def bootstrap() -> Bootstrap:
    logger.debug(stateful_functions._functions)
    handler = RequestReplyHandler(stateful_functions)
    return Bootstrap(handler=handler)
