"""add items

Revision ID: e70a950a2322
Revises: bde32fdc7ed6
Create Date: 2018-04-14 20:16:04.312983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70a950a2322'
down_revision = 'bde32fdc7ed6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(85), index=True),
        sa.Column('description', sa.String(255), index=True),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id'))
    )

def downgrade():
    op.drop_table('items')