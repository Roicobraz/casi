from tkinter import *

def effectProject(frame_content: Frame):
    for widget in frame_content.winfo_children():
        widget.destroy()
    project_frame(frame_content)

def project_frame(frame_content: Frame):
    print("test")