from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ..database.core import Base

class Cruiser(Base):
    __tablename__ = 'cruisers'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    updated = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    name = Column(String, nullable=False)
    power_source_id = Column(Integer, ForeignKey('parts.id'))
    propulsion_id = Column(Integer, ForeignKey('parts.id'))
    handling_id = Column(Integer, ForeignKey('parts.id'))

    power_source = relationship("Part", foreign_keys=[power_source_id])
    propulsion = relationship("Part", foreign_keys=[propulsion_id])
    handling = relationship("Part", foreign_keys=[handling_id])
