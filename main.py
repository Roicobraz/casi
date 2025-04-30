from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import os, os.path 

import models.project, models.autoload, views.nav

init = Tk()
init.title("Initialisation")
init.geometry("500x250")
init.resizable(False, False)

if(models.project.fileExist):
    models.autoload.autoloadProjects()

def setPath(event = ""):
    entryPath = repository['text']
    if(entryPath != "Répertoire des projets: \\"):
        print(entryPath)

        entryPath = entryPath.replace("Répertoire des projets: ", "")
        print(entryPath)
        models.project.parameters()
        path = entryPath
        models.project.addPath(path)

        if askyesno('Chargement', 'Voulez-vous enrigistrer automatiquement les projets déjà existant?'):
            models.autoload.autoload(True)
            for name in os.listdir(path):
                if(os.path.isdir(path+"\\"+name)):
                    models.project.addProject(name)

        for widget in frame.winfo_children():
            widget.destroy()
        views.nav.nav_frame(init)
    else:
        showerror('Erreur', 'Veuillez rechercher un répertoire!')

if (not models.project.fileExist):
    frame = Frame(init, height=250)

    repository = Label(frame, text="Répertoire des projets: \\")
    repository.pack()

    entryPath = Button(frame, text="Chercher dans le PC", command=lambda: models.project.initDirectory()).pack()

    Button(frame, text="Confirmer", command=setPath).pack()

    frame.place(relx=.5, rely=.45,anchor= CENTER)
else:
    views.nav.nav_frame(init)
init.mainloop()