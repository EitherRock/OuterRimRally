"""update rank_id to be int

Revision ID: 0286be8f7509
Revises: 6a2c16e5e8f6
Create Date: 2025-03-03 16:56:05.849461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0286be8f7509'
down_revision: Union[str, None] = '6a2c16e5e8f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
