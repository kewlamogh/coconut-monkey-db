import os

real_path = os.path.realpath(__file__)
fileName =  "db.txt"


def getSep() -> str:
    return "UISFDX YKJSDG OOOFSDFAS DBSFAS THECOOLDB"

def init() -> bool:
    try:
        open(real_path.split("coconutmonkey.py")[0]+fileName, "x")
        return True
    except:
        return False

init()

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
    return eval(res)

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

