from abc import ABC

class Parameters(ABC):
    path: str = './datas/parameters.json'
    path_solution: str = './datas/solutions.json'