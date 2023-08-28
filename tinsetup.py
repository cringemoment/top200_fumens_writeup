from py_fumen_py import decode

allfumens = open("top200fumens.txt").read().splitlines()

for i in allfumens:
    username, replay = i.split(": ")
    fumen = decode(replay)

    tused = 0

    lastpccount = 0

    for i in fumen:
        if(str(i.field).replace("\n", "") == "__________"):
            lastpccount = 0
        else:
            lastpccount += 1
        if(lastpccount <= 4):
            if(i.operation.mino == 5):
                tused += 1

    print(f"{username}:{tused}")
