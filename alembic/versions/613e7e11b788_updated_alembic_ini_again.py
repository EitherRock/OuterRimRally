"""updated alembic.ini again

Revision ID: 613e7e11b788
Revises: 5933dfc1fe34
Create Date: 2025-03-16 19:33:02.043604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '613e7e11b788'
down_revision: Union[str, None] = '5933dfc1fe34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
