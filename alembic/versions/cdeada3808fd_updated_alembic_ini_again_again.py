"""updated alembic.ini again again

Revision ID: cdeada3808fd
Revises: 84d331401e4a
Create Date: 2025-03-16 19:35:58.381493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdeada3808fd'
down_revision: Union[str, None] = '84d331401e4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
