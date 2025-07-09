from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import participantes_jugadores as crud

router = APIRouter(
    prefix="/participantes_jugadores",
    tags=["participantes_jugadores"]
)

# Agregar un jugador a un participantes_partido
@router.post("/")
def agregar_jugador_a_partido(partido_id: int, jugador_id: int, db: Session = Depends(get_db)):
    crud.agregar_jugador_a_partido(db, participantes_partido_id=partido_id, jugador_id=jugador_id)
    return {"detail": "Jugador agregado al partido correctamente"}

# Obtener todos los jugadores de un participantes_partido
@router.get("/partido/{partido_id}")
def obtener_jugadores_de_partido(partido_id: int, db: Session = Depends(get_db)):
    relaciones = crud.obtener_jugadores_de_partido(db, participantes_partido_id=partido_id)
    return [{"participantes_partido_id": r.participantes_partido_id, "jugador_id": r.jugador_id} for r in relaciones]

# Eliminar un jugador de un participantes_partido
@router.delete("/")
def eliminar_jugador_de_partido(partido_id: int, jugador_id: int, db: Session = Depends(get_db)):
    crud.eliminar_jugador_de_partido(db, participantes_partido_id=partido_id, jugador_id=jugador_id)
    return {"detail": "Relación jugador-partido eliminada correctamente"}
