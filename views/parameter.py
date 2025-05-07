from tkinter import *

import models.autoload, models.project
import views.solution

def effectParameter(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    parameter_frame(frame_content)

def parameter_frame(frame_content: Frame):
    check_var = BooleanVar(value=models.autoload.getAutoload())
    checkBtn_autoload = Checkbutton(frame_content, text='Autoload', bg="white", variable=check_var, command=lambda: models.autoload.effectAutoload(check_var))

    
    repository = Label(frame_content, text="Répertoire des projets: \n"+models.project.getDirectory(), bg="white")
    btnPath = Button(frame_content, text="Chercher dans le PC", bg="white", command=lambda: models.project.setDirectory(repository))

    btnSolution = Button(frame_content, text="Gérer les Frameworks/CMS", bg="white", command=lambda: views.solution.solution_window())


    checkBtn_autoload.pack()
    repository.pack()
    btnPath.pack()
    btnSolution.pack()
