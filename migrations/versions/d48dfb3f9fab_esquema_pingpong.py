"""esquema pingpong

Revision ID: d48dfb3f9fab
Revises: 
Create Date: 2025-06-12 13:42:53.995188

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd48dfb3f9fab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asociacion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('ciudad', sa.String(), nullable=True),
    sa.Column('pais', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('edad_min', sa.Integer(), nullable=True),
    sa.Column('edad_max', sa.Integer(), nullable=True),
    sa.Column('genero', sa.String(), nullable=True),
    sa.Column('sets_partido', sa.String(), nullable=True),
    sa.Column('puntos_set', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('participantes_partido',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rol', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('resultado_set',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('numero_set', sa.Integer(), nullable=True),
    sa.Column('puntos_jugA', sa.Integer(), nullable=True),
    sa.Column('puntos_equipA', sa.Integer(), nullable=True),
    sa.Column('puntos_jugB', sa.Integer(), nullable=True),
    sa.Column('puntos_equipB', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('torneo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('fecha_inicioinscripcion', sa.String(), nullable=True),
    sa.Column('fecha_terminoinscripcion', sa.String(), nullable=True),
    sa.Column('fecha_iniciocompe', sa.String(), nullable=True),
    sa.Column('fecha_fincompe', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('participantes_partido_id', sa.Integer(), nullable=True),
    sa.Column('torneo_id', sa.Integer(), nullable=True),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['pingpong.categoria.id'], ),
    sa.ForeignKeyConstraint(['participantes_partido_id'], ['pingpong.participantes_partido.id'], ),
    sa.ForeignKeyConstraint(['torneo_id'], ['pingpong.torneo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('inscripcion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('torneo_id', sa.Integer(), nullable=True),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['pingpong.categoria.id'], ),
    sa.ForeignKeyConstraint(['torneo_id'], ['pingpong.torneo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('mesa',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('numero_mesa', sa.Integer(), nullable=True),
    sa.Column('torneo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['torneo_id'], ['pingpong.torneo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('equipos_partido',
    sa.Column('equipo_id', sa.Integer(), nullable=True),
    sa.Column('participantes_partido_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['equipo_id'], ['pingpong.equipo.id'], ),
    sa.ForeignKeyConstraint(['participantes_partido_id'], ['pingpong.participantes_partido.id'], ),
    schema='pingpong'
    )
    op.create_table('jugador',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('fecha_nacimiento', sa.String(), nullable=True),
    sa.Column('genero', sa.String(), nullable=True),
    sa.Column('ciudad', sa.String(), nullable=True),
    sa.Column('pais', sa.String(), nullable=True),
    sa.Column('asociacion_id', sa.Integer(), nullable=True),
    sa.Column('inscripcion_id', sa.Integer(), nullable=True),
    sa.Column('equipo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asociacion_id'], ['pingpong.asociacion.id'], ),
    sa.ForeignKeyConstraint(['equipo_id'], ['pingpong.equipo.id'], ),
    sa.ForeignKeyConstraint(['inscripcion_id'], ['pingpong.inscripcion.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('partido',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tipo', sa.String(), nullable=True),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('hora', sa.DateTime(), nullable=True),
    sa.Column('fase', sa.String(), nullable=True),
    sa.Column('ronda', sa.String(), nullable=True),
    sa.Column('grupo', sa.String(), nullable=True),
    sa.Column('mesa_id', sa.Integer(), nullable=True),
    sa.Column('resultado_set_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mesa_id'], ['pingpong.mesa.id'], ),
    sa.ForeignKeyConstraint(['resultado_set_id'], ['pingpong.resultado_set.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='pingpong'
    )
    op.create_table('jugadores_inscripcion',
    sa.Column('jugador_id', sa.Integer(), nullable=True),
    sa.Column('inscripcion_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inscripcion_id'], ['pingpong.inscripcion.id'], ),
    sa.ForeignKeyConstraint(['jugador_id'], ['pingpong.jugador.id'], ),
    schema='pingpong'
    )
    op.create_table('jugadores_partido',
    sa.Column('jugador_id', sa.Integer(), nullable=True),
    sa.Column('participantes_partido_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['jugador_id'], ['pingpong.jugador.id'], ),
    sa.ForeignKeyConstraint(['participantes_partido_id'], ['pingpong.participantes_partido.id'], ),
    schema='pingpong'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jugadores_partido', schema='pingpong')
    op.drop_table('jugadores_inscripcion', schema='pingpong')
    op.drop_table('partido', schema='pingpong')
    op.drop_table('jugador', schema='pingpong')
    op.drop_table('equipos_partido', schema='pingpong')
    op.drop_table('mesa', schema='pingpong')
    op.drop_table('inscripcion', schema='pingpong')
    op.drop_table('equipo', schema='pingpong')
    op.drop_table('torneo', schema='pingpong')
    op.drop_table('resultado_set', schema='pingpong')
    op.drop_table('participantes_partido', schema='pingpong')
    op.drop_table('categoria', schema='pingpong')
    op.drop_table('asociacion', schema='pingpong')
    # ### end Alembic commands ###
