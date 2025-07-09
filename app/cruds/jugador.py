from typing import Optional             # indica que un parametro puede ser "none"
from datetime import datetime           # sirve para manejar fechas y horas  
from sqlalchemy.orm import Session      # es la secion activa para manejar la base de datos 
from ..models import Jugador            # Es el modelo de datos definido en models.py, que representa una tabla en la base de datos

# se crea un nuevo usuario en la base de datos
def create_jugador(session: Session, nombre: str, fecha_nacimiento: str, genero: str, ciudad: str, pais: str, asociacion_id: Optional[int] = None, inscripcion_id: Optional[int] = None, equipo_id: Optional[int] = None, ):
    jugador = Jugador(                                          # se crea una instacia de la clase jugador
        nombre=nombre,
        fecha_nacimiento=fecha_nacimiento,
        genero=genero,
        ciudad=ciudad, 
        pais=pais,
        asociacion_id=asociacion_id,
        inscripcion_id=inscripcion_id,
        equipo_id=equipo_id,
    )
    session.add(jugador)                                        # se agrega el objeto a la secion actual (no se agrega a la tabla solo queda como pendiente)
    session.commit()                                            # aqui se inserta a la tabla, si hay algun error lanza una excepcion
    session.refresh(jugador)                                    # se actualiza el objeto jugador
    return jugador                              

def get_jugadores(session: Session):                            # se obtiene todos los jugadores
    return session.query(Jugador).all()

def get_jugador(session: Session, jugador_id: int):             # se obtiene un jugador por su id
    return session.get(Jugador, jugador_id)

# se actualizaran los datos de un jugador que se proporcione
def update_jugador(session: Session, jugador_id: int, nombre: Optional[str] = None, ciudad: Optional[str] = None, pais: Optional[str] = None, equipo_id: Optional[int] = None, asociacion_id: Optional[int] = None, inscripcion_id: Optional[int] = None,):
    jugador = session.get(Jugador, jugador_id)
    if jugador:
        if nombre is not None:
            jugador.nombre = nombre
        if ciudad is not None:
            jugador.ciudad = ciudad
        if pais is not None:
            jugador.pais = pais
        if equipo_id is not None:
            jugador.equipo_id = equipo_id
        if asociacion_id is not None:
            jugador.asociacion_id = asociacion_id
        if inscripcion_id is not None:
            jugador.inscripcion_id = inscripcion_id

        session.commit()
        session.refresh(jugador)
    return jugador

def delete_jugador(session: Session, jugador_id: int):      # se elimina un jugador por su id
    jugador = session.get(Jugador, jugador_id)
    if jugador:
        session.delete(jugador)
        session.commit()
    return jugador
