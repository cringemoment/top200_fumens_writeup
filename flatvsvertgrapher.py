from json import loads
import matplotlib.pyplot as plt
import numpy as np

pbdata = loads(open("pbdata.json").read())

flattovert = open("flatvsvertall.txt").read().splitlines()
pbs = []
ratio = []

for i in flattovert:
    username, flat, vert = i.split(":")
    flattvertratio = int(flat) / int(vert)
    pbs.append(pbdata[username]["pb"])
    ratio.append(flattvertratio)

plt.plot(pbs, ratio, "o")

# Label every 5th point on the x-axis
label_indices = [pbs[i] for i in range(0, len(pbs), 1)]
plt.xticks(label_indices)

plt.xlabel('PBs')
plt.ylabel('Flat-to-Vert Ratio')
plt.title('Plotting Flat-to-Vert Ratio against PBs')

# Calculate the correlation coefficient
r_value = np.corrcoef(pbs, ratio)[0, 1]
plt.text(0.05, 0.95, f'r = {r_value:.2f}', transform=plt.gca().transAxes)

# Mirror the plot on the y-axis
plt.xlim(plt.xlim()[::-1])

plt.show()
