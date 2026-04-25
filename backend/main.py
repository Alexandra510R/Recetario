from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import recetas, usuarios, favoritos, comentarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recetario Colombiano API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(recetas.router, prefix="/recetas", tags=["Recetas"])
app.include_router(favoritos.router, prefix="/favoritos", tags=["Favoritos"])
app.include_router(comentarios.router, prefix="/comentarios", tags=["Comentarios"])

@app.get("/")
def root():
    return {"mensaje": "Bienvenido al API del Recetario Colombiano CO"}