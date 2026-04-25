from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{usuario_id}", response_model=List[schemas.FavoritoResponse])
def obtener_favoritos(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(models.Favorito).filter(models.Favorito.usuario_id == usuario_id).all()

@router.post("/", response_model=schemas.FavoritoResponse)
def agregar_favorito(favorito: schemas.FavoritoCreate, usuario_id: int, db: Session = Depends(get_db)):
    existente = db.query(models.Favorito).filter(
        models.Favorito.usuario_id == usuario_id,
        models.Favorito.receta_id == favorito.receta_id
    ).first()
    if existente:
        raise HTTPException(status_code=400, detail="Ya está en favoritos")
    nuevo = models.Favorito(usuario_id=usuario_id, receta_id=favorito.receta_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/{favorito_id}")
def eliminar_favorito(favorito_id: int, db: Session = Depends(get_db)):
    favorito = db.query(models.Favorito).filter(models.Favorito.id == favorito_id).first()
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    db.delete(favorito)
    db.commit()
    return {"mensaje": "Favorito eliminado correctamente"}