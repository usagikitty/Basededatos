from typing import Optional
from sqlalchemy.orm import Session
from ..models import Torneo
from datetime import datetime


# Crear un nuevo torneo
def create_torneo(
    session: Session,
    nombre: str,
    fecha_inicioinscripcion: datetime,
    fecha_terminoinscripcion: datetime,
    fecha_iniciocompe: datetime,
    fecha_fincompe: datetime,
):
    torneo = Torneo(
        nombre=nombre,
        fecha_inicioinscripcion=fecha_inicioinscripcion.date(),
        fecha_terminoinscripcion=fecha_terminoinscripcion.date(),
        fecha_iniciocompe=fecha_iniciocompe.date(),
        fecha_fincompe=fecha_fincompe.date(),
    )
    session.add(torneo)
    session.commit()
    session.refresh(torneo)
    return torneo


# Obtener todos los torneos
def get_torneos(session: Session):
    return session.query(Torneo).all()


# Obtener un torneo por ID
def get_torneo(session: Session, torneo_id: int):
    return session.get(Torneo, torneo_id)


# Actualizar datos de un torneo
def update_torneo(
    session: Session,
    torneo_id: int,
    nombre: Optional[str] = None,
    fecha_inicioinscripcion: Optional[datetime] = None,
    fecha_terminoinscripcion: Optional[datetime] = None,
    fecha_iniciocompe: Optional[datetime] = None,
    fecha_fincompe: Optional[datetime] = None,
):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        if nombre is not None:
            torneo.nombre = nombre
        if fecha_inicioinscripcion is not None:
            torneo.fecha_inicioinscripcion = fecha_inicioinscripcion.date()
        if fecha_terminoinscripcion is not None:
            torneo.fecha_terminoinscripcion = fecha_terminoinscripcion.date()
        if fecha_iniciocompe is not None:
            torneo.fecha_iniciocompe = fecha_iniciocompe.date()
        if fecha_fincompe is not None:
            torneo.fecha_fincompe = fecha_fincompe.date()

        session.commit()
        session.refresh(torneo)
    return torneo


# Eliminar un torneo por ID
def delete_torneo(session: Session, torneo_id: int):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        session.delete(torneo)
        session.commit()
    return torneo
