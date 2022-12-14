"""change logo required to non required

Revision ID: 6c6e40f2b60f
Revises: eadadc9da379
Create Date: 2022-12-02 13:46:42.714482

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c6e40f2b60f'
down_revision = 'eadadc9da379'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('logo',
               existing_type=mysql.VARCHAR(length=150),
               nullable=True)

    with op.batch_alter_table('variant', schema=None) as batch_op:
        batch_op.alter_column('logo',
               existing_type=mysql.VARCHAR(length=150),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variant', schema=None) as batch_op:
        batch_op.alter_column('logo',
               existing_type=mysql.VARCHAR(length=150),
               nullable=False)

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('logo',
               existing_type=mysql.VARCHAR(length=150),
               nullable=False)

    # ### end Alembic commands ###
