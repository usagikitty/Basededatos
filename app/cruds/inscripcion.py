from sqlalchemy.orm import Session
from ..models import Inscripcion
from typing import Optional

def create_inscripcion(session: Session, torneo_id: int, categoria_id: int):
    inscripcion = Inscripcion(torneo_id=torneo_id, categoria_id=categoria_id)
    session.add(inscripcion)
    session.commit()
    session.refresh(inscripcion)
    return inscripcion

def get_inscripciones(session: Session):
    return session.query(Inscripcion).all()

def get_inscripcion(session: Session, inscripcion_id: int):
    return session.get(Inscripcion, inscripcion_id)

def update_inscripcion(session: Session, inscripcion_id: int, torneo_id: Optional[int] = None, categoria_id: Optional[int] = None):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if inscripcion:
        if torneo_id is not None:
            inscripcion.torneo_id = torneo_id
        if categoria_id is not None:
            inscripcion.categoria_id = categoria_id
        session.commit()
        session.refresh(inscripcion)
    return inscripcion

def delete_inscripcion(session: Session, inscripcion_id: int):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if inscripcion:
        session.delete(inscripcion)
        session.commit()
    return inscripcion