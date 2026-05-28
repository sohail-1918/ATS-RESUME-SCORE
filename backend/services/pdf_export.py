# backend/services/pdf_export.py
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_combined_pdf(report_data: dict) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # ATS Score
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, f"ATS Score: {report_data['ats_score']}/100")

    # Summary
    c.setFont("Helvetica", 12)
    c.drawString(50, 730, report_data['summary_text'])

    # Component Scores
    y = 710
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Component Scores:")
    y -= 20
    for comp, val in report_data["component_scores"].items():
        c.setFont("Helvetica", 11)
        c.drawString(70, y, f"- {comp}: {val}")
        y -= 15

    # Issues Summary
    if report_data["issues_summary"]:
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Issues Summary:")
        y -= 20
        for issue in report_data["issues_summary"]:
            c.setFont("Helvetica", 11)
            c.drawString(70, y, f"- {issue}")
            y -= 15

    # Detailed Feedback
    if report_data["detailed_feedback"]:
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Detailed Feedback:")
        y -= 20
        for fb in report_data["detailed_feedback"]:
            c.setFont("Helvetica", 11)
            c.drawString(70, y, f"- {fb}")
            y -= 15

    # Recommendations
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Recommendations:")
    y -= 20
    for rec in report_data["recommendations"]:
        c.setFont("Helvetica-Bold", 11)
        c.drawString(70, y, f"[{rec['priority_label']}] {rec['title']}")
        y -= 15
        c.setFont("Helvetica", 10)
        c.drawString(90, y, rec['description'])
        y -= 15
        for item in rec['action_items']:
            c.drawString(110, y, f"- {item}")
            y -= 15
        y -= 10

    c.save()
    buffer.seek(0)
    return buffer.getvalue()
