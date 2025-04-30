from tkinter import *

import models.autoload, models.project

def effectParameter(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    parameter_frame(frame_content)

def parameter_frame(frame_content: Frame):
    # TODO 
    # autoload checké si autoload de parametre.json est en true
    # coché ou déchoché cela change la valeur dans le parametre.json

    check_var = BooleanVar(value=models.autoload.getAutoload())
    checkBtn_autoload = Checkbutton(frame_content, text='Autoload', bg="white", variable=check_var, command=lambda: models.autoload.effectAutoload(check_var))

    
    repository = Label(frame_content, text="Répertoire des projets: \n"+models.project.getDirectory(), bg="white")
    entryPath = Button(frame_content, text="Chercher dans le PC", bg="white", command=lambda: models.project.setDirectory(repository))

    checkBtn_autoload.pack()
    repository.pack()
    entryPath.pack()
