"""change logo

Revision ID: eadadc9da379
Revises: 9363bef5a5c2
Create Date: 2022-12-02 12:42:54.724812

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eadadc9da379'
down_revision = '9363bef5a5c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo', sa.String(length=150), nullable=False))
        batch_op.drop_column('logo_id')

    with op.batch_alter_table('variant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo', sa.String(length=150), nullable=False))
        batch_op.drop_column('logo_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
        batch_op.drop_column('logo')

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
        batch_op.drop_column('logo')

    # ### end Alembic commands ###
