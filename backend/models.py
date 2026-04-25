from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    edad = Column(Integer, nullable=True)
    genero = Column(String(20), nullable=True)
    interes = Column(String(100), nullable=True)
    mensaje = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    favoritos = relationship("Favorito", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")

class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    region = Column(String(100), nullable=False)
    ingredientes = Column(Text, nullable=False)
    pasos = Column(Text, nullable=False)
    video_url = Column(String(500))
    imagen_url = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())
    favoritos = relationship("Favorito", back_populates="receta")
    comentarios = relationship("Comentario", back_populates="receta")

class Favorito(Base):
    __tablename__ = "favoritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    receta_id = Column(Integer, ForeignKey("recetas.id"))
    usuario = relationship("Usuario", back_populates="favoritos")
    receta = relationship("Receta", back_populates="favoritos")

class Comentario(Base):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    receta_id = Column(Integer, ForeignKey("recetas.id"))
    created_at = Column(DateTime, server_default=func.now())
    usuario = relationship("Usuario", back_populates="comentarios")
    receta = relationship("Receta", back_populates="comentarios")