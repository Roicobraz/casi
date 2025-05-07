from tkinter import *
from tkinter import ttk

import models.solution

def solution_window():
    solutionWdw = Tk()
    solutionWdw.title("Gestion des solutions")
    solutionWdw.geometry("385x250")
    solutionWdw.resizable(False, False)

    solutions = models.solution.getAllNameSolutions()
    for solution in solutions:
        models.solution.listeSolution.append(solution)

    frameSolution = Frame(solutionWdw)

    comboSolution = ttk.Combobox(frameSolution, width=25)
    comboSolution["values"] = models.solution.listeSolution
    comboSolution.current(0)

    comboSolution.bind('<<ComboboxSelected>>', lambda event: listSolution(solutionWdw, comboSolution, event))

    labelName = Label(frameSolution, text="Nom")
    entryName = Entry(frameSolution, name="name")
    labelLink = Label(frameSolution, text="Lien git")
    entryLink = Entry(frameSolution, name="link")
    labelVersion = Label(frameSolution, text="Version")
    entryVersion = Entry(frameSolution)
    entryVersion.bind("<Return>", lambda event: addVersionToList(entryVersion, listeVersions, event))
    btnVersion = Button(frameSolution, text="Ajouter la version", command=lambda: addVersionToList(entryVersion, listeVersions))

    comboSolution.pack()
    labelName.pack()
    entryName.pack()
    labelLink.pack()
    entryLink.pack()
    labelVersion.pack()
    entryVersion.pack()
    btnVersion.pack()

    frameSolution.grid(row=1, column=1, padx=20, pady=10)

    frameVersion = Frame(solutionWdw)
    listeVersions = Listbox(frameVersion, yscrollcommand=True, selectmode="multiple", name="versions") 
    btnVersion = Button(frameVersion, text="Supprimer la version", command=lambda: supprVersionToList(listeVersions))

    listeVersions.pack()
    btnVersion.pack()
    frameVersion.grid(row=1, column=2, padx=20, pady=10)

    btnConfirm = Button(solutionWdw, text="Confirmer", command=lambda: effectVersion(comboSolution, entryName, entryLink, listeVersions))
    btnConfirm.grid(row=2, column=1)

def addVersionToList(entryVersion, listeVersions: Listbox, event=""):
    if(type(entryVersion) == Entry):
        if(entryVersion.get() != "" and not entryVersion.get().isspace()):
            if (entryVersion.get() not in listeVersions.get(0, "end")):
                    listeVersions.insert(listeVersions.size(), entryVersion.get())
                    entryVersion.delete(0, "end")
    else:
        if(entryVersion != "" and not entryVersion.isspace()):
            if (entryVersion not in listeVersions.get(0, "end")):
                    listeVersions.insert(listeVersions.size(), entryVersion)

def supprVersionToList(listeVersions: Listbox):
    items_selected = listeVersions.curselection()
    for selected in items_selected[::-1]:
        listeVersions.delete(selected)

def listSolution(window: Tk, comboSolution: ttk.Combobox, event=""):
    solution_datas = models.solution.getSolution(comboSolution.get())
    if(solution_datas):
        for child in window.winfo_children():
            if(type(child) == Frame):
                for widget in child.winfo_children():
                    if(widget.winfo_name() == "name"):
                        widget.delete(0, "end")
                        widget.insert(0, solution_datas['name'])
                    elif(widget.winfo_name() == "link"):
                        widget.delete(0, "end")
                        widget.insert(0, solution_datas['link'])
                    elif(widget.winfo_name() == "versions"):
                        widget.delete(0, "end")
                        for version in solution_datas['versions']:
                            addVersionToList(version, widget)
    else:
        for child in window.winfo_children():
            if(type(child) == Frame):
                for widget in child.winfo_children(): 
                    if(widget.winfo_name() == "name" or widget.winfo_name() == "link" or widget.winfo_name() == "versions"): 
                        widget.delete(0, "end")

def effectVersion(comboSolution: ttk.Combobox, name: Entry, link: Entry, versions: Listbox):
    solution_datas = models.solution.getSolution(comboSolution.get())
    if(solution_datas):
        models.solution.updateSolution(solution_datas, name.get(), link.get(), versions.get(0, "end"))
    else:
        models.solution.addSolution(name.get(), link.get(), versions.get(0, "end"))
