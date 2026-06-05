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

    story.append(Paragraph(f"Sabores Colombianos - {receta.titulo}", styles['Title']))
    story.append(Spacer(1, 0.2 * inch))

    if receta.region:
        story.append(Paragraph(f"Region: {receta.region}", styles['Heading2']))
        story.append(Spacer(1, 0.1 * inch))

    if receta.ingredientes:
        story.append(Paragraph("Ingredientes", styles['Heading2']))
        story.append(Paragraph(receta.ingredientes, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    if receta.pasos:
        story.append(Paragraph("Preparacion", styles['Heading2']))
        story.append(Paragraph(receta.pasos, styles['Normal']))
        story.append(Spacer(1, 0.2 * inch))

    if receta.video_url:
        story.append(Paragraph(f"Video: {receta.video_url}", styles['Normal']))

    doc.build(story)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=receta_{receta_id}.pdf"
        }
    )
