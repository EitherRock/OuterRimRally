from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from ..database.core import Base


class Part(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False, server_default=text('0'))
    stock_quantity = Column(Integer, nullable=False, server_default=text('0'))
    rating = Column(Integer, nullable=False, server_default=text('0'))

    category = relationship("Category", backref="parts")