import docx
from docx.shared import Inches

document = docx.Document()


table = document.add_table(rows=1, cols=2)

left_cell = table.rows[0].cells[0]
right_cell = table.rows[0].cells[1]


left_cell_text = 'notes prises avec surlignage'

right_cell.add_paragraph().add_run().add_picture("path de l'image")