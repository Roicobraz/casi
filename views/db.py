from tkinter import *

def effectDb(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    db_frame(frame_content)

def db_frame(frame_content: Frame):
    print("Affichage de la db du projet")