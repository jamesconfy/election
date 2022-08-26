"""First

Revision ID: 1cba3f7119ff
Revises: 
Create Date: 2022-08-23 16:12:29.799008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cba3f7119ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ward', 'ward_description',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ward', 'ward_description',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###