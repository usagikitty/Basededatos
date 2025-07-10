from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..cruds import categoria as crud

router = APIRouter(prefix="/categorias", tags=["categorias"])

# Obtener todas las categorías
@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db)

# Obtener una categoría por ID
@router.get("/{categoria_id}")
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# Crear una nueva categoría
@router.post("/")
def crear_categoria(
    nombre: str,
    edad_min: int,
    edad_max: int,
    genero: str,
    sets_partido: str,
    puntos_set: int,
    db: Session = Depends(get_db)
):
    categoria = crud.create_categoria(
        db,
        nombre=nombre,
        edad_min=edad_min,
        edad_max=edad_max,
        genero=genero,
        sets_partido=sets_partido,
        puntos_set=puntos_set
    )
    if not categoria:
        raise HTTPException(status_code=400, detail="No se pudo crear la categoría")
    return categoria

# Actualizar una categoría
@router.put("/{categoria_id}")
def actualizar_categoria(
    categoria_id: int,
    nombre: Optional[str] = None,
    edad_min: Optional[int] = None,
    edad_max: Optional[int] = None,
    genero: Optional[str] = None,
    sets_partido: Optional[str] = None,
    puntos_set: Optional[int] = None,
    db: Session = Depends(get_db)
):
    categoria = crud.update_categoria(
        db,
        categoria_id,
        nombre=nombre,
        edad_min=edad_min,
        edad_max=edad_max,
        genero=genero,
        sets_partido=sets_partido,
        puntos_set=puntos_set
    )
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# Eliminar una categoría
@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.delete_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"detail": "Categoría eliminada"}