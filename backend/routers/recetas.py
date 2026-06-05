from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.RecetaResponse])
def obtener_recetas(usuario_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(models.Receta)
    if usuario_id:
        query = query.filter(models.Receta.usuario_id == usuario_id)
    return query.all()

@router.get("/{receta_id}", response_model=schemas.RecetaResponse)
def obtener_receta(receta_id: int, db: Session = Depends(get_db)):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return receta

@router.post("/", response_model=schemas.RecetaResponse)
def crear_receta(receta: schemas.RecetaCreate, usuario_id: Optional[int] = None, db: Session = Depends(get_db)):
    datos = receta.dict()
    datos['usuario_id'] = usuario_id
    nueva = models.Receta(**datos)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{receta_id}", response_model=schemas.RecetaResponse)
def actualizar_receta(receta_id: int, datos: schemas.RecetaCreate, db: Session = Depends(get_db)):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    for key, value in datos.dict().items():
        setattr(receta, key, value)
    db.commit()
    db.refresh(receta)
    return receta

@router.delete("/{receta_id}")
def eliminar_receta(receta_id: int, db: Session = Depends(get_db)):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    db.delete(receta)
    db.commit()
    return {"mensaje": "Receta eliminada correctamente"}