from tkinter import *

def effectParameter(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    parameter_frame(frame_content)

def parameter_frame(frame_content: Frame):
    # TODO 
    # autoload checké si autoload de parametre.json est en true
    # coché ou déchoché cela change la valeur dans le parametre.json
    checkBtn_autoload = Checkbutton(frame_content, text='Autoload')
    label_path = Label(frame_content, text="Chemin des projets : ")
    entry_path = Entry(frame_content)

    checkBtn_autoload.pack()
    label_path.pack()
    entry_path.pack()