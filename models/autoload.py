from tkinter import *
import os.path, json

from models.project import Project
from models.parameters import Parameters

class Autoload(Parameters):
    project: Project = Project()

    def getAutoload(self) -> bool:
        with open(self.path, 'r', encoding='utf-8') as file:
            autoload = json.load(file)["autoload"]
            file.close()
        return(autoload)

    def effectAutoload(self, event: Checkbutton):
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            datas["autoload"] = event.get()
            self.project.parameters(datas)
            file.close()

    def autoload(self, activate):
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            datas["autoload"] = activate
            file.close()
            self.project.parameters(datas)

    def autoloadProjects(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            if(datas["autoload"]):
                arrprojects = []

                for project in datas['projects']:
                    if(project['name'] not in arrprojects):
                        arrprojects.append(project['name'])
                
                for supprproject in arrprojects:
                    if(not os.path.isdir(datas['path_projects']+"\\"+supprproject)):
                        print(project)
                        for project in datas["projects"]:
                            if (supprproject == project['name']):
                                datas["projects"].remove(project)
                                break  
                self.project.parameters(datas)

                for name in os.listdir(datas['path_projects']):
                    if(os.path.isdir(datas['path_projects']+"\\"+name) and ( name not in arrprojects)):
                        self.project.addProject(name)

            file.close() 