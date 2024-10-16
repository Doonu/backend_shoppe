from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Column, Table

metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("price", Integer)
)
