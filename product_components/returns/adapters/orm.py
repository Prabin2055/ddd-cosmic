import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

metadata = sa.MetaData()


class BillerEnum(sa.Enum):
    test_biller = "TestBiller"


class OrderTaxEnum(sa.Enum):
    no_tax = "NoTex"
    gst = "GST@%%"
    vat = "VAT@10%"


returns = sa.Table(
    "returns",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("date", sa.String(255), nullable=False),
    sa.Column("reference_no", sa.String(255), nullable=False),
    sa.Column("return_biller", sa.Enum("TestBiller")),
    sa.Column("customer", sa.String(255), nullable=False),
    sa.Column("order_tax", sa.Enum("NoTax", "GST@5%", "VAT@10%")),
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

)

