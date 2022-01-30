"""New boat table

Revision ID: 51919f01f049
Revises: 
Create Date: 2022-01-29 21:00:13.193879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51919f01f049'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('boat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('boat')
