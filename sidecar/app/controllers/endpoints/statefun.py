from logging import getLogger

from app.models import StatefunTime
from app.schemas import StatefunTimeCreateRequest
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies import get_session

router = APIRouter()

logger = getLogger(__name__)


@router.post("/")
async def create_statefun_time_stamp(
    new_statefun_time: StatefunTimeCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    statefun_time = StatefunTime(
        time_ns=new_statefun_time.time_ns,
        type_timer=new_statefun_time.type_timer,
        type_test_case=new_statefun_time.type_test_case,
    )
    try:
        session.add(statefun_time)
        await session.commit()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    return statefun_time
