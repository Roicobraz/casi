import os.path, json

from shutil import which

path_solutions: str = './datas/solutions.json'
isInstalled: bool = which("git") is not None
listeSolution: list[str] = ["Ajouter un Framework/CMS"]


def solutions(structure: dict = {'solutions': []}) -> None:
    if(isInstalled):
        with open(path_solutions, 'w') as file:
            file.write(json.dumps(structure, sort_keys=True, indent=4))
        file.close()

def addSolution(name: str, link: str, version: list) -> None:
    with open(path_solutions, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["solutions"].append({"name": name, "link": link, "versions": version})
    file.close()
    solutions(datas)

def getAllNameSolutions() -> list:
    with open(path_solutions, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        arrsolutions = []

        for solution in datas['solutions']:
            arrsolutions.append(solution['name'])
    file.close()
    return(arrsolutions)

def getAllSolutions() -> list:
    with open(path_solutions, 'r', encoding='utf-8') as file:
        datas = json.load(file)
    file.close()
    return(datas['solutions'])

def getSolution(name) -> list | int:
    with open(path_solutions, 'r', encoding='utf-8') as file:
        datas = json.load(file)

        for solution in datas['solutions']:
            if(name == solution['name']):
                break
            else:
                solution = 0
    file.close()
    return(solution)

def updateSolution(updsolution, name: str, link: str, version: list) -> None:
    # updsolution = getSolution(name)
    # solutions = getAllSolutions()
    # print(solutions)
    # for solution in solutions:
    # if(solution == updsolution):
    #     print("je modifie : "+ solution)

    with open(path_solutions, 'r', encoding='utf-8') as file:
        datas: dict = json.load(file)
        count = 0
        for solution in datas["solutions"]:
            if(solution == updsolution):
                datas["solutions"][count] = {"name": name, "link": link, "versions": version}
                break
            count += 1
    file.close()
    solutions(datas)

def supprSolution():
    print('Suppression')
# solutions()
# addSolution("JV_framework", "https://github.com/Roicobraz/mvc_poo.git", "V0.1")

# def createProject():
#     import subprocess
#     subprocess.Popen("git clone https://github.com/Roicobraz/mvc_poo.git C:/xampp/htdocs/dev_web/testgit --branch V0.1", shell=True)