from tkinter import *

import models.autoload, models.project

def effectParameter(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    parameter_frame(frame_content)

def parameter_frame(frame_content: Frame):
    check_var = BooleanVar(value=models.autoload.getAutoload())
    checkBtn_autoload = Checkbutton(frame_content, text='Autoload', bg="white", variable=check_var, command=lambda: models.autoload.effectAutoload(check_var))

    
    repository = Label(frame_content, text="Répertoire des projets: \n"+models.project.getDirectory(), bg="white")
    entryPath = Button(frame_content, text="Chercher dans le PC", bg="white", command=lambda: models.project.setDirectory(repository))

    checkBtn_autoload.pack()
    repository.pack()
    entryPath.pack()
