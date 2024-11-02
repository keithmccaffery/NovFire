from reportlab.platypus import BaseDocTemplate, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

# Create a Paragraph
styles = getSampleStyleSheet()

# Create a new style for the heading with a light gray background
heading_style = styles['Heading1'].clone('Heading1_with_Background')
heading_style.backColor = colors.lightgrey

heading = Paragraph('This is a Heading.', heading_style)
heading2 = Paragraph('This is another Heading.', styles['Heading2'])
paragraph = Paragraph('This is a paragraph.', styles['Normal'])
paragraph2 = Paragraph('This is another paragraph.', styles['BodyText'])

# Create a list of flowables
flowables = []

# Add the flowables 6 times
for _ in range(6):
    flowables.extend([heading, Spacer(1, 20), paragraph, Spacer(1, 20), heading2, Spacer(1, 20), paragraph2, Spacer(1, 20)])

# Create a Frame with a specified width and start position
frame = Frame(50, 100, 450, 700)

# Create a custom PageTemplate that uses the Frame and draws rulers
class MyPageTemplate(PageTemplate):
    def afterDrawPage(self, canvas, doc):
        # Draw horizontal rulers
        for i in range(int(A4[0])):
            if i % 50 == 0:
                canvas.drawString(i, A4[1] - 10, str(i))
                canvas.line(i, A4[1], i, A4[1] - 10)

        # Draw vertical rulers
        for i in range(int(A4[1])):
            if i % 50 == 0:
                canvas.drawString(10, 
                                  i, str(i))
                canvas.line(0, i, 10, i)

template = MyPageTemplate(frames=[frame])

# Create a BaseDocTemplate that uses the PageTemplate
doc = BaseDocTemplate('output.pdf', pagesize=A4)
doc.addPageTemplates([template])

# Add your flowables to the BaseDocTemplate
doc.build(flowables)