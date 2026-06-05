from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
import io

router = APIRouter()

@router.get("/{receta_id}/exportar-pdf")
def exportar_receta_pdf(receta_id: int, db: Session = Depends(get_db)):
    receta = db.query(models.Receta).filter(models.Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Título
    story.append(Paragraph(f"🍽️ {receta.titulo}", styles['Title']))
    story.append(Spacer(1, 0.2 * inch))

    # Descripción
    if receta.descripcion:
        story.append(Paragraph("Descripción", styles['Heading2']))
        story.append(Paragraph(receta.descripcion, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    # Ingredientes
    if receta.ingredientes:
        story.append(Paragraph("Ingredientes", styles['Heading2']))
        story.append(Paragraph(receta.ingredientes, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    # Instrucciones
    if receta.instrucciones:
        story.append(Paragraph("Instrucciones", styles['Heading2']))
        story.append(Paragraph(receta.instrucciones, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    # Categoría
    if receta.categoria:
        story.append(Paragraph(f"Categoría: {receta.categoria}", styles['Normal']))

    doc.build(story)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=receta_{receta_id}.pdf"
        }
    )