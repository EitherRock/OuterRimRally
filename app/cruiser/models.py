from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship, Session

from ..database.core import Base
from ..part.models import Part

class Cruiser(Base):
    __tablename__ = 'cruisers'

    id = Column(Integer, primary_key=True, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    updated = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    name = Column(String, nullable=False)
    racer_id = Column(Integer, ForeignKey('racers.id'), nullable=False, unique=True)
    power_source_id = Column(Integer, ForeignKey('parts.id'), nullable=False,)
    propulsion_id = Column(Integer, ForeignKey('parts.id'), nullable=False,)
    handling_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
    total_rating = Column(Integer, nullable=False)

    # Relationships
    racer = relationship("Racer", back_populates="cruiser")
    power_source = relationship("Part", foreign_keys=[power_source_id])
    propulsion = relationship("Part", foreign_keys=[propulsion_id])
    handling = relationship("Part", foreign_keys=[handling_id])


    @classmethod
    def calculate_total_rating(
        cls, 
        db: Session, 
        power_source_id,
        propulsion_id,
        handling_id
    ):
        
        power_source = db.query(Part).filter(Part.id == power_source_id).first()
        propulsion = db.query(Part).filter(Part.id == propulsion_id).first()
        handling = db.query(Part).filter(Part.id == handling_id).first()

        total_rating = 0
        if power_source and propulsion and handling:
            total_rating = power_source.rating + propulsion.rating + handling.rating

        return total_rating