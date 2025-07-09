from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import jugador_inscripcion as crud

router = APIRouter(
    prefix="/jugador_inscripcion",
    tags=["jugador_inscripcion"]
)

# Agregar un jugador a una inscripción
@router.post("/")
def agregar_jugador_a_inscripcion(jugador_id: int, inscripcion_id: int, db: Session = Depends(get_db)):
    crud.agregar_jugador_a_inscripcion(db, jugador_id, inscripcion_id)
    return {"detail": "Jugador agregado a la inscripción correctamente"}

# Obtener todas las inscripciones de un jugador
@router.get("/jugador/{jugador_id}")
def obtener_inscripciones_de_jugador(jugador_id: int, db: Session = Depends(get_db)):
    relaciones = crud.obtener_inscripciones_de_jugador(db, jugador_id)
    return [{"jugador_id": r.jugador_id, "inscripcion_id": r.inscripcion_id} for r in relaciones]

# Eliminar un jugador de una inscripción
@router.delete("/")
def eliminar_jugador_de_inscripcion(jugador_id: int, inscripcion_id: int, db: Session = Depends(get_db)):
    crud.eliminar_jugador_de_inscripcion(db, jugador_id, inscripcion_id)
    return {"detail": "Relación jugador-inscripción eliminada correctamente"}
