from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import participantes_equipos as crud

router = APIRouter(
    prefix="/participantes_equipos",
    tags=["participantes_equipos"]
)

# Agregar un equipo a un participantes_partido
@router.post("/")
def agregar_equipo_a_partido(partido_id: int, equipo_id: int, db: Session = Depends(get_db)):
    crud.agregar_equipo_a_partido(db, participantes_partido_id=partido_id, equipo_id=equipo_id)
    return {"detail": "Equipo agregado al partido correctamente"}

# Obtener todos los equipos de un participantes_partido
@router.get("/partido/{partido_id}")
def obtener_equipos_de_partido(partido_id: int, db: Session = Depends(get_db)):
    relaciones = crud.obtener_equipos_de_partido(db, participantes_partido_id=partido_id)
    return [{"participantes_partido_id": r.participantes_partido_id, "equipo_id": r.equipo_id} for r in relaciones]

# Eliminar un equipo de un participantes_partido
@router.delete("/")
def eliminar_equipo_de_partido(partido_id: int, equipo_id: int, db: Session = Depends(get_db)):
    crud.eliminar_equipo_de_partido(db, participantes_partido_id=partido_id, equipo_id=equipo_id)
    return {"detail": "Relación equipo-partido eliminada correctamente"}
