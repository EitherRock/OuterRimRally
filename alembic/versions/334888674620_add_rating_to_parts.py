"""add rating to parts

Revision ID: 334888674620
Revises: 0b577d1956b9
Create Date: 2025-03-16 20:35:17.545771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '334888674620'
down_revision: Union[str, None] = '0b577d1956b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
