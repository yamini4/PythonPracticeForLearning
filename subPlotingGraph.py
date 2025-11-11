import matplotlib.pyplot as plt

# Write a Python program to create a 1x2 grid of subplots. The first subplot should show a simple
# line plot with data [1, 2, 3, 4] and [10, 20, 30, 40]. The second subplot should display a bar plot
# with the same x-axis values and corresponding y-axis values [5, 10, 15, 20].

# Data
x = [1, 2, 3, 4]
y_line = [10, 20, 30, 40]
y_bar = [5, 10, 15, 20]

# Create a 1x2 grid of subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns

# First subplot: Line plot
axs[0].plot(x, y_line, marker='o', color='blue', linestyle='-', linewidth=2)
axs[0].set_title("Line Plot")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")

# Second subplot: Bar plot
axs[1].bar(x, y_bar, color='orange')
axs[1].set_title("Bar Plot")
axs[1].set_xlabel("X-axis")
axs[1].set_ylabel("Y-axis")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
