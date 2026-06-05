from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{usuario_id}")
def obtener_favoritos(usuario_id: int, db: Session = Depends(get_db)):
    favoritos = db.query(models.Favorito).filter(
        models.Favorito.usuario_id == usuario_id
    ).all()
    # Filtrar favoritos cuya receta aún existe
    resultado = []
    for f in favoritos:
        receta = db.query(models.Receta).filter(models.Receta.id == f.receta_id).first()
        if receta:
            resultado.append({"id": f.id, "usuario_id": f.usuario_id, "receta_id": f.receta_id})
    return resultado

@router.post("/")
def agregar_favorito(favorito: schemas.FavoritoCreate, usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    receta = db.query(models.Receta).filter(models.Receta.id == favorito.receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    existente = db.query(models.Favorito).filter(
        models.Favorito.usuario_id == usuario_id,
        models.Favorito.receta_id == favorito.receta_id
    ).first()
    if existente:
        db.delete(existente)
        db.commit()
        return {"mensaje": "Eliminado de favoritos", "action": "removed"}
    nuevo = models.Favorito(usuario_id=usuario_id, receta_id=favorito.receta_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Añadido a favoritos", "action": "added", "id": nuevo.id}

@router.delete("/{favorito_id}")
def eliminar_favorito(favorito_id: int, db: Session = Depends(get_db)):
    favorito = db.query(models.Favorito).filter(models.Favorito.id == favorito_id).first()
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    db.delete(favorito)
    db.commit()
    return {"mensaje": "Favorito eliminado correctamente"}
