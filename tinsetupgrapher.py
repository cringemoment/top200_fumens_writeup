from json import loads
import matplotlib.pyplot as plt
import numpy as np

pbdata = loads(open("pbdata.json").read())

flattovert = open("flatoververtratio.txt").read().splitlines()
pbs = []
ratio = []

for i in flattovert:
    username, used = i.split(":")
    pbs.append(pbdata[username]["pb"])
    ratio.append(float(used))

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
min_tick_distance = 50  # Adjust this value as needed
x_ticks = np.arange(0, max(pbs) + min_tick_distance, min_tick_distance)
plt.xticks(x_ticks)


plt.show()
