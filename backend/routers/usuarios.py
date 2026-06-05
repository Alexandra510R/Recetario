from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import Optional
import os

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta_recetario")
ALGORITHM = "HS256"

def hash_password(password: str):
    return pwd_context.hash(password[:72])

def crear_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=24)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

class ActualizarPerfil(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    edad: Optional[int] = None
    genero: Optional[str] = None
    interes: Optional[str] = None
    mensaje: Optional[str] = None

class CambiarPassword(BaseModel):
    password_actual: str
    password_nueva: str

@router.post("/registro", response_model=schemas.UsuarioResponse)
def registrar(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existente = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    nuevo = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        password=hash_password(usuario.password),
        telefono=usuario.telefono,
        edad=usuario.edad,
        genero=usuario.genero,
        interes=usuario.interes,
        mensaje=usuario.mensaje
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.post("/login", response_model=schemas.Token)
def login(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if not db_usuario or not pwd_context.verify(usuario.password[:72], db_usuario.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = crear_token({"sub": db_usuario.email, "id": db_usuario.id})
    usuario_data = {
        "id": db_usuario.id,
        "nombre": db_usuario.nombre,
        "email": db_usuario.email,
        "telefono": db_usuario.telefono,
        "edad": db_usuario.edad,
        "genero": db_usuario.genero,
        "interes": db_usuario.interes,
        "mensaje": db_usuario.mensaje
    }
    return {"access_token": token, "token_type": "bearer", "usuario": usuario_data}

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}")
def actualizar_perfil(usuario_id: int, datos: ActualizarPerfil, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombre   = datos.nombre
    usuario.telefono = datos.telefono
    usuario.edad     = datos.edad
    usuario.genero   = datos.genero
    usuario.interes  = datos.interes
    usuario.mensaje  = datos.mensaje
    db.commit()
    db.refresh(usuario)
    return {
        "mensaje": "Perfil actualizado correctamente",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "telefono": usuario.telefono,
            "edad": usuario.edad,
            "genero": usuario.genero,
            "interes": usuario.interes,
            "mensaje": usuario.mensaje
        }
    }

@router.put("/{usuario_id}/password")
def cambiar_password(usuario_id: int, datos: CambiarPassword, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not pwd_context.verify(datos.password_actual[:72], usuario.password):
        raise HTTPException(status_code=400, detail="La contraseña actual es incorrecta")
    usuario.password = hash_password(datos.password_nueva)
    db.commit()
    return {"mensaje": "Contraseña actualizada correctamente"}
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}
