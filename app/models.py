from datetime import date, datetime
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, ForeignKey, Table
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
SCHEMA = 'pingpong'

# Tablas de asociación para relaciones muchos a muchos
jugador_inscripcion = Table(
    'jugador_inscripcion', Base.metadata,
    Column('jugador_id', Integer, ForeignKey(f'{SCHEMA}.jugador.id')),
    Column('inscripcion_id', Integer, ForeignKey(f'{SCHEMA}.inscripcion.id')),
    schema=SCHEMA
)

participantes_jugadores = Table(
    'participantes_jugadores', Base.metadata,
    Column('participantes_partido_id', Integer, ForeignKey(f'{SCHEMA}.participantes_partido.id')),
    Column('jugador_id', Integer, ForeignKey(f'{SCHEMA}.jugador.id')),
    schema=SCHEMA
)

participantes_equipos = Table(
    'participantes_equipos', Base.metadata,
    Column('participantes_partido_id', Integer, ForeignKey(f'{SCHEMA}.participantes_partido.id')),
    Column('equipo_id', Integer, ForeignKey(f'{SCHEMA}.equipo.id')),
    schema=SCHEMA
)

class Jugador(Base):
    __tablename__ = 'jugador'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    fecha_nacimiento = Column(String)
    genero = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    asociacion_id = Column(Integer, ForeignKey(f'{SCHEMA}.asociacion.id'))
    asociacion = relationship('Asociacion', back_populates='jugadores')
    inscripcion_id = Column(Integer, ForeignKey(f'{SCHEMA}.inscripcion.id'))
    inscripcion = relationship('Inscripcion', back_populates='jugadores')
    equipo_id = Column(Integer, ForeignKey(f'{SCHEMA}.equipo.id'))
    equipo = relationship('Equipo', back_populates='jugadores')
    participantes_partido = relationship(
        'Participantes_partido',
        secondary=participantes_jugadores,
        back_populates='jugadores'
    )

class Torneo(Base):
    __tablename__ = 'torneo'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    fecha_inicioinscripcion = Column(String)
    fecha_terminoinscripcion = Column(String)
    fecha_iniciocompe = Column(String)
    fecha_fincompe = Column(String)
    inscripciones = relationship('Inscripcion', back_populates='torneo')
    equipos = relationship('Equipo', back_populates='torneo')
    mesas = relationship('Mesa', back_populates='torneo')

class Asociacion(Base):
    __tablename__ = 'asociacion'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    jugadores = relationship('Jugador', back_populates='asociacion')

class Mesa(Base):
    __tablename__ = 'mesa'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_mesa = Column(Integer)
    torneo_id = Column(Integer, ForeignKey(f'{SCHEMA}.torneo.id'))
    torneo = relationship('Torneo', back_populates='mesas')
    partidos = relationship('Partido', back_populates='mesa')

class Categoria(Base):
    __tablename__ = 'categoria'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    edad_min = Column(Integer)
    edad_max = Column(Integer)
    genero = Column(String)
    sets_partido = Column(String)
    puntos_set = Column(Integer)
    inscripciones = relationship('Inscripcion', back_populates='categoria')
    equipos = relationship('Equipo', back_populates='categoria')

class Inscripcion(Base):
    __tablename__ = 'inscripcion'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugadores = relationship('Jugador', back_populates='inscripcion')
    torneo_id = Column(Integer, ForeignKey(f'{SCHEMA}.torneo.id'))
    torneo = relationship('Torneo', back_populates='inscripciones')
    categoria_id = Column(Integer, ForeignKey(f'{SCHEMA}.categoria.id'))
    categoria = relationship('Categoria', back_populates='inscripciones')

class Equipo(Base):
    __tablename__ = 'equipo'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugadores = relationship('Jugador', back_populates='equipo')
    torneo_id = Column(Integer, ForeignKey(f'{SCHEMA}.torneo.id'))
    torneo = relationship('Torneo', back_populates='equipos')
    categoria_id = Column(Integer, ForeignKey(f'{SCHEMA}.categoria.id'))
    categoria = relationship('Categoria', back_populates='equipos')
    participantes_partido = relationship(
        'Participantes_partido',
        secondary=participantes_equipos,
        back_populates='equipos'
    )

class Participantes_partido(Base):
    __tablename__ = 'participantes_partido'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String)
    jugadores = relationship(
        'Jugador',
        secondary=participantes_jugadores,
        back_populates='participantes_partido'
    )
    equipos = relationship(
        'Equipo',
        secondary=participantes_equipos,
        back_populates='participantes_partido'
    )

class Partido(Base):
    __tablename__ = 'partido'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    fecha = Column(Date)
    hora = Column(DateTime)
    fase = Column(String)
    ronda = Column(String)
    grupo = Column(String)
    mesa_id = Column(Integer, ForeignKey(f'{SCHEMA}.mesa.id'))
    mesa = relationship('Mesa', back_populates='partidos')
    resultado_set_id = Column(Integer, ForeignKey(f'{SCHEMA}.resultado_set.id'))
    resultado_set = relationship('Resultado_set', uselist=False, back_populates='partido')

class Resultado_set(Base):
    __tablename__ = 'resultado_set'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_set = Column(Integer)
    puntos_jugA = Column(Integer)
    puntos_equipA = Column(Integer)
    puntos_jugB = Column(Integer)
    puntos_equipB = Column(Integer)
    partido = relationship('Partido', back_populates='resultado_set')