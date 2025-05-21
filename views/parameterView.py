from tkinter import *

from views.solutionView import solutionView

from models.project import Project
from models.autoload import Autoload


class ParameterView:
    content_frame: Frame
    
    
    def __init__(self, frame : Frame) -> None:
        self.frame_content = frame

    def frameParameter(self):
        autoload = Autoload()
        project = Project()
        
        check_var = BooleanVar(value=autoload.getAutoload())
        checkBtn_autoload = Checkbutton(self.frame_content, text='Autoload', bg="white", variable=check_var, command=lambda: autoload.effectAutoload(check_var))
        
        repository = Label(self.frame_content, text="Répertoire des projets: \n" + project.getDirectory(), bg="white")
        btnPath = Button(self.frame_content, text="Chercher dans le PC", bg="white", command=lambda: project.setDirectory(repository))

        btnSolution = Button(self.frame_content, text="Gérer les Frameworks/CMS", bg="white", command=lambda: solutionView().solution_window())

        checkBtn_autoload.pack()
        repository.pack()
        btnPath.pack()
        btnSolution.pack()
