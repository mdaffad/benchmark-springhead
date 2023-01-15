from __future__ import annotations

from dataclasses import dataclass

from statefun import RequestReplyHandler, StatefulFunctions


@dataclass
class Bootstrap:
    handler: RequestReplyHandler


async def bootstrap() -> Bootstrap:
    stateful_functions = StatefulFunctions()
    handler = RequestReplyHandler(stateful_functions)
    return Bootstrap(handler=handler)
