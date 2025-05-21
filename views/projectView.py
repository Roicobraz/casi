from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from models.project import Project
from models.solution import Solution


class ProjectView:
    content_frame: Frame
    comboProject: ttk.Combobox
    project = Project()

    def __init__(self, frame_content, comboProject):
        self.frame_content = frame_content
        self.comboProject = comboProject

    def frameProject(self):
        project = self.project.getProject(self.comboProject.get())
        if(project):
            self.frameManageProject(project)
        else:
            self.frameAddProject()
    
    def frameManageProject(self, project) -> None:
        Label(self.frame_content, text=project["name"]).pack()

        if(project["solution"]):
            Label(self.frame_content, text=project["solution"]).pack()
        if(project["version"]):
            Label(self.frame_content, text=project["version"]).pack()

        if(project["solution"] == "JV Framework"):
            Label(self.frame_content, text="combobox des assets disponible").pack()
        
        Button(self.frame_content, text="Supprimer le projet", command=lambda: self.verifySupprProject(project["name"])).pack()

    def frameAddProject(self) -> None:
        solution = Solution()
        Label(self.frame_content, text="Nom du projet").pack()
        Entry(self.frame_content).pack()

        comboSolution = ttk.Combobox(self.frame_content, width=25)
        comboSolution["values"] = solution.updcomboboxSolutions()
        comboSolution.current(0)
        comboSolution.pack()

        comboSolution = ttk.Combobox(self.frame_content, width=25)
        comboSolution["values"] = ["Choisir une version"]
        comboSolution.current(0)
        comboSolution.pack()

        Button(self.frame_content, text="Créer le projet").pack()

    def verifySupprProject(self, project):
        if askyesno('Confirmation', 'Voulez-vous supprimer le projet ' + project + '?'):
            self.project.supprProject(project)
            self.comboProject.current(0)
            values = list(self.comboProject["values"])
            values.remove(project)
            self.comboProject["values"] = tuple(values)
