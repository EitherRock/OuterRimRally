"""linux test

Revision ID: 0b577d1956b9
Revises: 8ffc94cdc9ff
Create Date: 2025-03-16 19:55:10.616719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b577d1956b9'
down_revision: Union[str, None] = '8ffc94cdc9ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
