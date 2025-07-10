from typing import Optional
from datetime import datetime, date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import partido as crud

router = APIRouter(prefix="/partidos", tags=["partidos"])

# Obtener todos los partidos
@router.get("/")
def listar_partidos(db: Session = Depends(get_db)):
    return crud.get_partidos(db)

# Obtener un partido por ID
@router.get("/{partido_id}")
def obtener_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = crud.get_partido(db, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

# Crear un nuevo partido
@router.post("/")
def crear_partido(
    tipo: str,
    fecha: date,
    hora: datetime,
    fase: str,
    ronda: str,
    grupo: str,
    mesa_id: int,
    resultado_set_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    partido = crud.create_partido(
        db,
        tipo=tipo,
        fecha=fecha,
        hora=hora,
        fase=fase,
        ronda=ronda,
        grupo=grupo,
        mesa_id=mesa_id,
        resultado_set_id=resultado_set_id
    )
    if not partido:
        raise HTTPException(status_code=400, detail="No se pudo crear el partido")
    return partido

# Actualizar un partido
@router.put("/{partido_id}")
def actualizar_partido(
    partido_id: int,
    tipo: Optional[str] = None,
    fase: Optional[str] = None,
    db: Session = Depends(get_db)
):
    partido = crud.update_partido(
        db,
        partido_id,
        tipo=tipo,
        fase=fase
    )
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

# Eliminar un partido
@router.delete("/{partido_id}")
def eliminar_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = crud.delete_partido(db, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return {"detail": "Partido eliminado"}