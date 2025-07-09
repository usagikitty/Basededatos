from typing import Optional                                                 # permite definir parametros que puedan ser "none"
from fastapi import APIRouter, HTTPException, Depends                       # APIRouter: Utilidad de FastAPI para modularizar rutas. HTTPException: Permite lanzar errores HTTP (por ejemplo, 404)
from sqlalchemy.orm import Session                                          # 
from ..db import get_db 
from ..cruds import jugador as crud                                         # Se importa el CRUD de jugador desde app/cruds/jugador.py

router = APIRouter(prefix="/jugadores", tags=["jugadores"])                 #

# Listar todos los jugadores
@router.get("/")
def listar_jugadores(db: Session = Depends(get_db)):
    return crud.get_jugadores(db)

# Obtener un jugador por ID
@router.get("/{jugador_id}")
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud.get_jugador(db, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

# Crear un nuevo jugador (faltaban todos los campos requeridos)
@router.post("/")
def crear_jugador(
    nombre: str,
    fecha_nacimiento: str,
    genero: str,
    ciudad: str,
    pais: str,
    asociacion_id: Optional[int] = None,
    inscripcion_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return crud.create_jugador(
        db,
        nombre=nombre,
        fecha_nacimiento=fecha_nacimiento,
        genero=genero,
        ciudad=ciudad,
        pais=pais,
        asociacion_id=asociacion_id,
        inscripcion_id=inscripcion_id,
        equipo_id=equipo_id,
    )

# Actualizar campos del jugador
@router.put("/{jugador_id}")
def actualizar_jugador(
    jugador_id: int,
    nombre: Optional[str] = None,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    equipo_id: Optional[int] = None,
    asociacion_id: Optional[int] = None,
    inscripcion_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    jugador = crud.update_jugador(
        db,
        jugador_id,
        nombre=nombre,
        ciudad=ciudad,
        pais=pais,
        equipo_id=equipo_id,
        asociacion_id=asociacion_id,
        inscripcion_id=inscripcion_id,
    )
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

# Eliminar jugador
@router.delete("/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud.delete_jugador(db, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return {"detail": "Jugador eliminado"}
