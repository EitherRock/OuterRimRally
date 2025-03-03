from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Racer(Base):
    __tablename__ = 'racers'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    password_hash = Column(String, nullable=False)
    rank_id = Column(Integer, ForeignKey("ranks.id", ondelete="SET NULL"), nullable=True)
    races_attended = Column(Integer, default=0, nullable=False)
    credits = Column(Integer, default=1000, nullable=False)


    rank = relationship("Rank")

class Rank(Base):
    __tablename__ = 'ranks'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, unique=True, nullable=False)
    credits_first = Column(Integer, nullable=False)
    credits_second = Column(Integer, nullable=False)
    credits_third = Column(Integer, nullable=False)
    
