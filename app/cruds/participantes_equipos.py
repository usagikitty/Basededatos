from sqlalchemy.orm import Session
from sqlalchemy import insert, select, delete
from ..models import participantes_equipos


def agregar_equipo_a_partido(session: Session, participantes_partido_id: int, equipo_id: int):
    """Agrega una relación entre un equipo y un participantes_partido."""
    stmt = insert(participantes_equipos).values(
        participantes_partido_id=participantes_partido_id,
        equipo_id=equipo_id
    )
    session.execute(stmt)
    session.commit()


def obtener_equipos_de_partido(session: Session, participantes_partido_id: int):
    """Obtiene todos los equipos asociados a un participantes_partido."""
    stmt = select(participantes_equipos).where(
        participantes_equipos.c.participantes_partido_id == participantes_partido_id
    )
    result = session.execute(stmt).fetchall()
    return result


def eliminar_equipo_de_partido(session: Session, participantes_partido_id: int, equipo_id: int):
    """Elimina la relación entre un equipo y un participantes_partido."""
    stmt = delete(participantes_equipos).where(
        participantes_equipos.c.participantes_partido_id == participantes_partido_id,
        participantes_equipos.c.equipo_id == equipo_id
    )
    session.execute(stmt)
    session.commit()
