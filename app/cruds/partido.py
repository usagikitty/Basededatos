from sqlalchemy.orm import Session
from datetime import datetime, date
from ..models import Partido
from typing import Optional

def create_partido(session: Session, tipo: str, fecha: date, hora: datetime, fase: str, ronda: str, grupo: str, mesa_id: int, resultado_set_id: Optional[int] = None):
    partido = Partido(
        tipo=tipo,
        fecha=fecha,
        hora=hora,
        fase=fase,
        ronda=ronda,
        grupo=grupo,
        mesa_id=mesa_id,
        resultado_set_id=resultado_set_id
    )
    session.add(partido)
    session.commit()
    session.refresh(partido)
    return partido

def get_partidos(session: Session):
    return session.query(Partido).all()

def get_partido(session: Session, partido_id: int):
    return session.get(Partido, partido_id)

def update_partido(session: Session, partido_id: int, fecha: Optional[date] = None, hora: Optional[datetime] = None, ronda: Optional[str] = None, grupo: Optional[str] = None, mesa_id: Optional[int] = None, resultado_set_id: Optional[int] = None, tipo: Optional[str] = None, fase: Optional[str] = None):
    partido = session.get(Partido, partido_id)
    if partido:
        if tipo is not None:
            partido.tipo = tipo
        if fecha is not None:
            partido.fecha = fecha
        if hora is not None:
            partido.hora = hora
        if fase is not None:
            partido.fase = fase
        if ronda is not None:
            partido.ronda = ronda
        if grupo is not None:
            partido.grupo = grupo
        if mesa_id is not None:
            partido.mesa_id = mesa_id
        if resultado_set_id is not None:
            partido.resultado_set_id = resultado_set_id

        session.commit()
        session.refresh(partido)
    return partido

def delete_partido(session: Session, partido_id: int):
    partido = session.get(Partido, partido_id)
    if partido:
        session.delete(partido)
        session.commit()
    return partido