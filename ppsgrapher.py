from json import loads
import matplotlib.pyplot as plt
import numpy as np

pbdata = loads(open("pbdata.json").read())

pbs = []
ratio = []

for username in pbdata:
    if(pbdata[username]["pb"]/pbdata[username]["block count"] > 0.1):
        pbs.append(pbdata[username]["pb"])
        ratio.append(pbdata[username]["pb"]/pbdata[username]["block count"])

plt.plot(pbs, ratio, "o")

# Calculate the correlation coefficient
r_value = np.corrcoef(pbs, ratio)[0, 1]

plt.xlabel('PBs')
plt.ylabel('pc/piece')
plt.title('2L reliance for pb')

plt.text(0.05, 0.95, f'r = {r_value:.2f}', transform=plt.gca().transAxes)

# Mirror the plot on the y-axis
plt.xlim(plt.xlim()[::-1])

# Calculate a reasonable step size for x-axis ticks
min_tick_distance = 50  # Adjust this value as needed
x_ticks = np.arange(0, max(pbs) + min_tick_distance, min_tick_distance)
plt.xticks(x_ticks)

plt.show()
