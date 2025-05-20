import matplotlib.pyplot as plt
import numpy as np
import random
import time
from google.colab import files

# Simulating the autonomous vehicle system with random performance metrics
def simulate_performance_metrics():
    metrics = [
        "Navigation Accuracy",
        "Obstacle Avoidance",
        "Decision Speed",
        "System Reliability",
        "Load Handling"
    ]
    # Random values between 70 and 100 to simulate performance percentages
    values = [random.randint(70, 100) for _ in range(len(metrics))]
    return metrics, values

# Function to visualize the performance metrics as a bar chart
def plot_performance_graph(metrics, values):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(metrics, values, color='skyblue')

    # Add value labels on each bar
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # Vertical offset
                     textcoords="offset points",
                     ha='center', fontsize=10)

    # Add titles and labels
    plt.title("Autonomous Vehicles and Robotics: Performance Metrics", fontsize=14, fontweight='bold')
    plt.xlabel("Metrics")
    plt.ylabel("Performance (%)")
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the chart to a file
    plt.tight_layout()
    plt.savefig("performance_metrics_chart.png")
    plt.show()

# Function to simulate the process of testing the vehicle's performance
def simulate_testing():
    print("Simulating Autonomous Vehicle System Testing...\n")
    time.sleep(2)
    print("Testing in Progress...\n")
    time.sleep(3)

    metrics, values = simulate_performance_metrics()

    print("\nPerformance Metrics Generated:")
    for metric, value in zip(metrics, values):
        print(f"{metric}: {value}%")

    print("\nVisualization of Performance Metrics:")
    plot_performance_graph(metrics, values)

# Main function
def main():
    print("Welcome to the Autonomous Vehicles and Robotics System Simulation!")

    # Simulate system testing
    simulate_testing()

    # Provide the option to download the chart
    print("\nDownload the performance metrics chart:")
    files.download("performance_metrics_chart.png")

if __name__ == "__main__":
    main()
