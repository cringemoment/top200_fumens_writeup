from json import loads
from py_fumen_py import encode, Field, Page

fullfumen = []

setupcount = loads(open("4psetupcolor").read())

setupcount = sorted(setupcount.items(), key=lambda x:x[1] * -1)
for index, i in enumerate(setupcount):
    setupcount[index] = list(i)
    tetrisfield = Field(field=i[0][:-10], garbage="__________")
    page = Page(field=tetrisfield, comment = str(i[1]))
    fullfumen.append(page)

print(encode(fullfumen))
