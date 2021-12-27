"""user

Revision ID: 25ceaf4f9abb
Revises: 
Create Date: 2021-08-05 06:20:08.532906

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '25ceaf4f9abb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_table",
        sa.Column("id", postgresql.UUID(as_uuid=False)),
        sa.Column("first_name", sa.String(255), nullable=False),
        sa.Column("last_name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("user_name", sa.String(255), nullable=False),
        sa.Column("password", sa.String(255)),
        sa.Column("phone_number", sa.String(255)),
        sa.Column("is_admin", sa.Boolean(), server_default="f", default=False),
        sa.Column("is_client", sa.Boolean(), server_default="f", default=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_name"),
    )


def downgrade():
    op.drop_table("user_table")
