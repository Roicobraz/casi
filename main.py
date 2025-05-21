from views.mainView import mainView
from models.project import Project
from models.autoload import Autoload

if(Project.fileExist):
    Autoload().autoloadProjects()

mainView()