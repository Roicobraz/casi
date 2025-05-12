from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import models.project, models.solution

def verifySupprProject(project, comboProject: ttk.Combobox, frame_content):
    if askyesno('Confirmation', 'Voulez-vous supprimer le projet ' + project + '?'):
        models.project.supprProject(project)
        comboProject.current(0)
        values = list(comboProject["values"])
        values.remove(project)
        comboProject["values"] = tuple(values)
        effectProject(frame_content, comboProject)

def effectProject(frame_content: Frame, comboProject: ttk.Combobox):
    for widget in frame_content.winfo_children():
        widget.destroy()
    project_frame(frame_content, comboProject)

def project_frame(frame_content: Frame, comboProject: ttk.Combobox):
    project = models.project.getProject(comboProject.get())
    if(project):
        # Projet existant, modifiable, supprimable
        Label(frame_content, text=project["name"]).pack()

        if(project["solution"]):
            Label(frame_content, text=project["solution"]).pack()
        if(project["version"]):
            Label(frame_content, text=project["version"]).pack()

        if(project["solution"] == "JV Framework"):
            Label(frame_content, text="combobox des assets disponible").pack()
        
        Button(frame_content, text="Supprimer le projet", command=lambda: verifySupprProject(project["name"], comboProject, frame_content)).pack()
    else:
        # Ajout de projet
        Label(frame_content, text="Nom du projet").pack()
        Entry(frame_content).pack()

        comboSolution = ttk.Combobox(frame_content, width=25)
        comboSolution["values"] = models.solution.updcomboboxSolutions()
        comboSolution.current(0)
        comboSolution.pack()

        comboSolution = ttk.Combobox(frame_content, width=25)
        comboSolution["values"] = ["Choisir une version"]
        comboSolution.current(0)
        comboSolution.pack()

        Button(frame_content, text="Créer le projet").pack()