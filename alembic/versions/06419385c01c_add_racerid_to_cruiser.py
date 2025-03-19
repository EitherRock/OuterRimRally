"""add racerid to cruiser

Revision ID: 06419385c01c
Revises: 5a6fcff9e18f
Create Date: 2025-03-17 17:51:18.942307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06419385c01c'
down_revision: Union[str, None] = '5a6fcff9e18f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cruisers', sa.Column('racer_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'cruisers', 'racers', ['racer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cruisers', type_='foreignkey')
    op.drop_column('cruisers', 'racer_id')
    # ### end Alembic commands ###
