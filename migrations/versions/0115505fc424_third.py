"""third

Revision ID: 0115505fc424
Revises: ab90af7c4a17
Create Date: 2023-03-14 11:18:27.406056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0115505fc424'
down_revision = 'ab90af7c4a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=64), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
