from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import models.project

def verifySupprProject(project):
    if askyesno('Confirmation', 'Voulez-vous supprimer le projet ' + project + '?'):
        models.project.supprProject(project)

def effectProject(frame_content, listeCombo, event = ""):
    for widget in frame_content.winfo_children():
        widget.destroy()
    project_frame(frame_content, listeCombo)

def project_frame(frame_content: Frame, listeCombo: ttk.Combobox):
    project = models.project.getProject(listeCombo.get())
    if(project):
        # Projet existant, modifiable, supprimable
        Label(frame_content, text=project["name"]).pack()
        Label(frame_content, text=project["solution"]).pack()
        Label(frame_content, text=project["version"]).pack()
        if(project["solution"] == "JV Framework"):
            Label(frame_content, text="combobox des assets disponible").pack()
        
        Button(frame_content, text="Supprimer le projet", command=lambda: verifySupprProject(project["name"])).pack()
    else:
        # Ajout de projet
        Label(frame_content, text="Nom du projet").pack()
        Entry(frame_content).pack()

        Label(frame_content, text="combobox des framewok/cms").pack()
        Label(frame_content, text="combobox des versions").pack()

        Button(frame_content, text="Créer le projet").pack()