from tkinter import *

def init():
    frame = Frame(init, height=250)

    Label(frame, text="Chemin absolue du répertoire des solutions web : ").pack()
    entryPath = Entry(frame, bd = 5, width=50)
    entryPath.bind("<Return>", setPath)
    entryPath.pack()
    Button(frame, text="Confirmer", command=setPath).pack()

    frame.place(relx=.5, rely=.45,anchor= CENTER)