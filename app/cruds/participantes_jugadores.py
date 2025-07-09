from sqlalchemy.orm import Session
from sqlalchemy import insert, select, delete
from ..models import participantes_jugadores


def agregar_jugador_a_partido(session: Session, participantes_partido_id: int, jugador_id: int):
    stmt = insert(participantes_jugadores).values(
        participantes_partido_id=participantes_partido_id,
        jugador_id=jugador_id
    )
    session.execute(stmt)
    session.commit()


def obtener_jugadores_de_partido(session: Session, participantes_partido_id: int):
    stmt = select(participantes_jugadores).where(
        participantes_jugadores.c.participantes_partido_id == participantes_partido_id
    )
    result = session.execute(stmt).fetchall()
    return result


def eliminar_jugador_de_partido(session: Session, participantes_partido_id: int, jugador_id: int):
    stmt = delete(participantes_jugadores).where(
        participantes_jugadores.c.participantes_partido_id == participantes_partido_id,
        participantes_jugadores.c.jugador_id == jugador_id
    )
    session.execute(stmt)
    session.commit()
