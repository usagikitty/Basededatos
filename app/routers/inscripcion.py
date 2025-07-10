from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import inscripcion as crud

router = APIRouter(prefix="/inscripciones", tags=["inscripciones"])

# Obtener todas las inscripciones
@router.get("/")
def listar_inscripciones(db: Session = Depends(get_db)):
    return crud.get_inscripciones(db)

# Obtener una inscripción por ID
@router.get("/{inscripcion_id}")
def obtener_inscripcion(inscripcion_id: int, db: Session = Depends(get_db)):
    inscripcion = crud.get_inscripcion(db, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return inscripcion

# Crear una nueva inscripción
@router.post("/")
def crear_inscripcion(
    torneo_id: int,
    categoria_id: int,
    db: Session = Depends(get_db)
):
    inscripcion = crud.create_inscripcion(db, torneo_id=torneo_id, categoria_id=categoria_id)
    if not inscripcion:
        raise HTTPException(status_code=400, detail="No se pudo crear la inscripción")
    return inscripcion

# Actualizar una inscripción
@router.put("/{inscripcion_id}")
def actualizar_inscripcion(
    inscripcion_id: int,
    torneo_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    inscripcion = crud.update_inscripcion(
        db,
        inscripcion_id,
        torneo_id=torneo_id,
        categoria_id=categoria_id
    )
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return inscripcion

# Eliminar una inscripción
@router.delete("/{inscripcion_id}")
def eliminar_inscripcion(inscripcion_id: int, db: Session = Depends(get_db)):
    inscripcion = crud.delete_inscripcion(db, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return {"detail": "Inscripción