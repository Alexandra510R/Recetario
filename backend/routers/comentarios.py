from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{receta_id}", response_model=List[schemas.ComentarioResponse])
def obtener_comentarios(receta_id: int, db: Session = Depends(get_db)):
    return db.query(models.Comentario).filter(models.Comentario.receta_id == receta_id).all()

@router.post("/", response_model=schemas.ComentarioResponse)
def crear_comentario(comentario: schemas.ComentarioCreate, usuario_id: int, db: Session = Depends(get_db)):
    nuevo = models.Comentario(
        contenido=comentario.contenido,
        receta_id=comentario.receta_id,
        usuario_id=usuario_id
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/{comentario_id}")
def eliminar_comentario(comentario_id: int, db: Session = Depends(get_db)):
    comentario = db.query(models.Comentario).filter(models.Comentario.id == comentario_id).first()
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    db.delete(comentario)
    db.commit()
    return {"mensaje": "Comentario eliminado correctamente"}