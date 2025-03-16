from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from ..database.core import Base
    
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False)
    racer_id = Column(Integer, ForeignKey('racers.id', ondelete='CASCADE'), nullable=True, index=True)
    order_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    total_amount = Column(Integer, nullable=False, server_default=text('0'))

    racer = relationship('Racer', lazy='joined', back_populates='orders')
    order_parts =relationship('OrderPart', cascade='all, delete')

class OrderPart(Base):
    __tablename__ = 'order_parts'

    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=True, index=True)
    part_id = Column(Integer, ForeignKey("parts.id", ondelete="SET NULL"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, server_default=text('1'))

    order = relationship("Order")
    part = relationship("Part")