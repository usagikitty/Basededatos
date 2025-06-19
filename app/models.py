from datetime import date, datetime
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, ForeignKey, Table
)
from sqlalchemy.orm import relationship
from .db import Base

CASCADE_ALL_DELETE_ORPHAN = "all, delete-orphan"

# Tablas de asociación para relaciones muchos a muchos
jugador_inscripcion = Table(
    'jugador_inscripcion', Base.metadata,
    Column('jugador_id', Integer, ForeignKey('jugador.id')),
    Column('inscripcion_id', Integer, ForeignKey('inscripcion.id'))
)

participantes_jugadores = Table(
    'participantes_jugadores', Base.metadata,
    Column('participantes_partido_id', Integer, ForeignKey('participantes_partido.id')),
    Column('jugador_id', Integer, ForeignKey('jugador.id'))
)

participantes_equipos = Table(
    'participantes_equipos', Base.metadata,
    Column('participantes_partido_id', Integer, ForeignKey('participantes_partido.id')),
    Column('equipo_id', Integer, ForeignKey('equipo.id'))
)

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    fecha_nacimiento = Column(String)
    genero = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    asociacion_id = Column(Integer, ForeignKey('asociacion.id'))
    asociacion = relationship('Asociacion', back_populates='jugadores')
    # Removed inscripcion_id and equipo_id to avoid conflicting relationships
    inscripcion = relationship('Inscripcion', secondary=jugador_inscripcion, back_populates='jugadores')
    equipo = relationship('Equipo', back_populates='jugadores')
    participantes_partido = relationship(
        'ParticipantesPartido',
        secondary=participantes_jugadores,
        back_populates='jugadores'
    )

class Torneo(Base):
    __tablename__ = 'torneo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    fecha_inicioinscripcion = Column(String)
    fecha_terminoinscripcion = Column(String)
    inscripciones = relationship('Inscripcion', back_populates='torneo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    equipos = relationship('Equipo', back_populates='torneo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    mesas = relationship('Mesa', back_populates='torneo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    equipos = relationship('Equipo', back_populates='torneo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    mesas = relationship('Mesa', back_populates='torneo', cascade=CASCADE_ALL_DELETE_ORPHAN)

class Asociacion(Base):
    __tablename__ = 'asociacion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    jugadores = relationship('Jugador', back_populates='asociacion', cascade=CASCADE_ALL_DELETE_ORPHAN)
    pais = Column(String)
    jugadores = relationship('Jugador', back_populates='asociacion', cascade=CASCADE_ALL_DELETE_ORPHAN)

class Mesa(Base):
    __tablename__ = 'mesa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_mesa = Column(Integer)
    partidos = relationship('Partido', back_populates='mesa', cascade=CASCADE_ALL_DELETE_ORPHAN)
    torneo = relationship('Torneo', back_populates='mesas')
    partidos = relationship('Partido', back_populates='mesa', cascade=CASCADE_ALL_DELETE_ORPHAN)

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    edad_min = Column(Integer)
    edad_max = Column(Integer)
    genero = Column(String)
    inscripciones = relationship('Inscripcion', back_populates='categoria', cascade=CASCADE_ALL_DELETE_ORPHAN)
    equipos = relationship('Equipo', back_populates='categoria', cascade=CASCADE_ALL_DELETE_ORPHAN)
    inscripciones = relationship('Inscripcion', back_populates='categoria', cascade=CASCADE_ALL_DELETE_ORPHAN)
    equipos = relationship('Equipo', back_populates='categoria', cascade=CASCADE_ALL_DELETE_ORPHAN)

class Inscripcion(Base):
    jugadores = relationship('Jugador', secondary=jugador_inscripcion, back_populates='inscripcion', cascade=CASCADE_ALL_DELETE_ORPHAN)
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugadores = relationship('Jugador', secondary=jugador_inscripcion, back_populates='inscripcion', cascade="all, delete")
    torneo_id = Column(Integer, ForeignKey('torneo.id'))
    torneo = relationship('Torneo', back_populates='inscripciones')
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship('Categoria', back_populates='inscripciones')
class Equipo(Base):
    jugadores = relationship('Jugador', back_populates='equipo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    id = Column(Integer, primary_key=True, autoincrement=True)
    jugadores = relationship('Jugador', back_populates='equipo', cascade=CASCADE_ALL_DELETE_ORPHAN)
    torneo_id = Column(Integer, ForeignKey('torneo.id'))
    torneo = relationship('Torneo', back_populates='equipos')
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship('Categoria', back_populates='equipos')
    participantes_partido = relationship(
        'ParticipantesPartido',
        secondary=participantes_equipos,
        back_populates='equipos'
    )

class ParticipantesPartido(Base):
    __tablename__ = 'participantes_partido'
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    fecha = Column(Date)
    hora = Column(DateTime)
    fase = Column(String)
    ronda = Column(String)
    grupo = Column(String)
    mesa_id = Column(Integer, ForeignKey('mesa.id'))
    resultado_set = relationship('ResultadoSet', back_populates='partido', uselist=False, cascade=CASCADE_ALL_DELETE_ORPHAN)
    resultado_set_id = Column(Integer, ForeignKey('resultado_set.id'), unique=True)
    resultado_set = relationship('ResultadoSet', back_populates='partido', uselist=False, cascade=CASCADE_ALL_DELETE_ORPHAN)

class ResultadoSet(Base):
    __tablename__ = 'resultado_set'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_set = Column(Integer)
    puntos_jugA = Column(Integer)
    puntos_equipA = Column(Integer)
    puntos_jugB = Column(Integer)
    puntos_equipB = Column(Integer)
    partido = relationship('Partido', back_populates='resultado_set', uselist=False)