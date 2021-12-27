import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

metadata = sa.MetaData()


class ProductTypeEnum(sa.Enum):
    standard = "Standard"
    combo = "Combo"
    digital = "Digital"
    service = "Service"


class BarcodeSymbologyEnum(sa.Enum):
    crem01 = "CREM01"
    um01 = "UM01"
    sem01 = "SEM01"
    cof01 = "COF01"
    fun01 = "FUN01"
    dis01 = "DIS01"
    nis01 = "NIS01"


class CategoryEnum(sa.Enum):
    beauty = "Beauty"
    grocery = "Grocery"
    food = "Food"
    furniture = "Furniture"
    shoes = "Shoes"
    frames = "Frames"
    jewellery = "Jewellery"


class TaxMethodEnum(sa.Enum):
    exclusive = "Exclusive"
    inclusive = "Inclusive"


product = sa.Table(
    "product",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("products_type", sa.Enum("Standard", "Combo", "Digital", "Service")),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("code", sa.String(255), nullable=False),
    sa.Column("barcodes_symbology", sa.Enum("CREM01", "UM01", "SEM01", "COF01", "FUN01", "DIS01", "NIS01")),
    sa.Column("categories", sa.Enum("Beauty", "Grocery", "Food", "Furniture", "Shoes", "Frames", "Jewellery")),
    sa.Column("cost", sa.String(255), nullable=False),
    sa.Column("price", sa.String(255), nullable=False),
    sa.Column("tax_method", sa.Enum("Exclusive", "Inclusive")),
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

)

batch = sa.Table(
    "batch",
    metadata,
    sa.Column("ref", postgresql.UUID(as_uuid=False), unique=True, primary_key=True),
    sa.Column("sku", sa.String(255), unique=True, nullable=False),
    sa.Column("purchased_quantity", sa.String(255), nullable=False),
    sa.Column("eta", sa.String(255), nullable=False),
)
