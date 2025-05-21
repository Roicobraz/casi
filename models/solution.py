import json
from shutil import which

from models.parameters import Parameters

class Solution(Parameters):
    isInstalled: bool = which("git") is not None
    listeSolution: list[str] = ["Ajouter un Framework/CMS"]

    def solutions(self, structure: dict = {'solutions': []}) -> None:
        with open(self.path_solution, 'w') as file:
            file.write(json.dumps(structure, sort_keys=True, indent=4))
        file.close()
        self.updcomboboxSolutions()

    def addSolution(self, name: str, link: str, version: list) -> None:
        with open(self.path_solution, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            datas["solutions"].append({"name": name, "link": link, "versions": version})
        file.close()
        self.solutions(datas)

    def delSolution(self, solution_name):
        if(self.getSolutionByName(solution_name)):
            with open(self.path_solution, 'r', encoding='utf-8') as file:
                datas = json.load(file)
                for solution in datas["solutions"]:
                    if (solution.get('name') == solution_name):
                        datas["solutions"].remove(solution)
                        break  
            file.close()
            self.solutions(datas)

    def getAllNameSolutions(self) -> list:
        with open(self.path_solution, 'r', encoding='utf-8') as file:
            datas = json.load(file)
            arrsolutions = []

            for solution in datas['solutions']:
                arrsolutions.append(solution['name'])
        file.close()
        return(arrsolutions)

    def getAllSolutions(self) -> list:
        with open(self.path_solution, 'r', encoding='utf-8') as file:
            datas = json.load(file)
        file.close()
        return(datas['solutions'])

    def getSolutionByName(self, name) -> list | int:
        with open(self.path_solution, 'r', encoding='utf-8') as file:
            datas = json.load(file)

            for solution in datas['solutions']:
                if(name == solution['name']):
                    break
                else:
                    solution = 0
        file.close()
        return(solution)

    def updateSolution(self, updsolution, name: str, link: str, version: list) -> None:
        with open(self.path_solution, 'r', encoding='utf-8') as file:
            datas: dict = json.load(file)
            count = 0
            for solution in datas["solutions"]:
                if(solution == updsolution):
                    datas["solutions"][count] = {"name": name, "link": link, "versions": version}
                    break
                count += 1
        file.close()
        self.solutions(datas)

    def updcomboboxSolutions(self) -> list[str]:
        solutions = self.getAllNameSolutions()
        for solution in solutions:
            if(solution not in self.listeSolution):
                self.listeSolution.append(solution)
        return(self.listeSolution)
    
    def getVersionsbyName(self, name) -> list | int:
        solution = self.getSolutionByName(name)
        if(len(solution["versions"]) > 0):
            return(solution["versions"])
        else:
            return 0
        
    def getLinkbyName(self, name) -> list | int:
        solution = self.getSolutionByName(name)
        return(solution["link"])