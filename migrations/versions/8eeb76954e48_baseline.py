"""baseline

Revision ID: 8eeb76954e48
Revises: 21f63dd3c65c
Create Date: 2026-02-01 21:06:36.949693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eeb76954e48'
down_revision: Union[str, Sequence[str], None] = '21f63dd3c65c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
