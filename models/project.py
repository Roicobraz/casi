from tkinter import *
from tkinter import filedialog

import shutil, os.path, json

from models.parameters import Parameters

class Project(Parameters):
    fileExist: bool = os.path.isfile(Parameters.path)
    listeProject: list[str] = ["Choisir un projet"]
    dirProject: str

    def initDirectory(self, label_file_explorer: Label) -> None:
        filename = filedialog.askdirectory()
        if (filename == ""):
            filename = "\\"
        label_file_explorer.configure(text="Répertoire des projets: \n" + filename)
        self.dirProject = filename

    def setDirectory(self, label):
        self.initDirectory(label)
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            datas["path_projects"] = self.dirProject
            file.close()
            self.parameters(datas)

    def getDirectory(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)["path_projects"]
        file.close()
        return(data)

    def parameters(self, structure = {'path_projects': '', 'projects': [], 'autoload': False}):
        with open(self.path, 'w') as file:
            file.write(json.dumps(structure, sort_keys=True, indent=4))
            file.close()

    def addPath(self, path_project):
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            datas["path_projects"] = path_project
            file.close()
            self.parameters(datas)

    def addProject(self, name):
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            
            solution = self.checkSolution(name)
            datas["projects"].append({"name": name, "solution": solution[0], "version": solution[1]})
            file.close()
            self.parameters(datas)

    def supprProject(self, project_name):
        path_project = self.getDirectory()+"\\"+project_name

        if(os.path.isdir(path_project)):
            shutil.rmtree(path_project)
        if(not os.path.isdir(path_project)):
            with open(self.path, 'r', encoding='utf-8') as file:
                datas = json.load(file)
                for project in datas["projects"]:
                    if (project.get('name') == project_name):
                        datas["projects"].remove(project)
                        break  
            file.close()
            self.parameters(datas)

    def getIdProject(self, name) -> int:
        count = 0
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            for project in datas['projects']:
                if(project['name'] == name):
                    break
                count += 1
        file.close()
        return(count)

    def getProject(self, name) -> dict|int:
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            for project in datas['projects']:
                if(project['name'] == name):
                    break
                else:
                    project = 0
        file.close()
        return(project)

    def getAllNameProject(self) -> list:
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            arrprojects = []

            for project in datas['projects']:
                arrprojects.append(project['name'])
        file.close()
        return(arrprojects)

    def checkSolution(self, project_name: str):
        solution = ""
        version = ""
        with open(self.path, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            path_project = datas["path_projects"]
            for project in os.listdir(path_project + "\\" + project_name):
                if( "license.txt" == project or "wp-admin" == project or "wp-content" == project or "wp-includes" == project):
                    with open(self.dirProject + "\\" + project_name + "\\" + 'license.txt') as licence:
                        first_line = licence.readline()
                        if("WordPress" in first_line):
                            solution = "WordPress"
                            with open(self.dirProject + "\\" + project_name + "\\wp-includes\\version.php") as version_file:
                                for line_no, line in enumerate(version_file):
                                    if line_no == 18:    
                                        version = line.replace("$wp_version = '", "")
                                        version = version.replace("';", "")
                                        version = version.strip()
                                file.close()
                        file.close()
                        break
                elif("README.md" == project):
                    with open(self.dirProject + "\\" + project_name + "\\" + 'README.md') as readme:
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

    def updcomboboxProject(self) -> list[str]:
        solutions = self.getAllNameProject()
        for solution in solutions:
            if(solution not in self.listeProject):
                self.listeProject.append(solution)
        return(self.listeProject)

    def createProject(self, name, solutionLink, version):
        print('creation du projet' + name + "\n Il utilise le framework ")
        gitClone = "git clone {} {}/{} --branch {}"
        gitCommand = gitClone.format(solutionLink, self.dirProject, name, version)
        print(gitCommand)
        # import subprocess
        # subprocess.Popen(gitCommand, shell=True)

        # subprocess.Popen("git clone https://github.com/Roicobraz/mvc_poo.git C:/xampp/htdocs/dev_web/testgit --branch V0.1", shell=True)