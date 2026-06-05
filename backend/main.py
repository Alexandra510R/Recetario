from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .routers import recetas, usuarios, favoritos, comentarios
from prometheus_fastapi_instrumentator import Instrumentator

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recetario Colombiano API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics
Instrumentator().instrument(app).expose(app)

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(recetas.router, prefix="/recetas", tags=["Recetas"])
app.include_router(favoritos.router, prefix="/favoritos", tags=["Favoritos"])
app.include_router(comentarios.router, prefix="/comentarios", tags=["Comentarios"])

@app.get("/")
def root():
    return {"mensaje": "Bienvenido al API del Recetario Colombiano CO"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/migrate")
def migrate(db: Session = Depends(get_db)):
    from sqlalchemy import text
    try:
        db.execute(text("ALTER TABLE recetas ADD COLUMN usuario_id INTEGER REFERENCES usuarios(id)"))
        db.commit()
        return {"mensaje": "Migracion exitosa"}
    except Exception as e:
        return {"mensaje": f"Ya existe o error: {str(e)}"}