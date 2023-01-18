import logging

from app.controllers.router import api_router
from app.core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger()

app = FastAPI()
app.include_router(
    api_router,
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    docs_url="/",
)

# Sets all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    # app.state.bootstrap: Bootstrap = await bootstrap()
    logger.info("Bootstrap is done")
