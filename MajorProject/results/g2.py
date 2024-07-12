import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Given vehicle counts for each lane
vehicle_counts = [3, 20, 18, 15]

# Constants for the formula
v = 10  # vehicle speed in m/s
L = 5   # average length of vehicles in meters
G = 2   # inter-vehicle gap in meters
yellow_delay = 2  # yellow delay in seconds (consistent for all lanes)

# Calculate green delay for each lane
green_delays = [(L + (vc - 1) * (L + G)) / v for vc in vehicle_counts]

# Calculate the total green delay considering all lanes
total_green_delay = sum(green_delays)

# Calculate red, yellow, and green delays for each lane
red_delays = []
yellow_delays = [yellow_delay] * len(vehicle_counts)
green_starts = []

current_time = 0
for gd in green_delays:
    red_delays.append(current_time)
    green_starts.append(current_time + yellow_delay)
    current_time += gd + yellow_delay

# Total cycle time is the maximum of all green start times plus green delay
total_cycle_time = max(green_starts) + max(green_delays)

# Plotting the 3D bar graph
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set background color
ax.set_facecolor('#2E2E2E')  # Dark grey background for the axes
fig.patch.set_facecolor('#1E1E1E')  # Darker grey background for the figure

# Data for bars
x = np.arange(len(vehicle_counts))
y = np.zeros(len(vehicle_counts))
z = np.zeros(len(vehicle_counts))

# Bar widths
dx = np.ones(len(vehicle_counts)) * 0.5
dy = np.ones(len(vehicle_counts)) * 0.5

# Plot red delays
red_bars = ax.bar3d(x, y, z, dx, dy, red_delays, color='#FF6F61', zsort='average', label='Red Delay')

# Plot green delays
green_bars = ax.bar3d(x, y, np.array(red_delays), dx, dy, green_delays, color='#6BFF61', zsort='average', label='Green Delay')

# Plot yellow delays
yellow_bars = ax.bar3d(x, y, np.array(red_delays) + np.array(green_delays), dx, dy, yellow_delays, color='#FFE761', zsort='average', label='Yellow Delay')

# Adding labels and title
ax.set_ylabel('Lanes', color='white')
ax.set_xlabel('Time (seconds)', color='white')
ax.set_zlabel('Delays', color='white')
ax.set_title('Traffic Signal Phases Over Time with Dynamic Green Delay', color='white')

# Set axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4'], color='white')
ax.set_yticks([])
ax.set_zticks(np.arange(0, total_cycle_time + 1, 10))

# Set the color of the tick labels
ax.tick_params(colors='white')

# Manually add legend
red_patch = plt.Line2D([0], [0], color='red', lw=4, label='Red Delay')
green_patch = plt.Line2D([0], [0], color='green', lw=4, label='Green Delay')
yellow_patch = plt.Line2D([0], [0], color='yellow', lw=4, label='Yellow Delay')

legend = plt.legend(handles=[red_patch, green_patch, yellow_patch], facecolor='#2E2E2E', edgecolor='white')
for text in legend.get_texts():
    text.set_color('white')

plt.tight_layout()
plt.show()
