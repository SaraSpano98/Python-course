"""
Creata solo per far vedere le immagini a chi non usa il jupyter notebook
Dovrebbe funzionare su tutti i sistemi operativi
Se per il vostro non fuziona, aprite le immagine nella cartella img
"""
from pathlib import Path
import platform
import os

BASE_PATH = Path(__file__).resolve().parent.name

def __show_image(file_path):
    """ Nessuna libreria esterna così non dovete installare niente """
    if platform.system() == "Darwin":  # macOS
        os.system(f"open {file_path}")
    elif platform.system() == "Windows":  # Windows
        os.system(f'start "" "{file_path}"')
    else:  # Linux
        os.system(f"xdg-open {file_path}")
    
def show_img1():
    path = BASE_PATH + "/img/variables_init.png"
    __show_image(path)
    
def show_img2():
    path = BASE_PATH + "/img/variables_same_reference.png"
    __show_image(path)