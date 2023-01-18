"""
SQL Alchemy models declaration.
https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#example-two-dataclasses-with-declarative-table
Dataclass style for powerful autocompletion support.

https://alembic.sqlalchemy.org/en/latest/tutorial.html
Note, it is used by alembic migrations logic, see `alembic/env.py`

Alembic shortcuts:
# create migration
alembic revision --autogenerate -m "migration_name"

# apply all migrations
alembic upgrade head
"""

import uuid
from dataclasses import dataclass

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry
from sqlalchemy.sql import func

Base = registry()


@Base.mapped
class SpringheadTime:
    __tablename__ = "springhead_times"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time_ns = Column(BigInteger, nullable=False, index=True)
    type_timer = Column(String(128), nullable=False)
    type_test_case = Column(String(128), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


@Base.mapped
@dataclass
class StatefunTime:
    __tablename__ = "statefun_times"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time_ns = Column(BigInteger, nullable=False, index=True)
    type_timer = Column(String(128), nullable=False)
    type_test_case = Column(String(128), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
