from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Racer(Base):
    __tablename__ = 'racers'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    rank_id = Column(Integer, ForeignKey("ranks.id", ondelete="SET NULL"), nullable=True)
    races_attended = Column(Integer, default=0, nullable=False)
    credits = Column(Integer, default=1000, nullable=False)


    rank = relationship("Rank", lazy="joined")  # Optimizes the join when querying
    orders = relationship("Order", cascade="all, delete", back_populates="racer")

class Rank(Base):
    __tablename__ = 'ranks'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, unique=True, nullable=False)
    credits_first = Column(Integer, nullable=False)
    credits_second = Column(Integer, nullable=False)
    credits_third = Column(Integer, nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

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

    category = relationship("Category", backref="parts")
    
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=True, index=True)
    order_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    total_amount = Column(Integer, nullable=False, server_default=text('0'))

    racer = relationship("Racer", lazy="joined", back_populates="orders")
    order_parts =relationship("OrderPart", cascade="all, delete")

class OrderPart(Base):
    __tablename__ = 'order_parts'

    id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=True, index=True)
    part_id = Column(Integer, ForeignKey("parts.id", ondelete="SET NULL"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, server_default=text('1'))
    unit_price = Column(Integer, nullable=False, server_default=text('0'))

    order = relationship("Order")
    part = relationship("Part")