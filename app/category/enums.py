from enum import Enum, unique

@unique
class Categories(Enum):
    POWER_SOURCE = 'Power Source'
    PROPULSION = 'Propulsion'
    HANDLING ='Handling'