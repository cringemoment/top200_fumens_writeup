from json import loads
import matplotlib.pyplot as plt
import numpy as np
import math

pbdata = loads(open("pbdata.json").read())

pbs = []
ratio = []

for username in pbdata:
    if pbdata[username]["pb"] / pbdata[username]["block count"] >= 0.1:
        pbs.append(math.log(pbdata[username]["pb"]))
        ratio.append(pbdata[username]["pb"] / pbdata[username]["block count"])

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

# Set x-axis to logarithmic scale

plt.show()
