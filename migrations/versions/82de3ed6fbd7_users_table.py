"""users table

Revision ID: 82de3ed6fbd7
Revises: 
Create Date: 2023-01-21 21:29:16.776915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82de3ed6fbd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('nip', sa.String(length=8), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_nip'), ['nip'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_nip'))

    op.drop_table('user')
    # ### end Alembic commands ###
