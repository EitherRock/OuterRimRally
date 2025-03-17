"""updated alembic.ini again

Revision ID: 84d331401e4a
Revises: 613e7e11b788
Create Date: 2025-03-16 19:35:46.442864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84d331401e4a'
down_revision: Union[str, None] = '613e7e11b788'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
