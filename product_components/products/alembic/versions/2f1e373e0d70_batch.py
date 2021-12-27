"""batch

Revision ID: 2f1e373e0d70
Revises: f818d3ed450d
Create Date: 2021-08-02 21:23:37.569808

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '2f1e373e0d70'
down_revision = 'f818d3ed450d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "batch",
        sa.Column("ref", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("sku", sa.String(255), nullable=False),
        sa.Column("purchased_quantity", sa.String(255), nullable=False),
        sa.Column("eta", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("ref"),
        sa.UniqueConstraint("sku")
    )


def downgrade():
    op.drop_table("batch")
