import matplotlib.pyplot as plt
import datetime

# Sample data
vehicle_counts = [15, 20, 18, 3, 22, 7, 13]
times = [datetime.datetime.now() - datetime.timedelta(minutes=i*5) for i in range(len(vehicle_counts))]

# Plotting the area plot
plt.figure(figsize=(10, 6))
plt.fill_between(times, vehicle_counts, color="skyblue", alpha=0.4)
plt.plot(times, vehicle_counts, color="Slateblue", alpha=0.6, linewidth=2)

# Formatting labels and title with increased font size
plt.xlabel('Time', fontsize=20)
plt.ylabel('Vehicle Count', fontsize=20)
plt.title('Vehicle Count Over Time', fontsize=20)

# Auto format x-axis labels
plt.gcf().autofmt_xdate()

plt.grid(False)
plt.tight_layout()
plt.show()
