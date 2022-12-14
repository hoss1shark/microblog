"""empty message

Revision ID: de515df22f36
Revises: bde9f60077dc
Create Date: 2022-12-14 19:38:50.286794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de515df22f36'
down_revision = 'bde9f60077dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_message_read_time', sa.DateTime(), nullable=True))
    op.drop_column('user', 'last_massage_read_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_massage_read_time', sa.DATETIME(), nullable=True))
    op.drop_column('user', 'last_message_read_time')
    # ### end Alembic commands ###
