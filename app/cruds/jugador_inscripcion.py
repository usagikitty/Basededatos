from sqlalchemy.orm import Session
from sqlalchemy import insert, delete, select
from ..models import jugador_inscripcion


def agregar_jugador_a_inscripcion(
    session: Session, jugador_id: int, inscripcion_id: int
):
    stmt = insert(jugador_inscripcion).values(
        jugador_id=jugador_id, inscripcion_id=inscripcion_id
    )
    session.execute(stmt)
    session.commit()


def obtener_inscripciones_de_jugador(session: Session, jugador_id: int):
    stmt = select(jugador_inscripcion).where(
        jugador_inscripcion.c.jugador_id == jugador_id
    )
    result = session.execute(stmt).fetchall()
    return result


def eliminar_jugador_de_inscripcion(
    session: Session, jugador_id: int, inscripcion_id: int
):
    stmt = delete(jugador_inscripcion).where(
        jugador_inscripcion.c.jugador_id == jugador_id,
        jugador_inscripcion.c.inscripcion_id == inscripcion_id,
    )
    session.execute(stmt)
    session.commit()
