"""empty message

Revision ID: b927c37c6395
Revises: 21f1ea097175
Create Date: 2021-03-29 20:49:26.130827

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b927c37c6395'
down_revision = '21f1ea097175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyname', sa.String(length=64), nullable=True),
    sa.Column('stockcode', sa.String(length=64), nullable=True),
    sa.Column('ipodate', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('stock_amount', sa.Integer(), nullable=True),
    sa.Column('year_later_price', sa.Integer(), nullable=True),
    sa.Column('year_later_return', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='company'
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyname', sa.String(length=64), nullable=True),
    sa.Column('prediction_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='users'
    )
    op.drop_table('users')
    op.drop_table('company')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('companyname', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('stockcode', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('ipodate', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('ipotype', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('stocktype', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('bankers', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('bookvalue', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stock_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('year_later', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='company_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('companyname', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('prediction_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_table('users', schema='users')
    op.drop_table('company', schema='company')
    # ### end Alembic commands ###