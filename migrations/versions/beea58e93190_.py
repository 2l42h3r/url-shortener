"""empty message

Revision ID: beea58e93190
Revises: 
Create Date: 2022-08-01 19:10:56.081598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beea58e93190'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_url_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_url', sa.String(length=500), nullable=False),
    sa.Column('shortened', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('shortened')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_url_table')
    # ### end Alembic commands ###