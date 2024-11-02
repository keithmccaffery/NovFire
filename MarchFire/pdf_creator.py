from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
c = canvas.Canvas("my_paragraph.pdf", pagesize=letter)
width, height = letter
doc = SimpleDocTemplate("my_paragraph.pdf", pagesize=letter)
styles = getSampleStyleSheet()
flowables = []

text = """
Hello, Keith!
This is a Paragraph.
"""

para = Paragraph(text, styles["BodyText"])

print("Attributes of BodyText style:")
print(f"Font Name: {styles['BodyText'].fontName}")
print(f"Font Size: {styles['BodyText'].fontSize}")
print(f"Text Color: {styles['BodyText'].textColor}")
print(f"Alignment: {styles['BodyText'].alignment}")

flowables.append(para)

doc.build(flowables)