"""init time test schema

Revision ID: d66524fce938
Revises:
Create Date: 2023-01-18 07:45:02.123987

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "d66524fce938"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "springhead_times",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("time_ns", sa.BigInteger(), nullable=False),
        sa.Column("type_timer", sa.String(length=128), nullable=False),
        sa.Column("type_test_case", sa.String(length=128), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "statefun_times",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("time_ns", sa.BigInteger(), nullable=False),
        sa.Column("type_timer", sa.String(length=128), nullable=False),
        sa.Column("type_test_case", sa.String(length=128), nullable=False),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_statefun_times_time_ns"), table_name="statefun_times")
    op.drop_table("statefun_times")
    op.drop_index(op.f("ix_springhead_times_time_ns"), table_name="springhead_times")
    op.drop_table("springhead_times")
    # ### end Alembic commands ###