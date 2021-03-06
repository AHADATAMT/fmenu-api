"""empty message

Revision ID: 8a2d105ea211
Revises: 4322077a9c55
Create Date: 2019-05-20 10:13:29.619464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a2d105ea211'
down_revision = '4322077a9c55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.drop_constraint('category_user_id_fkey', 'category', type_='foreignkey')
    op.create_foreign_key(None, 'category', 'restaurant', ['restaurant_id'], ['id'])
    op.drop_column('category', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.create_foreign_key('category_user_id_fkey', 'category', 'user', ['user_id'], ['id'])
    op.drop_column('category', 'restaurant_id')
    # ### end Alembic commands ###
