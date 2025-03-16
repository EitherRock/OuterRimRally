from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database.core import Base

class Rank(Base):
    __tablename__ = 'ranks'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, unique=True, nullable=False)
    credits_first = Column(Integer, nullable=False)
    credits_second = Column(Integer, nullable=False)
    credits_third = Column(Integer, nullable=False)