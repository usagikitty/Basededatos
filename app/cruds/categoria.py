from sqlalchemy.orm import Session
from ..models import Categoria

def create_categoria(session: Session, nombre: str, edad_min: int, edad_max: int, genero: str, sets_partido: str, puntos_set: int):
    categoria = Categoria(nombre=nombre, edad_min=edad_min, edad_max=edad_max, genero=genero, sets_partido=sets_partido, puntos_set=puntos_set)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def get_categorias(session: Session):
    return session.query(Categoria).all()

def get_categoria(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)

def update_categoria(session: Session, categoria_id: int, nombre=None, edad_min=None, edad_max=None, genero=None, sets_partido=None, puntos_set=None):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return None
    if nombre: categoria.nombre = nombre
    if edad_min: categoria.edad_min = edad_min
    if edad_max: categoria.edad_max = edad_max
    if genero: categoria.genero = genero
    if sets_partido: categoria.sets_partido = sets_partido
    if puntos_set: categoria.puntos_set = puntos_set
    session.commit()
    session.refresh(categoria)
    return categoria

def delete_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        session.delete(categoria)
        session.commit()
    return categoria
