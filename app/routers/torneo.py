from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import torneo as crud

router = APIRouter(prefix="/torneos", tags=["torneos"])


# Listar todos los torneos
@router.get("/")
def listar_torneos(db: Session = Depends(get_db)):
    return crud.get_torneos(db)


# Obtener un torneo por ID
@router.get("/{torneo_id}")
def obtener_torneo(torneo_id: int, db: Session = Depends(get_db)):
    torneo = crud.get_torneo(db, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo


# Crear un nuevo torneo
@router.post("/")
def crear_torneo(
    nombre: str,
    fecha_inicioinscripcion: str,
    fecha_terminoinscripcion: str,
    fecha_iniciocompe: str,
    fecha_fincompe: str,
    db: Session = Depends(get_db),
):
    return crud.create_torneo(
        db,
        nombre=nombre,
        fecha_inicioinscripcion=fecha_inicioinscripcion,
        fecha_terminoinscripcion=fecha_terminoinscripcion,
        fecha_iniciocompe=fecha_iniciocompe,
        fecha_fincompe=fecha_fincompe,
    )


# Actualizar un torneo
@router.put("/{torneo_id}")
def actualizar_torneo(
    torneo_id: int,
    nombre: Optional[str] = None,
    fecha_inicioinscripcion: Optional[str] = None,
    fecha_terminoinscripcion: Optional[str] = None,
    fecha_iniciocompe: Optional[str] = None,
    fecha_fincompe: Optional[str] = None,
    db: Session = Depends(get_db),
):
    torneo = crud.update_torneo(
        db,
        torneo_id,
        nombre=nombre,
        fecha_inicioinscripcion=fecha_inicioinscripcion,
        fecha_terminoinscripcion=fecha_terminoinscripcion,
        fecha_iniciocompe=fecha_iniciocompe,
        fecha_fincompe=fecha_fincompe,
    )
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo


# Eliminar un torneo
@router.delete("/{torneo_id}")
def eliminar_torneo(torneo_id: int, db: Session = Depends(get_db)):
    torneo = crud.delete_torneo(db, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return {"detail": "Torneo eliminado"}
