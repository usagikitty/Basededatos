from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import participantes_partido as crud

router = APIRouter(prefix="/participantes_partido", tags=["participantes_partido"])

# Obtener todos los participantes
@router.get("/")
def listar_participantes(db: Session = Depends(get_db)):
    return crud.get_participantes(db)

# Obtener un participante por ID
@router.get("/{participante_id}")
def obtener_participante(participante_id: int, db: Session = Depends(get_db)):
    participante = crud.get_participante(db, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return participante

# Crear un nuevo participante
@router.post("/")
def crear_participante(
    rol: str,
    db: Session = Depends(get_db)
):
    participante = crud.create_participante(db, rol=rol)
    if not participante:
        raise HTTPException(status_code=400, detail="No se pudo crear el participante")
    return participante

# Actualizar un participante
@router.put("/{participante_id}")
def actualizar_participante(
    participante_id: int,
    rol: str,
    db: Session = Depends(get_db)
):
    participante = crud.update_participante(
        db,
        participante_id,
        rol=rol
    )
    if not participante:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return participante

# Eliminar un participante
@router.delete("/{participante_id}")
def eliminar_participante(participante_id: int, db: Session = Depends(get_db)):
    participante = crud.delete_participante(db, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return {"detail": "Participante