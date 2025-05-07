import os.path, json
from tkinter import *
from tkinter import filedialog
import shutil

path = './datas/parameters.json'
fileExist = os.path.isfile(path)
listeProject = ["Choisir un projet"]

def initDirectory(label_file_explorer: Label):
    filename = filedialog.askdirectory()
    if (filename == ""):
        filename = "\\"
    label_file_explorer.configure(text="Répertoire des projets: \n"+filename)
    return(filename)

def setDirectory(label):
    filename = initDirectory(label)
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["path_projects"] = filename
        file.close()
        parameters(datas)

def getDirectory():
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)["path_projects"]
    file.close()
    return(data)

def parameters(structure = {'path_projects': '', 'projects': [], 'autoload': False}):
    with open(path, 'w') as file:
        file.write(json.dumps(structure, sort_keys=True, indent=4))
        file.close()

def addPath(path_project):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["path_projects"] = path_project
        file.close()
        parameters(datas)

def addProject(name):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        
        solution = checkSolution(name)
        datas["projects"].append({"name": name, "solution": solution[0], "version": solution[1]})
        file.close()
        parameters(datas)

def supprProject(project_name):
    path_project = getDirectory()+"\\"+project_name

    if(os.path.isdir(path_project)):
        shutil.rmtree(path_project)
    if(not os.path.isdir(path_project)):
        with open(path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            for project in datas["projects"]:
                if (project.get('name') == project_name):
                    datas["projects"].remove(project)
                    break  
        file.close()
        parameters(datas)

def getIdProject(name) -> int:
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        for project in datas['projects']:
            if(project['name'] == name):
                break
            count += 1
    file.close()
    return(count)

def getProject(name) -> dict|int:
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        for project in datas['projects']:
            if(project['name'] == name):
                break
            else:
                project = 0
    file.close()
    return(project)

def getAllProjects() -> list:
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        arrprojects = []

        for project in datas['projects']:
            arrprojects.append(project['name'])
    file.close()
    return(arrprojects)

def checkSolution(project_name: str):
    solution = ""
    version = ""
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        path_project = datas["path_projects"]
        for project in os.listdir(path_project + "\\" + project_name):
            if( "license.txt" == project or "wp-admin" == project or "wp-content" == project or "wp-includes" == project):
                with open(path_project + "\\" + project_name + "\\" + 'license.txt') as licence:
                    first_line = licence.readline()
                    if("WordPress" in first_line):
                        solution = "WordPress"
                        with open(path_project + "\\" + project_name + "\\wp-includes\\version.php") as version_file:
                            for line_no, line in enumerate(version_file):
                                if line_no == 18:    
                                    version = line.replace("$wp_version = '", "")
                                    version = version.replace("';", "")
                                    version = version.strip()
                            file.close()
                    file.close()
                    break
            elif("README.md" == project):
                with open(path_project + "\\" + project_name + "\\" + 'README.md') as readme:
                    first_line = readme.readline()
                    if("MVC-POO" in first_line):
                        solution = "JV Framework"
                        for line_no, line in enumerate(readme):
                            if line_no == 2:    
                                version = line.replace("> ", "")
                                version = version.replace(" -", "")
                                version = version.strip()
                    file.close()
        file.close()
    return(solution, version)

def createProject(name, solution, version):
    print('creation de projet')
    # import subprocess
    # subprocess.Popen("git clone https://github.com/Roicobraz/mvc_poo.git C:/xampp/htdocs/dev_web/testgit --branch V0.1", shell=True)