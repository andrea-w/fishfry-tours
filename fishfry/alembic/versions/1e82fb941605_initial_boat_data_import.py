"""Initial boat data import

Revision ID: 1e82fb941605
Revises: 51919f01f049
Create Date: 2022-01-29 21:02:03.581164

"""
from alembic import op
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = '1e82fb941605'
down_revision = '51919f01f049'
branch_labels = None
depends_on = None


def upgrade():
    # Solution for this taken from https://stackoverflow.com/a/57609029
    # get metadata from current connection
    meta = MetaData(bind=op.get_bind())

    # pass in tuple with tables we want to reflect (otherwise entire DB will be reflected)
    meta.reflect(only=('boat',))

    # define table representation
    boat_tbl = Table('boat', meta)


    op.bulk_insert(boat_tbl, [
        {
            "name": "Boaty McBoatFace",
            "status": "DOCKED"
        },
        {
            "name": "Ships n' Giggles",
            "status": "MAINTENANCE"
        },
        {
            "name": "Moor Often Than Knot",
            "status": "OUTBOUND_TO_SEA"
        },
        {
            "name": "Seas The Day",
            "status": "INBOUND_TO_HARBOUR"
        },
        {
            "name": "Knight of the Caribbean",
            "status": "DOCKED"
        },
        {
            "name": "Usain Boat",
            "status": "MAINTENANCE"
        },
        {
            "name": "The Codfather",
            "status": "OUTBOUND_TO_SEA"
        },
        {
            "name": "Pier Pressure",
            "status": "INBOUND_TO_HARBOUR"
        }
    ])


def downgrade():
    op.execute('DELETE FROM TABLE boat;')
