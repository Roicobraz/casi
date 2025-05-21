from tkinter import *
from tkinter import ttk

from views.parameterView import *
from views.projectView import *

from models.project import Project

class navView:
    window: Tk
    menu_frame: Frame
    content_frame: Frame
    contentView: ProjectView | ParameterView
    project = Project()

    def __init__(self, window : Tk) -> None:
        self.window = window
        self.menu_frame = Frame(self.window, bg="#636363")
        self.content_frame = Frame(self.window, bg="white", height=250, width=300)

        self.menu_frame.place(x=0, y=0, height=250, width=200)
        self.content_frame.place(x=200, y=0, height=250, width=300)

    def nav_frame(self):
        comboProject = ttk.Combobox(self.menu_frame)
        comboProject["values"] = self.project.updcomboboxProject()
        comboProject.current(0)

        comboProject.bind('<<ComboboxSelected>>', lambda event: self.listProjectEvent(comboProject, event))

        btnProject = Button(self.menu_frame, text="Projet", command = lambda: self.effectProject(comboProject))
        btnParameter = Button(self.menu_frame, text="Paramètres", command = lambda: self.effectParameter())

        comboProject.pack()
        btnProject.pack()
        btnParameter.pack(side=BOTTOM, anchor=SW)

        self.effectProject(comboProject)
        
    def listProjectEvent(self, comboProject, event=""):
        self.effectProject(comboProject)

    def effectParameter(self):
        self.destroyView()
        self.contentView = ParameterView(self.content_frame)
        self.contentView.frameParameter()

    def effectProject(self, comboProject: ttk.Combobox):
        self.destroyView()
        self.contentView = ProjectView(self.content_frame, comboProject)
        self.contentView.frameProject()

    def destroyView(self):
        if(hasattr(self, "contentView")):
            for widget in self.contentView.frame_content.winfo_children():
                widget.destroy()