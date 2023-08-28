import requests
import json

jstrisurl = "https://jstris.jezevec10.com/PC-mode"
pbsraw = requests.get(jstrisurl).text.splitlines()
print(pbsraw)
pbdata = {}

for lineindex, line in enumerate(pbsraw):
    if "time-mil" in line:
        try:
            pblink = pbsraw[lineindex + 6].split('" target')[0].split('a href="')[1]
            username = pbsraw[lineindex - 3].replace("</a>", "")
            pbcount = pbsraw[lineindex - 1].replace("<td>", "").replace("</td>", "").replace("<strong>", "").replace("</strong>", "")
            pps = pbsraw[lineindex + 2].replace("<td>", "").replace("</td>", "")
            blockcount = pbsraw[lineindex + 1].replace("<td>", "").replace("</td>", "")
            pbdata[username] = {}
            pbdata[username]["pb"] = int(pbcount)
            pbdata[username]["link"] = pblink
            pbdata[username]["pps"] = float(pps)
            pbdata[username]["block count"] = int(blockcount)
        except:
            pass

print(pbdata)
print(len(pbdata))
json.dump(pbdata, open("pbdata.json", "w"))
