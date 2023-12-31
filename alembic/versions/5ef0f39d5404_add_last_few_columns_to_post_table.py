"""add last few columns to post table

Revision ID: 5ef0f39d5404
Revises: 5f6c41c4fdb5
Create Date: 2023-06-18 12:53:16.576964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ef0f39d5404'
down_revision = '5f6c41c4fdb5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE')
    )
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
    )

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
