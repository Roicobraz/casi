from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
from tkinter.messagebox import *

import os, os.path 

from views.navView import navView
from models.project import Project
from models.autoload import Autoload

class mainView:
    window: Tk
    PROJECT: Project = Project()

    def __init__(self) -> None:
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.geometry("500x250")
        
        self.PROJECT = Project()

        if (not self.PROJECT.fileExist):
            self.initializationView()
        else:
            self.homeView()

        self.window.mainloop()

    def homeView(self) -> None:
        self.window.title("Casi")
        nav = navView(self.window)
        nav.nav_frame()

    def initializationView(self) -> None:
        self.PROJECT
        self.window.title("Initialisation")
        frame = Frame(self.window, height=250)

        repository = Label(frame, text="Répertoire des projets: ")
        repository.pack()

        Button(frame, text="Chercher dans le PC", command=lambda repository=repository: self.PROJECT.initDirectory(repository)).pack()
        Button(frame, text="Confirmer", command=lambda: self.setProjectPath(frame)).pack()

        frame.place(relx=.5, rely=.45,anchor= CENTER)

    def setProjectPath(self, frame: Frame, event = ""):
        if(hasattr(self.PROJECT, "dirProject")):
            self.PROJECT.parameters()
            self.PROJECT.addPath(self.PROJECT.dirProject)

            if askyesno('Chargement', 'Voulez-vous enregistrer automatiquement les projets?'):
                Autoload().autoload(True)
                for name in os.listdir(self.PROJECT.dirProject):
                    if(os.path.isdir(self.PROJECT.dirProject + "\\" + name)):
                        self.PROJECT.addProject(name)

            for widget in frame.winfo_children():
                widget.destroy()
            self.homeView()

        else:
            showerror('Erreur', 'Veuillez rechercher un répertoire!')