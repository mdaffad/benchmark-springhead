from logging import getLogger

from app.models import SpringheadTime
from app.schemas import SpringheadTimeCreateRequest
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies import get_session

router = APIRouter()

logger = getLogger(__name__)


@router.post("/")
async def create_springhead_time_stamp(
    new_springhead_time: SpringheadTimeCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    springhead_time = SpringheadTime(
        time_ns=new_springhead_time.time_ns,
        type_timer=new_springhead_time.type_timer,
        type_test_case=new_springhead_time.type_test_case,
    )
    try:
        session.add(springhead_time)
        await session.commit()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    return springhead_time
