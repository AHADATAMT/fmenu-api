"""empty message

Revision ID: 4322077a9c55
Revises: 5e1364908414
Create Date: 2019-05-19 22:22:40.582853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4322077a9c55'
down_revision = '5e1364908414'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('url', sa.String(), nullable=True))
    op.drop_constraint('image_name_key', 'image', type_='unique')
    op.create_unique_constraint(None, 'image', ['url'])
    op.drop_column('image', 'name')
    op.add_column('qrcode', sa.Column('code', sa.String(), nullable=True))
    op.drop_constraint('qrcode_name_key', 'qrcode', type_='unique')
    op.create_unique_constraint(None, 'qrcode', ['code'])
    op.drop_column('qrcode', 'name')
    op.add_column('restaurant', sa.Column('qrcode', sa.String(), nullable=True))
    op.drop_constraint('restaurant_qrcode_id_fkey', 'restaurant', type_='foreignkey')
    op.drop_column('restaurant', 'qrcode_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('qrcode_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('restaurant_qrcode_id_fkey', 'restaurant', 'qrcode', ['qrcode_id'], ['id'])
    op.drop_column('restaurant', 'qrcode')
    op.add_column('qrcode', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'qrcode', type_='unique')
    op.create_unique_constraint('qrcode_name_key', 'qrcode', ['name'])
    op.drop_column('qrcode', 'code')
    op.add_column('image', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'image', type_='unique')
    op.create_unique_constraint('image_name_key', 'image', ['name'])
    op.drop_column('image', 'url')
    # ### end Alembic commands ###