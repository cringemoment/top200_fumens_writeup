import requests
import lzstring

def translate_link(url):
    target = "jstris.jezevec10.com"
    parts = url.split("/")

    if parts[3] == "replay" and parts[2].endswith(target) and parts[4] != "1v1":
        type_val = 0
        if parts[4] == "live":
            type_val = 1
        elif parts[4] == "game":
            type_val = 3

        if len(parts) == 6 or len(parts) == 7:
            replay_id = parts[5]
        else:
            replay_id = parts[4]

        url2 = f"https://{parts[2]}/replay/data?id={replay_id}&type={type_val}"

        resp = requests.get(url2).text

        data = {
            'replay': lzstring.LZString.compressToEncodedURIComponent(resp)
        }

        # Make the POST request to the specified endpoint
        post_response = requests.post("https://fumen.tstman.net/jstris", data = data)

        # Parse the JSON response
        json_data = post_response.json()

        # Print the fumen data
        return(json_data['fumen'])

#print(translate_link("https://jstris.jezevec10.com/replay/68776000"))

jstrisurl = "https://jstris.jezevec10.com/PC-mode"
pbsraw = requests.get(jstrisurl).text.splitlines()
pblinks = []

added = 0
for lineindex, line in enumerate(pbsraw):
    if "time-mil" in line:
        try:
            pblink = pbsraw[lineindex + 6].split('" target')[0].split('a href="')[1]
            username = pbsraw[lineindex - 3].replace("</a>", "")
            fumen = translate_link(pblink)
            pblinks.append([fumen, username])
            added += 1
            print(f"On number {added}")
        except:
            added += 1
            pass

with open("top200fumenstest.txt", "w", encoding = "utf-8") as file:
    accum = ""
    for i in pblinks:
        accum += f"{i[1]}: {i[0]}\n"
    file.write(accum)
