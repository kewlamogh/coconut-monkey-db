import os

real_path = os.path.realpath(__file__)
fileName =  "db.txt"


def getSep() -> str:
    return "<=UISFDXLYKJSDGLOOOFSDFASLBOSKDLTHECOOLDBLFAD|L1FE=>"

def init() -> bool:
    try:
        open(real_path.split(f"{__name__}.py")[0]+fileName, "x")
        return True
    except:
        return False


def addOrSetItem(key, item) -> dict:
    with open(fileName, 'a') as f:
        f.write(f'\n{key}{getSep()}{item}')
    return {key: item}

def getItem(key) -> any:
    res = None
    with open(fileName, 'r') as f:
        for i in f:
            if (i.split(getSep())[0] == key):
                res =  i.split(getSep())[1]
    if (res == None):
        raise IndexError("Invalid Key")
    try:
        return eval(res)
    except:
        return str(res)

def deleteItem(key):
    filtered = ""
    with open(f"{fileName}", "r") as f:
        for i in f:
            if i.split(getSep())[0] == key:
                pass
            else:
                filtered += i
    with open(fileName, "w") as wr:
        wr.write(filtered)

def getKeys():
    res = []
    with open(f"{fileName}", "r") as f:
        for i in f:
            if i.split(getSep())[0] not in res:
                res.append(i.split(getSep())[0])
    return res
