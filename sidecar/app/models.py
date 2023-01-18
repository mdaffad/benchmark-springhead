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
from dataclasses import dataclass, field

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry
from sqlalchemy.sql import func

Base = registry()


@Base.mapped
@dataclass
class SpringheadTime:
    __tablename__ = "springhead_times"
    __sa_dataclass_metadata_key__ = "sa"

    id: uuid.UUID = field(
        init=False,
        default_factory=uuid.uuid4,
        metadata={"sa": Column(UUID(as_uuid=True), primary_key=True)},
    )
    time_ns: int = field(
        metadata={"sa": Column(BigInteger, nullable=False, unique=True, index=True)}
    )
    type_timer: str = field(metadata={"sa": Column(String(128), nullable=False)})
    type_test_case: str = field(metadata={"sa": Column(String(128), nullable=False)})
    timestamp = field(
        metadata={"sa": Column(DateTime(timezone=True), server_default=func.now())}
    )


@Base.mapped
@dataclass
class StatefunTime:
    __tablename__ = "statefun_times"
    __sa_dataclass_metadata_key__ = "sa"

    id: uuid.UUID = field(
        init=False,
        default_factory=uuid.uuid4,
        metadata={"sa": Column(UUID(as_uuid=True), primary_key=True)},
    )
    time_ns: int = field(
        metadata={"sa": Column(BigInteger, nullable=False, unique=True, index=True)}
    )
    type_timer: str = field(metadata={"sa": Column(String(128), nullable=False)})
    type_test_case: str = field(metadata={"sa": Column(String(128), nullable=False)})
    timestamp = field(
        metadata={"sa": Column(DateTime(timezone=True), server_default=func.now())}
    )
