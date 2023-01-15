from __future__ import annotations

from dataclasses import dataclass

from app.adapters.stateful_functions import stateful_functions
from statefun import RequestReplyHandler


@dataclass
class Bootstrap:
    handler: RequestReplyHandler


async def bootstrap() -> Bootstrap:
    handler = RequestReplyHandler(stateful_functions)
    return Bootstrap(handler=handler)
