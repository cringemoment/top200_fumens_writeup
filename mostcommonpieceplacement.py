from py_fumen_py import decode
from json import dump

allfumens = open("top200fumens.txt").read().splitlines()
pieceplacements = {}

for i in allfumens:
    username, replay = i.split(": ")
    print(username)
    fumen = decode(replay)

    for i in fumen:
        operationname = f"{i.operation.mino}{i.operation.rotation}{i.operation.x}{i.operation.y}"
        if not operationname in pieceplacements:
            pieceplacements[operationname] = 1
        else:
            pieceplacements[operationname] += 1

dump(pieceplacements, open("mostcommonpieceplacements.json", "w"))
