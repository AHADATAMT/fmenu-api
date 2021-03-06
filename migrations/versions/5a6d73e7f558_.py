"""empty message

Revision ID: 5a6d73e7f558
Revises: f652a8a22d83
Create Date: 2019-05-14 09:31:25.656150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a6d73e7f558'
down_revision = 'f652a8a22d83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'restaurant', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'restaurant', type_='foreignkey')
    op.drop_column('restaurant', 'user_id')
    # ### end Alembic commands ###
