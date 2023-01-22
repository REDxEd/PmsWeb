"""users table access column

Revision ID: 22145a4b70ce
Revises: 82de3ed6fbd7
Create Date: 2023-01-21 21:57:53.111620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22145a4b70ce'
down_revision = '82de3ed6fbd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('super_user', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('super_user')

    # ### end Alembic commands ###
