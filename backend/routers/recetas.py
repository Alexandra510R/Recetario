from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas
from ..database import get_db
from jose import jwt, JWTError
import os

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta_recetario")
ALGORITHM = "HS256"

def get_current_user(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token requerido")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token inválido")
        usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()
        if not usuario:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        return usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

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
def crear_receta(
    receta: schemas.RecetaCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    datos = receta.dict()
    datos['usuario_id'] = current_user.id
    nueva = models.Receta(**datos)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{receta_id}", response_model=schemas.RecetaResponse)
def actualizar_receta(
    receta_id: int,
    datos: schemas.RecetaCreate,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    for key, value in datos.dict().items():
        setattr(receta, key, value)
    db.commit()
    db.refresh(receta)
    return receta

@router.delete("/{receta_id}")
def eliminar_receta(
    receta_id: int,
    db: Session = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    db.delete(receta)
    db.commit()
    return {"mensaje": "Receta eliminada correctamente"}