"""empty message

Revision ID: 13d95a04142a
Revises: e01393a9dce4
Create Date: 2019-05-20 11:39:00.758206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d95a04142a'
down_revision = 'e01393a9dce4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dish', sa.Column('image_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'dish', 'image', ['image_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dish', type_='foreignkey')
    op.drop_column('dish', 'image_id')
    # ### end Alembic commands ###