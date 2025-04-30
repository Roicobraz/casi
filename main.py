from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import os, os.path 

import parameters, views.nav


init = Tk()
init.title("Initialisation")
init.geometry("500x250")
init.resizable(False, False)

if(parameters.fileExist):
    parameters.autoloadSites()

def setPath(event = ""):
    if(entryPath.get() != "" and (not os.path.isfile("./parameters.json")) and os.path.exists(entryPath.get())):
        parameters.parameters()
        path = entryPath.get()
        parameters.addPath(path)

        if askyesno('Chargement', 'Voulez-vous enrigistrer automatiquement les projets déjà existant?'):
            parameters.autoload(True)
            for name in os.listdir(path):
                if(os.path.isdir(path+"\\"+name)):
                    parameters.addSite(name)

        for widget in frame.winfo_children():
            widget.destroy()
        views.nav.nav_frame(init)
    elif(not os.path.exists(entryPath.get())):
        showerror('Erreur', 'Chemin invalide!')

if (not parameters.fileExist):
    frame = Frame(init, height=250)

    Label(frame, text="Chemin absolue du répertoire des solutions web : ").pack()
    entryPath = Entry(frame, bd = 5, width=50)
    entryPath.bind("<Return>", setPath)
    entryPath.pack()
    Button(frame, text="Confirmer", command=setPath).pack()

    frame.place(relx=.5, rely=.45,anchor= CENTER)
else:
    views.nav.nav_frame(init)
init.mainloop()