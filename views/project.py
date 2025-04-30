from tkinter import *
from tkinter import ttk

import models.project

def effectProject(frame_content, listeCombo, event = ""):
    for widget in frame_content.winfo_children():
        widget.destroy()
    project_frame(frame_content, listeCombo)

def project_frame(frame_content: Frame, listeCombo: ttk.Combobox):
    project = models.project.getProject(listeCombo.get())
    if(project):
        Label(frame_content, text=project["name"]).pack()
        Label(frame_content, text=project["solution"]).pack()
        Label(frame_content, text=project["version"]).pack()
    else:
        print("Ajouter un projet")