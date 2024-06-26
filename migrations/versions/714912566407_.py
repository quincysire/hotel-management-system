"""empty message

Revision ID: 714912566407
Revises: 
Create Date: 2024-06-22 18:12:40.997665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714912566407'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=100), nullable=False),
    sa.Column('secondName', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=True),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('hotel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotelName', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guest_id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.Column('check_in', sa.DateTime(), nullable=True),
    sa.Column('check_out', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['guest_id'], ['guest.id'], ),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('hotel')
    op.drop_table('guest')
    # ### end Alembic commands ###
