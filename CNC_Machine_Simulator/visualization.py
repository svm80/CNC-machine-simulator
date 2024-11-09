import matplotlib.pyplot as plt

def display_simulation(tool_path):
    # Visualize the tool path
    plt.plot([point[0] for point in tool_path], [point[1] for point in tool_path])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Tool Path Simulation')
    plt.show()
