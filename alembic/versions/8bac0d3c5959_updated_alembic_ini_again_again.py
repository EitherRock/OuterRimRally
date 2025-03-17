"""updated alembic.ini again again

Revision ID: 8bac0d3c5959
Revises: cdeada3808fd
Create Date: 2025-03-16 19:40:21.468106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bac0d3c5959'
down_revision: Union[str, None] = 'cdeada3808fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
