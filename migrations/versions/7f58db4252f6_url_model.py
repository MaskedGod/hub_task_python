"""url model

Revision ID: 7f58db4252f6
Revises: 
Create Date: 2025-03-28 00:02:26.656518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f58db4252f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('original_url', sa.String(), nullable=False),
    sa.Column('short_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('original_url'),
    sa.UniqueConstraint('short_url')
    )
    op.create_index(op.f('ix_urls_id'), 'urls', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_id'), table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###
