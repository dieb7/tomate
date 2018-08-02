"""tasks table

Revision ID: c48c96a0a823
Revises: ba0c140719c7
Create Date: 2018-08-01 22:38:09.482880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c48c96a0a823'
down_revision = 'ba0c140719c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=140), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('started', sa.DateTime(), nullable=True),
    sa.Column('done', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_created'), 'task', ['created'], unique=False)
    op.create_index(op.f('ix_task_done'), 'task', ['done'], unique=False)
    op.create_index(op.f('ix_task_started'), 'task', ['started'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_started'), table_name='task')
    op.drop_index(op.f('ix_task_done'), table_name='task')
    op.drop_index(op.f('ix_task_created'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###