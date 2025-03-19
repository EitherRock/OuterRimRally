from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from ..database.core import Base
from ..order.models import Order

class Racer(Base):
    __tablename__ = 'racers'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    rank_id = Column(Integer, ForeignKey("ranks.id", ondelete="SET NULL"), nullable=True)
    races_attended = Column(Integer, default=0, nullable=False)
    credits = Column(Integer, default=1000, nullable=False)

    cruiser = relationship("Cruiser", back_populates="racer", uselist=False, cascade="all, delete")
    rank = relationship("Rank", lazy="joined")  # Optimizes the join when querying
    orders = relationship("Order", cascade="all, delete", back_populates="racer")