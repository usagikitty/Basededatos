from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import mesa as crud

router = APIRouter(prefix="/mesas", tags=["mesas"])

# Obtener todas las mesas
@router.get("/")
def listar_mesas(db: Session = Depends(get_db)):
    return crud.get_mesas(db)

# Obtener una mesa por ID
@router.get("/{mesa_id}")
def obtener_mesa(mesa_id: int, db: Session = Depends(get_db)):
    mesa = crud.get_mesa(db, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return mesa

# Crear una nueva mesa
@router.post("/")
def crear_mesa(
    numero_mesa: int,
    torneo_id: int,
    db: Session = Depends(get_db)
):
    mesa = crud.create_mesa(db, numero_mesa=numero_mesa, torneo_id=torneo_id)
    if not mesa:
        raise HTTPException(status_code=400, detail="No se pudo crear la mesa")
    return mesa

# Actualizar una mesa
@router.put("/{mesa_id}")
def actualizar_mesa(
    mesa_id: int,
    numero_mesa: Optional[int] = None,
    torneo_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    mesa = crud.update_mesa(
        db,
        mesa_id,
        numero_mesa=numero_mesa,
        torneo_id=torneo_id
    )
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return mesa

# Eliminar una mesa
@router.delete("/{mesa_id}")
def eliminar_mesa(mesa_id: int, db: Session = Depends(get_db)):
    mesa = crud.delete_mesa(db, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"detail": "Mesa