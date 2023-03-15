"""token created

Revision ID: a6b0c621c2ce
Revises: 0115505fc424
Create Date: 2023-03-15 07:40:06.145596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6b0c621c2ce'
down_revision = '0115505fc424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###