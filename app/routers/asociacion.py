# app/routers/asociacion.py

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import asociacion as crud

router = APIRouter(prefix="/asociaciones", tags=["asociaciones"])

# Obtener todas las asociaciones
@router.get("/")
def listar_asociaciones(db: Session = Depends(get_db)):
    return crud.get_asociaciones(db)

# Obtener una asociación por ID
@router.get("/{asociacion_id}")
def obtener_asociacion(asociacion_id: int, db: Session = Depends(get_db)):
    asociacion = crud.get_asociacion(db, asociacion_id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return asociacion

# Crear una nueva asociación
@router.post("/")
def crear_asociacion(nombre: str, ciudad: str, pais: str, db: Session = Depends(get_db)):
    return crud.create_asociacion(db, nombre=nombre, ciudad=ciudad, pais=pais)

# Actualizar una asociación
@router.put("/{asociacion_id}")
def actualizar_asociacion(
    asociacion_id: int,
    nombre: Optional[str] = None,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    db: Session = Depends(get_db),
):
    asociacion = crud.update_asociacion(db, asociacion_id, nombre=nombre, ciudad=ciudad, pais=pais)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return asociacion

# Eliminar una asociación
@router.delete("/{asociacion_id}")
def eliminar_asociacion(asociacion_id: int, db: Session = Depends(get_db)):
    asociacion = crud.delete_asociacion(db, asociacion_id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return {"detail": "Asociación eliminada"}
