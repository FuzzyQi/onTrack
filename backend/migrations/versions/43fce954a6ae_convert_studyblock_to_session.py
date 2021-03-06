"""Convert studyblock to session

Revision ID: 43fce954a6ae
Revises: 667ef0849200
Create Date: 2021-03-27 16:14:12.706932

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43fce954a6ae'
down_revision = '667ef0849200'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('study_block')
    op.drop_table('sessions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('duration_s', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.VARCHAR(length=7), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.code'], name='sessions_course_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='sessions_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='sessions_pkey')
    )
    op.create_table('study_block',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('duration_s', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.VARCHAR(length=7), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.code'], name='study_block_course_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='study_block_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='study_block_pkey')
    )
    # ### end Alembic commands ###
