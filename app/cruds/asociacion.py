from sqlalchemy.orm import Session
from ..models import Asociacion

def create_asociacion(session: Session, nombre: str, ciudad: str, pais: str):
    asociacion = Asociacion(nombre=nombre, ciudad=ciudad, pais=pais)
    session.add(asociacion)
    session.commit()
    session.refresh(asociacion)
    return asociacion

def get_asociaciones(session: Session):
    return session.query(Asociacion).all()

def get_asociacion(session: Session, asociacion_id: int):
    return session.get(Asociacion, asociacion_id)

def update_asociacion(session: Session, asociacion_id: int, nombre=None, ciudad=None, pais=None):
    asociacion = session.get(Asociacion, asociacion_id)
    if not asociacion:
        return None
    if nombre: asociacion.nombre = nombre
    if ciudad: asociacion.ciudad = ciudad
    if pais: asociacion.pais = pais
    session.commit()
    session.refresh(asociacion)
    return asociacion

def delete_asociacion(session: Session, asociacion_id: int):
    asociacion = session.get(Asociacion, asociacion_id)
    if asociacion:
        session.delete(asociacion)
        session.commit()
    return asociacion