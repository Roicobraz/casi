import os.path, json

path = './parameters.json'
fileExist = os.path.isfile(path)

def parameters(structure = {'path_sites': '', 'sites': [], 'autoload': False}):
    with open(path, 'w') as file:
        file.write(json.dumps(structure, sort_keys=True, indent=4))
        file.close()

def addPath(path_site):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["path_sites"] = path_site
        file.close()
        parameters(datas)

def addSite(name):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        
        solution = checkSolution(name)
        datas["sites"].append({"name": name, "solution": solution[0], "version": solution[1]})
        file.close()
        parameters(datas)

def autoload(activate):
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        datas["autoload"] = activate
        file.close()
        parameters(datas)

def autoloadSites():
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        if(datas["autoload"]):
            arrSites = []

            # je parcoure le json
            for site in datas['sites']:
                if(site['name'] not in arrSites):
                    arrSites.append(site['name'])

            # je parcoure le dossier
            for name in os.listdir(datas['path_sites']):
                if(os.path.isdir(datas['path_sites']+"\\"+name) and ( name not in arrSites)):
                    addSite(name)
        file.close() 

def checkSolution(project_name):
    solution = ""
    version = ""
    with open(path, 'r', encoding='utf-8') as file:
        datas = json.load(file)
        path_site = datas["path_sites"]
        for project in os.listdir(path_site + "\\" + project_name):
            if( "license.txt" == project or "wp-admin" == project or "wp-content" == project or "wp-includes" == project):
                with open(path_site + "\\" + project_name + "\\" + 'license.txt') as licence:
                    first_line = licence.readline()
                    if("WordPress" in first_line):
                        solution = "WordPress"
                        with open(path_site + "\\" + project_name + "\\wp-includes\\version.php") as version_file:
                            for line_no, line in enumerate(version_file):
                                if line_no == 18:    
                                    version = line.replace("$wp_version = '", "")
                                    version = version.replace("';", "")
                                    version = version.strip()
                            file.close()
                    file.close()
                    break
            elif("README.md" == project):
                with open(path_site + "\\" + project_name + "\\" + 'README.md') as readme:
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