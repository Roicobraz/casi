from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from models.solution import Solution

class solutionView:
    solution = Solution()

    def solution_window(self):
        solutionWdw = Tk()
        solutionWdw.title("Gestion des solutions")
        solutionWdw.resizable(False, False)

        if(1==1):
            solutionWdw.geometry("385x250")

            frameSolution = Frame(solutionWdw)

            comboSolution = ttk.Combobox(frameSolution, width=25)
            comboSolution["values"] = self.solution.updcomboboxSolutions()
            comboSolution.current(0)

            comboSolution.bind('<<ComboboxSelected>>', lambda event: self.listSolution(solutionWdw, comboSolution, event))

            labelName = Label(frameSolution, text="Nom")
            entryName = Entry(frameSolution, name="name")
            labelLink = Label(frameSolution, text="Lien git")
            entryLink = Entry(frameSolution, name="link")
            labelVersion = Label(frameSolution, text="Version")
            entryVersion = Entry(frameSolution)
            entryVersion.bind("<Return>", lambda event: self.addVersionToList(entryVersion, listeVersions, event))
            btnVersion = Button(frameSolution, text="Ajouter la version", command=lambda: self.addVersionToList(entryVersion, listeVersions))

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
            btnVersion = Button(frameVersion, text="Supprimer la version", command=lambda: self.supprVersionToList(listeVersions))

            listeVersions.pack()
            btnVersion.pack()
            frameVersion.grid(row=1, column=2, padx=20, pady=10)

            btnConfirm = Button(solutionWdw, text="Confirmer", command=lambda: self.effectVersion(comboSolution, entryName, entryLink, listeVersions))
            btnConfirm.grid(row=2, column=1)

            btnSuppr = Button(solutionWdw, text="Supprimer la solution", command=lambda: self.verifySupprSolution(comboSolution.get(), comboSolution, solutionWdw))
            btnSuppr.grid(row=2, column=2)
        else:
            solutionWdw.geometry("500x250")

            comboSolution = ttk.Combobox(solutionWdw, width=25)
            comboSolution["values"] = self.solution.updcomboboxSolutions()
            comboSolution.current(0)

            comboSolution.grid(row=1, column=1, columnspan=2)

            Label(solutionWdw, text="Nom").grid(row=2, column=1, columnspan=2)
            Entry(solutionWdw, name="name").grid(row=3, column=1, columnspan=2)

            Label(solutionWdw, text="Lien git").grid(row=4, column=1, columnspan=2)
            Entry(solutionWdw, name="link").grid(row=5, column=1, columnspan=2)

            Button(solutionWdw, text="Confirmer", command=lambda: self.effectVersion(comboSolution, entryName, entryLink, listeVersions)).grid(row=7, column=1)
            Button(solutionWdw, text="Supprimer la solution", command=lambda: self.verifySupprSolution(comboSolution.get(), comboSolution, solutionWdw)).grid(row=7, column=2)


            Label(solutionWdw, text="Version").grid(row=2, column=3, rowspan=1)
            Entry(solutionWdw, name="version").grid(row=3, column=3, rowspan=1)
            
            Listbox(solutionWdw, yscrollcommand=True, selectmode="multiple", name="versions").grid(row=4, column=3, rowspan=10)

            Button(solutionWdw, text="Ajouter la version", command=lambda: self.addVersionToList(entryVersion, listeVersions)).grid(row=3, column=4)
            Button(solutionWdw, text="Supprimer la version", command=lambda: self.supprVersionToList(listeVersions)).grid(row=4, column=4)

    def addVersionToList(self, entryVersion, listeVersions: Listbox, event=""):
        if(type(entryVersion) == Entry):
            if(entryVersion.get() != "" and not entryVersion.get().isspace()):
                if (entryVersion.get() not in listeVersions.get(0, "end")):
                        listeVersions.insert(listeVersions.size(), entryVersion.get())
                        entryVersion.delete(0, "end")
        else:
            if(entryVersion != "" and not entryVersion.isspace()):
                if (entryVersion not in listeVersions.get(0, "end")):
                        listeVersions.insert(listeVersions.size(), entryVersion)

    def supprVersionToList(self, listeVersions: Listbox):
        items_selected = listeVersions.curselection()
        for selected in items_selected[::-1]:
            listeVersions.delete(selected)

    def listSolution(self, window: Tk, comboSolution: ttk.Combobox, event=""):
        solution_datas = self.solution.getSolution(comboSolution.get())
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
                                self.addVersionToList(version, widget)
        else:
            self.resetEntries(window)

    def effectVersion(self, comboSolution: ttk.Combobox, name: Entry, link: Entry, versions: Listbox):
        solution_datas = self.solution.getSolutionByName(comboSolution.get())
        if(solution_datas):
            self.solution.updateSolution(solution_datas, name.get(), link.get(), versions.get(0, "end"))
        else:
            self.solution.addSolution(name.get(), link.get(), versions.get(0, "end"))

    def verifySupprSolution(self, solution, comboSolution: ttk.Combobox, window: Tk):
        if(comboSolution.get() == 0):
            if askyesno('Confirmation', 'Voulez-vous supprimer la solution ' + solution + '?'):
                self.solution.supprSolution(solution)
                comboSolution.current(0)
                values = list(comboSolution["values"])
                values.remove(solution)
                comboSolution["values"] = tuple(values)
                self.resetEntries(window)

    def resetEntries(self, window: Tk):
        for child in window.winfo_children():
                if(type(child) == Frame):
                    for widget in child.winfo_children(): 
                        if(type(widget) == Entry or type(widget) == Listbox): 
                            widget.delete(0, "end")
