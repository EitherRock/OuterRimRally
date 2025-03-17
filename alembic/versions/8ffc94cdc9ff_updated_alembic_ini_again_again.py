"""updated alembic.ini again again

Revision ID: 8ffc94cdc9ff
Revises: 8bac0d3c5959
Create Date: 2025-03-16 19:42:01.649499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ffc94cdc9ff'
down_revision: Union[str, None] = '8bac0d3c5959'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
