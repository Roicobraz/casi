from tkinter import *
from tkinter import ttk

def test():
    init = Tk()
    init.title(" ")
    init.geometry("500x250")
    init.resizable(False, False)

    menu = Frame(init, bg="#636363", height=250)

    listeSite=["Choisir un site"]
    listeCombo = ttk.Combobox(menu, values=listeSite)
    listeCombo.current(0)


    btnSite = Button(menu, text="Site")
    btnDb = Button(menu, text="Base de données")

    listeCombo.pack()
    btnSite.pack()
    btnDb.pack()

    menu.pack(side=TOP, anchor=NW)

    init.mainloop()