import matplotlib.pyplot as plt

# Sample data for system performance metrics
labels = ['Congestion control', 'Emergency Vehicle Detection', 'Idle Time']
sizes = [60, 37, 3]  # Proportions of time spent in each state (in percentages)
colors = ['#66b3ff', '#ff9999', '#99ff99']  # Colors for each slice
explode = (0.1, 0, 0)  # Explode the first slice (Normal Operation)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140,
        textprops={'fontsize': 20})  # Increase font size here
plt.title('System Performance Metrics', fontsize=16)  # Increase title font size
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
