from sqlalchemy.orm import Session
from ..models import Resultado_set

def create_resultado(session: Session, numero_set: int, puntos_jugA: int, puntos_equipA: int, puntos_jugB: int, puntos_equipB: int):
    resultado = Resultado_set(
        numero_set=numero_set,
        puntos_jugA=puntos_jugA,
        puntos_equipA=puntos_equipA,
        puntos_jugB=puntos_jugB,
        puntos_equipB=puntos_equipB
    )
    session.add(resultado)
    session.commit()
    session.refresh(resultado)
    return resultado

def get_resultados(session: Session):
    return session.query(Resultado_set).all()

def get_resultado(session: Session, resultado_id: int):
    return session.get(Resultado_set, resultado_id)

def update_resultado(session: Session, resultado_id: int, puntos_jugA: int):
    resultado = session.get(Resultado_set, resultado_id)
    if resultado:
        resultado.puntos_jugA = puntos_jugA
        session.commit()
        session.refresh(resultado)
    return resultado

def delete_resultado(session: Session, resultado_id: int):
    resultado = session.get(Resultado_set, resultado_id)
    if resultado:
        session.delete(resultado)
        session.commit()
    return resultado