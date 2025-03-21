"""Added name, phone, and address to Patient

Revision ID: 9e2ca5bd167b
Revises: aab65a369ebd
Create Date: 2025-03-21 20:55:25.430264

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9e2ca5bd167b'
down_revision = 'aab65a369ebd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(length=15), nullable=False))
        batch_op.add_column(sa.Column('address', sa.String(length=255), nullable=False))
        batch_op.create_unique_constraint(None, ['phone'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_column('password')

    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('address')
        batch_op.drop_column('phone')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
