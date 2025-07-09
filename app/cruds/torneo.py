from typing import Optional
from sqlalchemy.orm import Session
from ..models import Torneo


# Crear un nuevo torneo
def create_torneo(
    session: Session,
    nombre: str,
    fecha_inicioinscripcion: str,
    fecha_terminoinscripcion: str,
    fecha_iniciocompe: str,
    fecha_fincompe: str,
):
    torneo = Torneo(
        nombre=nombre,
        fecha_inicioinscripcion=fecha_inicioinscripcion,
        fecha_terminoinscripcion=fecha_terminoinscripcion,
        fecha_iniciocompe=fecha_iniciocompe,
        fecha_fincompe=fecha_fincompe,
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
    fecha_inicioinscripcion: Optional[str] = None,
    fecha_terminoinscripcion: Optional[str] = None,
    fecha_iniciocompe: Optional[str] = None,
    fecha_fincompe: Optional[str] = None,
):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        if nombre is not None:
            torneo.nombre = nombre
        if fecha_inicioinscripcion is not None:
            torneo.fecha_inicioinscripcion = fecha_inicioinscripcion
        if fecha_terminoinscripcion is not None:
            torneo.fecha_terminoinscripcion = fecha_terminoinscripcion
        if fecha_iniciocompe is not None:
            torneo.fecha_iniciocompe = fecha_iniciocompe
        if fecha_fincompe is not None:
            torneo.fecha_fincompe = fecha_fincompe

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
