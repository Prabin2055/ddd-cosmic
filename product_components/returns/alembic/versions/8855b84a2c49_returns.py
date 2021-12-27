"""returns

Revision ID: 8855b84a2c49
Revises: 
Create Date: 2021-08-10 07:41:24.758054

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '8855b84a2c49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "returns",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("date", sa.String(255), nullable=True),
        sa.Column("reference_no", sa.String(255), nullable=True),
        sa.Column("return_biller", sa.Enum("TestBiller", name="return_biller")),
        sa.Column("customer", sa.String(255), nullable=True),
        sa.Column("order_tax", sa.Enum("NoTax", "GST@5%", "VAT@10%", name="order_tax")),
        sa.Column("order_discount", sa.Float(), nullable=False),
        sa.Column("shipping", sa.String(255), nullable=False),
        sa.Column("attach_document", sa.String(255), nullable=False),
        sa.Column("return_note", sa.String(255), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("reference_no")
    )


def downgrade():
    op.drop_table("returns")
