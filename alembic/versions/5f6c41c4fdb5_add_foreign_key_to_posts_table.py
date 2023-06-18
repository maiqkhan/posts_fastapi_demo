"""add foreign key to posts table

Revision ID: 5f6c41c4fdb5
Revises: a2ba53f8aeab
Create Date: 2023-06-18 12:48:56.168536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f6c41c4fdb5'
down_revision = 'a2ba53f8aeab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name='post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
