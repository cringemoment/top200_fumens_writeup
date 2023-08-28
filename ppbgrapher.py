from json import loads
import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt

pbdata = loads(open("ultrapbdata.json").read())

pbs = []
ratio = []

for username in pbdata:
    pbs.append(pbdata[username]["pb"])
    ppb = pbdata[username]["pb"]/pbdata[username]["block count"]
    mn = ppb * sqrt(log(pbdata[username]["block count"], 10))
    print(sqrt(log(pbdata[username]["block count"], 10)))
    ratio.append(mn)

print(ratio)


plt.plot(pbs, ratio, "o")

# Calculate the correlation coefficient
r_value = np.corrcoef(pbs, ratio)[0, 1]

plt.xlabel('PBs')
plt.ylabel('ppb')
plt.title('ppb vs score')

plt.text(0.05, 0.95, f'r = {r_value:.2f}', transform=plt.gca().transAxes)

# Mirror the plot on the y-axis
plt.xlim(plt.xlim()[::-1])

# Calculate a reasonable step size for x-axis ticks
min_tick_distance = 50000  # Adjust this value as needed
x_ticks = np.arange(0, max(pbs) + min_tick_distance, min_tick_distance)
plt.xticks(x_ticks)

plt.show()
