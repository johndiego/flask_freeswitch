"""empty message

Revision ID: 55b09d2c3412
Revises: 202a40d16d10
Create Date: 2015-03-06 21:48:04.079770

"""

# revision identifiers, used by Alembic.
revision = '55b09d2c3412'
down_revision = '202a40d16d10'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    ### end Alembic commands ###
