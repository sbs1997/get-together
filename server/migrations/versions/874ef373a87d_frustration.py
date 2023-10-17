"""frustration

Revision ID: 874ef373a87d
Revises: 44fb3098b561
Create Date: 2023-10-17 17:32:08.131163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '874ef373a87d'
down_revision = '44fb3098b561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('DOB',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('DOB',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
