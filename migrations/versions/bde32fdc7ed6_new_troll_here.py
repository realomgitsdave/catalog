"""new troll here

Revision ID: bde32fdc7ed6
Revises: 
Create Date: 2018-04-14 19:49:46.612516

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bde32fdc7ed6'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(85), index=True, unique=True),
        sa.Column('description', sa.String(255), index=True),
    )

def downgrade():
    op.drop_table('categories')