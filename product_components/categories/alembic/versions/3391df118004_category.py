"""category

Revision ID: 3391df118004
Revises: 
Create Date: 2021-08-08 12:37:33.814189

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '3391df118004'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categorie",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("image", sa.String(255), nullable=False),
        sa.Column("product_name", sa.String(255), nullable=False),
        sa.Column("category",
                  sa.Enum("Beauty", "Grocery", "Food", "Furniture", "Shoes", "Frames", "Jewellery", name="category"),
                  nullable=False,
                  ),
        sa.Column("code", sa.String(255), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("categorie")
