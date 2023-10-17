"""fixed ambiguous foreign keys

Revision ID: 67ef4ddd4ee8
Revises: fa58042638d4
Create Date: 2023-10-17 16:37:13.595157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67ef4ddd4ee8'
down_revision = 'fa58042638d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_blocked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_blocked_id'], ['user_blockeds.id'], name=op.f('fk_blockees_user_blocked_id_user_blockeds')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_blockees_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blockers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_blocked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_blocked_id'], ['user_blockeds.id'], name=op.f('fk_blockers_user_blocked_id_user_blockeds')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_blockers_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user_blockeds', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_blockeds_blocker_id_users', type_='foreignkey')
        batch_op.drop_constraint('fk_user_blockeds_blockee_id_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_user_blockeds_blockee_id_blockees'), 'blockees', ['blockee_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_user_blockeds_blocker_id_blockers'), 'blockers', ['blocker_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_blockeds', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_blockeds_blocker_id_blockers'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_user_blockeds_blockee_id_blockees'), type_='foreignkey')
        batch_op.create_foreign_key('fk_user_blockeds_blockee_id_users', 'users', ['blockee_id'], ['id'])
        batch_op.create_foreign_key('fk_user_blockeds_blocker_id_users', 'users', ['blocker_id'], ['id'])

    op.drop_table('blockers')
    op.drop_table('blockees')
    # ### end Alembic commands ###
