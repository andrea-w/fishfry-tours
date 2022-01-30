"""Add unique constraint on boat name

Revision ID: 34eee32a7aaf
Revises: 1e82fb941605
Create Date: 2022-01-30 00:17:09.593832

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '34eee32a7aaf'
down_revision = '1e82fb941605'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, 'boat', ['name'])


def downgrade():
    op.drop_constraint(None, 'boat', type_='unique')
