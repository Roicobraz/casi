from tkinter import *
from tkinter import ttk

from views.parameter import *
from views.db import *
from views.project import *

def nav_frame(init: Tk):
    menu_frame = Frame(init, bg="#636363")
    menu_frame.place(x=0, y=0, height=250, width=200)
    frame_content = Frame(init, bg="white", height=250, width=300)
    frame_content.place(x=200, y=0, height=250, width=300)
    
    projects = models.project.getAllProjects()
    for project in projects:
        models.project.listeProject.append(project)
    comboProject = ttk.Combobox(menu_frame)
    comboProject["values"] = models.project.listeProject
    comboProject.current(0)

    comboProject.bind('<<ComboboxSelected>>', lambda event: effectProject(frame_content, comboProject, event))

    btnProject = Button(menu_frame, text="Projet", command = lambda: effectProject(frame_content, comboProject))
    btnDb = Button(menu_frame, text="Base de données", command = lambda: effectDb(frame_content))
    btnParameter = Button(menu_frame, text="Paramètres", command = lambda: effectParameter(frame_content))

    comboProject.pack()
    btnProject.pack()
    btnDb.pack()
    btnParameter.pack(side=BOTTOM, anchor=SW)

    parameter_frame(frame_content)