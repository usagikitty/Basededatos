from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import resultado as crud

router = APIRouter(prefix="/resultados", tags=["resultados"])

# Obtener todos los resultados
@router.get("/")
def listar_resultados(db: Session = Depends(get_db)):
    return crud.get_resultados(db)

# Obtener un resultado por ID
@router.get("/{resultado_id}")
def obtener_resultado(resultado_id: int, db: Session = Depends(get_db)):
    resultado = crud.get_resultado(db, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return resultado

# Crear un nuevo resultado
@router.post("/")
def crear_resultado(
    numero_set: int,
    puntos_jugA: int,
    puntos_equipA: int,
    puntos_jugB: int,
    puntos_equipB: int,
    db: Session = Depends(get_db)
):
    resultado = crud.create_resultado(
        db,
        numero_set=numero_set,
        puntos_jugA=puntos_jugA,
        puntos_equipA=puntos_equipA,
        puntos_jugB=puntos_jugB,
        puntos_equipB=puntos_equipB
    )
    if not resultado:
        raise HTTPException(status_code=400, detail="No se pudo crear el resultado")
    return resultado

# Actualizar un resultado (solo puntos_jugA según tu función)
@router.put("/{resultado_id}")
def actualizar_resultado(
    resultado_id: int,
    puntos_jugA: int,
    db: Session = Depends(get_db)
):
    resultado = crud.update_resultado(
        db,
        resultado_id,
        puntos_jugA=puntos_jugA
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return resultado

# Eliminar un resultado
@router.delete("/{resultado_id}")
def eliminar_resultado(resultado_id: int, db: Session = Depends(get_db)):
    resultado = crud.delete_resultado(db, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return {"detail": "Resultado