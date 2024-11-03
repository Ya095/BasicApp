"""fix user and token tables

Revision ID: 2c0c1fed234f
Revises: 19fbb4b5a8aa
Create Date: 2024-11-03 22:33:19.265424

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2c0c1fed234f"
down_revision: Union[str, None] = "19fbb4b5a8aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("access_tokens", "id")


def downgrade() -> None:
    op.add_column(
        "access_tokens",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
