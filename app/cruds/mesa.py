from sqlalchemy.orm import Session
from ..models import Mesa

def create_mesa(session: Session, numero_mesa: int, torneo_id: int):
    mesa = Mesa(numero_mesa=numero_mesa, torneo_id=torneo_id)
    session.add(mesa)
    session.commit()
    session.refresh(mesa)
    return mesa

def get_mesas(session: Session):
    return session.query(Mesa).all()

def get_mesa(session: Session, mesa_id: int):
    return session.get(Mesa, mesa_id)

def update_mesa(session: Session, mesa_id: int, numero_mesa=None, torneo_id=None):
    mesa = session.get(Mesa, mesa_id)
    if not mesa:
        return None
    if numero_mesa: mesa.numero_mesa = numero_mesa
    if torneo_id: mesa.torneo_id = torneo_id
    session.commit()
    session.refresh(mesa)
    return mesa

def delete_mesa(session: Session, mesa_id: int):
    mesa = session.get(Mesa, mesa_id)
    if mesa:
        session.delete(mesa)
        session.commit()
    return mesa