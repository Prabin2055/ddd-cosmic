"""sale

Revision ID: d4b670ec1268
Revises: 
Create Date: 2021-08-08 15:33:11.810876

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'd4b670ec1268'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "sale",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("date", sa.String(255), nullable=False),
        sa.Column("reference_no", sa.String(255), nullable=True),
        sa.Column("customer", sa.String(255), nullable=True),
        sa.Column("sale_biller", sa.Enum("TestBiller", name="sale_biller")),
        sa.Column("tax", sa.Enum("NoTax", "GST@5%", "VAT@10%", name="tax")),
        sa.Column("order_discount", sa.Float(), nullable=False),
        sa.Column("shipping", sa.String(255), nullable=False),
        sa.Column("attach_document", sa.String(255), nullable=False),
        sa.Column("sale_status", sa.Enum("Completed", "Pending", name="sale_status")),
        sa.Column("payments_status", sa.Enum("Pending", "Due", "Paid", name="payments_status")),
        sa.Column("sales_note", sa.String(255), nullable=False),
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
    op.drop_table("sale")
