from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Dict, Any

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    telefono: Optional[str] = None
    edad: Optional[int] = None
    genero: Optional[str] = None
    interes: Optional[str] = None
    mensaje: Optional[str] = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: Optional[str] = None
    edad: Optional[int] = None
    genero: Optional[str] = None
    interes: Optional[str] = None
    mensaje: Optional[str] = None
    created_at: datetime
    class Config:
        from_attributes = True

# Recetas
class RecetaCreate(BaseModel):
    titulo: str
    region: str
    ingredientes: str
    pasos: str
    video_url: Optional[str] = None
    imagen_url: Optional[str] = None

class RecetaResponse(RecetaCreate):
    id: int
    usuario_id: Optional[int] = None
    created_at: datetime
    class Config:
        from_attributes = True

# Favoritos
class FavoritoCreate(BaseModel):
    receta_id: int

class FavoritoResponse(BaseModel):
    id: int
    usuario_id: int
    receta_id: int
    class Config:
        from_attributes = True

# Comentarios
class ComentarioCreate(BaseModel):
    contenido: str
    receta_id: int

class ComentarioResponse(BaseModel):
    id: int
    contenido: str
    usuario_id: int
    receta_id: int
    created_at: datetime
    class Config:
        from_attributes = True

# Token
class Token(BaseModel):
    access_token: str
    token_type: str
    usuario: Optional[Dict[str, Any]] = None