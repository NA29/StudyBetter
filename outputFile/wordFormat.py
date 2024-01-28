import docx
import requests
from docx.shared import Inches
import subprocess
import sys
import os
import googleimage
from google_images_search import GoogleImagesSearch

PATH_TXT = ""
notesTaken = ""


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def getDefinition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            return "No definitions found."
        
        first_definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        return first_definition
    else: return "Word not found or an error occurred."




def main():
    document = docx.Document()
    table = document.add_table(rows=1, cols=2)
    left_cell = table.rows[0].cells[0]
    right_cell = table.rows[0].cells[1]
    # left_cell.text = read_text_file(PATH_TXT)
    googleimage.getImage()
    right_cell.add_paragraph().add_run().add_picture("out.png",width=Inches(2))

    left_cell.text = getDefinition("battery")


    document.save('notes.docx')
    if sys.platform.startswith('darwin'):  
        subprocess.run(['open', 'notes.docx'])



if __name__ == '__main__':
    main()