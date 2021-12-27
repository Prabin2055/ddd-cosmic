"""products

Revision ID: f818d3ed450d
Revises: 
Create Date: 2021-08-01 15:50:38.175017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f818d3ed450d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column(
            "products_type",
            sa.Enum("Standard", "Combo", "Digital", "Service", name="products_type"),
            nullable=False,
        ),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("code", sa.String(255), nullable=False),
        sa.Column(
            "barcodes_symbology",
            sa.Enum("CREM01", "UM01", "SEM01", "COF01", "FUN01", "DIS01", "NIS01", name="barcodes_symbology"),
            nullable=False,
        ),
        sa.Column("categories",
                  sa.Enum("Beauty", "Grocery", "Food", "Furniture", "Shoes", "Frames", "Jewellery", name="categories"),
                  nullable=False,
                  ),
        sa.Column("cost", sa.String(255), nullable=False),
        sa.Column("price", sa.String(255), nullable=False),
        sa.Column("tax_method",
                  sa.Enum("Exclusive", "Inclusive", name="tax_method"),
                  nullable=False
                  ),
        sa.Column("quantity", sa.INTEGER(), nullable=False),
        sa.Column("image", sa.String(255), nullable=False),
        sa.Column("discription", sa.String(255), nullable=False),
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
    op.drop_table("product")
