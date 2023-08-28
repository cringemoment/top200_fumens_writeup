from py_fumen_py import decode
from json import dump
import re

allfumens = open("top200fumens.txt").read().splitlines()

setups = {}

for i in allfumens:
    username, replay = i.split(": ")
    print(username)
    fumen = decode(replay)
    print("decoded")

    flatt = 0
    vertt = 0

    lastpccount = 0

    for i in fumen:
        if(str(i.field).replace("\n", "") == "__________"):
            lastpccount = 0
        else:
            lastpccount += 1
        if(lastpccount == 4):
            testfield = str(i.field)
            testfield = re.sub("[IOSZJLT]", "X", testfield)
            if(testfield not in setups):
                setups[testfield] = 1
            else:
                setups[testfield] += 1

dump(setups, open("4psetupcolor", "w"))
print(setups)
