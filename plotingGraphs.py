import matplotlib.pyplot as plt

# Create a Python program to plot a graph, add a title, and label the axes. Use the following data for
# the x and y axes:
# x-axis data: [1, 2, 3, 4, 5]
# y-axis data: [2, 4, 6, 8, 10]
# 3. Write a Python program using Matplotlib to create a scatter plot. Plot the following
# points:
# (1, 2), (2, 3), (3, 5), (4, 7), (5, 11)

def plot_graph(x, y, plot_type="line", color="blue", marker="o", **kwargs):
    """
    Plots either a line or scatter graph based on the plot_type argument.
    Acts like an overloaded function.
    """
    if plot_type == "scatter":
        plt.scatter(x, y, color=color, marker=marker, s=kwargs.get("size", 80))
        plt.title("Scatter Plot Example")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
    elif plot_type == "line":
        plt.plot(x, y, color=color, marker=marker,
                 linestyle=kwargs.get("linestyle", "-"),
                 linewidth=kwargs.get("linewidth", 2))
        plt.title("Line Graph Example")
        plt.xlabel("Number")
        plt.ylabel("Value")
    else:
        print("Invalid plot type! Use 'line' or 'scatter'.")
        return
    
    plt.show()

# --- Example calls ---
plot_graph([1, 2, 3, 4, 5], [2, 3, 5, 7, 11], plot_type="scatter", color="red",linewidth=1)
plot_graph([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], plot_type="line", color="green", linewidth=1)
