from sqlalchemy.orm import Session
from ..models import Participantes_partido

def create_participante(session: Session, rol: str):
    participante = Participantes_partido(rol=rol)
    session.add(participante)
    session.commit()
    session.refresh(participante)
    return participante

def get_participantes(session: Session):
    return session.query(Participantes_partido).all()

def get_participante(session: Session, participante_id: int):
    return session.get(Participantes_partido, participante_id)

def update_participante(session: Session, participante_id: int, rol: str):
    participante = session.get(Participantes_partido, participante_id)
    if participante:
        participante.rol = rol
        session.commit()
        session.refresh(participante)
    return participante

def delete_participante(session: Session, participante_id: int):
    participante = session.get(Participantes_partido, participante_id)
    if participante:
        session.delete(participante)
        session.commit()
    return participante