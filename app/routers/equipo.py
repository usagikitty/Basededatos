from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import equipo as crud

router = APIRouter(prefix="/equipos", tags=["equipos"])

# Obtener todos los equipos
@router.get("/")
def listar_equipos(db: Session = Depends(get_db)):
    return crud.get_equipos(db)

# Obtener un equipo por ID
@router.get("/{equipo_id}")
def obtener_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = crud.get_equipo(db, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

# Crear un nuevo equipo
@router.post("/")
def crear_equipo(
    torneo_id: int,
    categoria_id: int,
    db: Session = Depends(get_db)
):
    equipo = crud.create_equipo(db, torneo_id=torneo_id, categoria_id=categoria_id)
    if not equipo:
        raise HTTPException(status_code=400, detail="No se pudo crear el equipo")
    return equipo

# Actualizar un equipo
@router.put("/{equipo_id}")
def actualizar_equipo(
    equipo_id: int,
    torneo_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    equipo = crud.update_equipo(
        db,
        equipo_id,
        torneo_id=torneo_id,
        categoria_id=categoria_id
    )
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

# Eliminar un equipo
@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = crud.delete_equipo(db, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return {"detail": "Equipo eliminado"}