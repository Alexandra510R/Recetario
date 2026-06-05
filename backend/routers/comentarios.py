from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{receta_id}")
def obtener_comentarios(receta_id: int, db: Session = Depends(get_db)):
    comentarios = db.query(models.Comentario).filter(
        models.Comentario.receta_id == receta_id
    ).all()
    return [{"id": c.id, "contenido": c.contenido, "usuario_id": c.usuario_id, 
             "receta_id": c.receta_id, "created_at": c.created_at} for c in comentarios]

@router.post("/")
def crear_comentario(comentario: schemas.ComentarioCreate, usuario_id: int, db: Session = Depends(get_db)):
    # Verificar que la receta existe
    receta = db.query(models.Receta).filter(models.Receta.id == comentario.receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    # Verificar que el usuario existe
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    nuevo = models.Comentario(
        contenido=comentario.contenido,
        receta_id=comentario.receta_id,
        usuario_id=usuario_id
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"id": nuevo.id, "contenido": nuevo.contenido, "usuario_id": nuevo.usuario_id,
            "receta_id": nuevo.receta_id, "created_at": nuevo.created_at}

@router.delete("/{comentario_id}")
def eliminar_comentario(comentario_id: int, db: Session = Depends(get_db)):
    comentario = db.query(models.Comentario).filter(models.Comentario.id == comentario_id).first()
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    db.delete(comentario)
    db.commit()
    return {"mensaje": "Comentario eliminado correctamente"}
