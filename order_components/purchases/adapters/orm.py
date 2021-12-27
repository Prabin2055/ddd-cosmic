import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

metadata = sa.MetaData()


class SupplierEnum(sa.Enum):
    select_supplier = "SelectSupplier"
    test_supplier = "TestSupplier"


class ReceivedEnum(sa.Enum):
    received = "Received"
    not_received_yet = "NotReceivedYet"


class OrderTaxEnum(sa.Enum):
    no_tax = "NoTax"
    gst = "GST@5%"
    vat = "VAT@20%"


purchase = sa.Table(
    "purchase",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("date", sa.String(255), nullable=False),
    sa.Column("purchase_no", sa.String(255), nullable=False),
    sa.Column("supplier", sa.Enum("SelectSupplier", "TestSupplier")),
    sa.Column("received", sa.Enum("Received", "NotReceivedYet")),
    sa.Column("order_taxes", sa.Enum("NoTax", "GST@5%", "VAT@20%")),
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

)
