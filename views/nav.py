from tkinter import *
from tkinter import ttk

import models.project

from views.parameter import *
from views.db import *
from views.project import *

def nav_frame(init: Tk):
    menu = Frame(init, bg="#636363")
    menu.place(x=0, y=0, height=250, width=200)
    frame_content = Frame(init, bg="white", height=250, width=300)
    frame_content.place(x=200, y=0, height=250, width=300)
    
    listeSite=["Choisir un projet"]
    sites = models.project.getAllProjects()
    for site in sites:
        listeSite.append(site)
    listeCombo = ttk.Combobox(menu, values=listeSite)
    listeCombo.current(0)
    listeCombo.bind('<<ComboboxSelected>>', lambda event: effectProject(frame_content, listeCombo, event))

    btnProject = Button(menu, text="Projet", command = lambda: effectProject(frame_content, listeCombo))
    btnDb = Button(menu, text="Base de données", command = lambda: effectDb(frame_content))
    btnParameter = Button(menu, text="Paramètres", command = lambda: effectParameter(frame_content))

    listeCombo.pack()
    btnProject.pack()
    btnDb.pack()
    btnParameter.pack(side=BOTTOM, anchor=SW)

    parameter_frame(frame_content)