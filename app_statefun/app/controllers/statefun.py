import logging
from time import time_ns

import requests
from app.schemas import StatefunTimeCreateRequest
from fastapi import APIRouter, Depends, Request, Response
from statefun import RequestReplyHandler

from .dependencies import get_handler

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("")
async def handle(request: Request, handler: RequestReplyHandler = Depends(get_handler)):
    start_time = time_ns()
    req = await request.body()
    res = await handler.handle_async(req)
    response = Response(
        res,
        media_type="application/octet-stream",
    )
    end_time = time_ns()
    bootstrap_object = request.app.state.bootstrap
    if bootstrap_object.benchmark_mode:
        elapsed_time = end_time - start_time
        requests.post(
            bootstrap_object.side_car_address,
            json=StatefunTimeCreateRequest(
                time_ns=elapsed_time,
                type_test_case=bootstrap_object.type_test_case,
                type_timer="endpoint",
            ).dict(),
        )
        logger.info(f"elapsed statefun endpoint: {end_time-start_time}")
    logger.info(f"elapsed statefun endpoint: {end_time-start_time}")
    return response
