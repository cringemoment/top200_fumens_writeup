import requests
import json

jstrisurl = "https://jstris.jezevec10.com/ultra"
pbsraw = requests.get(jstrisurl).text.splitlines()
pbdata = {}

for lineindex, line in enumerate(pbsraw):
    if 'class="ut">' in line:
        try:
            pblink = pbsraw[lineindex + 10].split('" target')[0].split('a href="')[1]
            username = pbsraw[lineindex + 1].replace("</a>", "")
            pbcount = pbsraw[lineindex + 3].replace("<td>", "").replace("</td>", "").replace("<strong>", "").replace("</strong>", "").replace(",", "")
            pps = pbsraw[lineindex + 6].replace("<td>", "").replace("</td>", "")
            blockcount = pbsraw[lineindex + 4].replace("<td>", "").replace("</td>", "")
            pbdata[username] = {}
            pbdata[username]["pb"] = int(pbcount)
            pbdata[username]["link"] = pblink
            pbdata[username]["pps"] = float(pps)
            pbdata[username]["block count"] = int(blockcount)
        except:
            print(line)
            print(pbsraw[lineindex + 10])
            pass

print(pbdata)
print(len(pbdata))
json.dump(pbdata, open("ultrapbdata.json", "w"))
