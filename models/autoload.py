from tkinter import *
import os.path, json

import models.project

path = './parameters.json'

def getAutoload() -> bool:
    with open(path, 'r', encoding='utf-8') as file:
        autoload = json.load(file)["autoload"]
        file.close()
    return(autoload)

def effectAutoload(event: Checkbutton):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["autoload"] = event.get()
        models.project.parameters(datas)
        file.close()

def autoload(activate):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["autoload"] = activate
        file.close()
        models.project.parameters(datas)

def autoloadProjects():
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        if(datas["autoload"]):
            arrprojects = []

            # je parcoure le json
            for project in datas['projects']:
                if(project['name'] not in arrprojects):
                    arrprojects.append(project['name'])

            # je parcoure le dossier
            for name in os.listdir(datas['path_projects']):
                if(os.path.isdir(datas['path_projects']+"\\"+name) and ( name not in arrprojects)):
                    models.project.addProject(name)
        file.close() 

