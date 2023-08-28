mostcommon = eval(open("mostcommonpieceplacements.json").read())

allplacements = []

for i in range(1, 8):
    for j in range(0, 3):
        for k in range(0, 8):
            for l in range(0, 4):
                temp = str(i) + str(j) + str(k) + str(l)
                allplacements.append(temp)

for i in allplacements:
    for j in mostcommon:
        if(i in j):
            break
    else:
        print(i)
