import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

metadata = sa.MetaData()


class CategoryEnum(sa.Enum):
    beauty = "Beauty"
    grocery = "Grocery"
    food = "Food"
    furniture = "Furniture"
    shoes = "Shoes"
    frames = "Frames"
    jewellery = "Jewellery"


categorie = sa.Table(
    "categorie",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("image", sa.String(255), nullable=False),
    sa.Column("product_name", sa.String(255), nullable=False),
    sa.Column("category", sa.Enum("Beauty", "Grocery", "Food", "Furniture", "Shoes", "Frames", "Jewellery")),
    sa.Column("code", sa.String(255), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.TIMESTAMP(timezone=True),
        default=sa.func.now(),
        onupdate=sa.func.now(),
    ),

)
