"""purchase

Revision ID: 3a1794c41fbf
Revises: 
Create Date: 2021-08-08 20:32:40.106534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '3a1794c41fbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "purchase",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("date", sa.String(255), nullable=False),
        sa.Column("purchase_no", sa.String(255), nullable=False),
        sa.Column("supplier", sa.Enum("SelectSupplier", "TestSupplier", name="supplier")),
        sa.Column("received", sa.Enum("Received", "NotReceivedYet", name="received")),
        sa.Column("order_taxes", sa.Enum("NoTax", "GST@5%", "VAT@20%", name="order_taxes")),
        sa.Column("discount", sa.Float(), nullable=False),
        sa.Column("shipping", sa.String(255), nullable=False),
        sa.Column("payment", sa.Float(), nullable=False),
        sa.Column("note", sa.String(255), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade():
    op.drop_table("purchase")
