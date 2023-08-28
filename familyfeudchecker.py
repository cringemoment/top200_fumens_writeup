from py_fumen_py import *

mostcommon = eval(open("mostcommonpieceplacements.json").read())
mostcommon = sorted(mostcommon, key=lambda x:x[1] * -1)

fumen = []
field = Field(field = "__________", garbage = "__________")
for i in mostcommon:
    po = i[0]
    operation = Operation(mino=Mino(int(po[0])), rotation=Rotation(int(po[1])), x = int(po[2]), y = int(po[3]))
    fumen.append(Page(field = field, operation = operation, comment = str(i[1])))

print(encode(fumen))
