"""Merge heads

Revision ID: ecfcb0f0c7c7
Revises: fb53bc6cfc01, 001
Create Date: 2025-01-05 01:27:18.953430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecfcb0f0c7c7'
down_revision: Union[str, None] = ('fb53bc6cfc01', '001')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
