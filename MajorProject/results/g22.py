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

# Set green delay to 20 seconds for all lanes
green_delays = [20] * len(vehicle_counts)

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

# Data for bars
xpos = np.arange(len(vehicle_counts))
ypos = np.zeros(len(vehicle_counts))
zpos_red = np.zeros(len(vehicle_counts))
zpos_green = np.array(red_delays) + np.array(yellow_delays)  # Adjusted green starts
zpos_yellow = np.array(red_delays) + np.array(green_delays) + np.array(yellow_delays)  # Adjusted yellow starts

# Heights of bars
dx = np.ones(len(vehicle_counts)) * 0.5
dy = np.ones(len(vehicle_counts)) * 0.5
dz_red = red_delays
dz_green = green_delays
dz_yellow = yellow_delays

# Plot red bars
ax.bar3d(xpos, ypos, zpos_red, dx, dy, dz_red, color='red', zsort='average', label='Red Delay')

# Plot green bars
ax.bar3d(xpos, ypos, zpos_green, dx, dy, dz_green, color='green', zsort='average', label='Green Delay')

# Plot yellow bars
ax.bar3d(xpos, ypos, zpos_yellow, dx, dy, dz_yellow, color='yellow', zsort='average', label='Yellow Delay')

# Adding labels and title with white font color
ax.set_xlabel('Lanes', color='white')
ax.set_ylabel('Time (seconds)', color='white')
ax.set_zlabel('Phases', color='white')
ax.set_title('Traffic Signal Phases Over Time with Fixed Green Delay (3D View)', color='white')

# Set axis ticks and labels color
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

# Set background color
ax.set_facecolor('#1E1E1E')  # Darker background for the 3D plot
fig.patch.set_facecolor('#121212')  # Even darker background for the entire figure

# Add legend
red_patch = plt.Line2D([0], [0], color='red', lw=4, label='Red Delay')
green_patch = plt.Line2D([0], [0], color='green', lw=4, label='Green Delay')
yellow_patch = plt.Line2D([0], [0], color='yellow', lw=4, label='Yellow Delay')

legend = plt.legend(handles=[red_patch, green_patch, yellow_patch], loc='upper left', fontsize=12)
ax.add_artist(legend)

plt.tight_layout()
plt.show()
