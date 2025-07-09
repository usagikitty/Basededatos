from sqlalchemy.orm import Session
from ..models import Equipo
from typing import Optional

def create_equipo(session: Session, torneo_id: int, categoria_id: int):
    equipo = Equipo(torneo_id=torneo_id, categoria_id=categoria_id)
    session.add(equipo)
    session.commit()
    session.refresh(equipo)
    return equipo

def get_equipos(session: Session):
    return session.query(Equipo).all()

def get_equipo(session: Session, equipo_id: int):
    return session.get(Equipo, equipo_id)

def update_equipo(session: Session, equipo_id: int, torneo_id: Optional[int] = None, categoria_id: Optional[int] = None):
    equipo = session.get(Equipo, equipo_id)
    if equipo:
        if torneo_id is not None:
            equipo.torneo_id = torneo_id
        if categoria_id is not None:
            equipo.categoria_id = categoria_id
        session.commit()
        session.refresh(equipo)
    return equipo

def delete_equipo(session: Session, equipo_id: int):
    equipo = session.get(Equipo, equipo_id)
    if equipo:
        session.delete(equipo)
        session.commit()
    return equipo