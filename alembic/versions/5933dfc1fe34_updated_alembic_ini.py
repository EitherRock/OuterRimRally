"""updated alembic.ini

Revision ID: 5933dfc1fe34
Revises: 4d9cad4ae858
Create Date: 2025-03-16 19:31:59.245323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5933dfc1fe34'
down_revision: Union[str, None] = '4d9cad4ae858'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
