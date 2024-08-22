from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QTextEdit, QLabel, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import psutil

# Add the parent directory of 'lib' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from lib import monitor_signal_strength, monitor_bandwidth_usage, analyze_channel_interference

class PerformanceMonitorWidget(QDialog):
    def __init__(self, parent=None):
        super(PerformanceMonitorWidget, self).__init__(parent)
        self.setWindowTitle("Performance Monitor")

        # Layout for the widget
        layout = QVBoxLayout(self)

        # Label
        self.label = QLabel("Wi-Fi Performance Monitor", self)
        layout.addWidget(self.label)

        # Text area to display results
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # Button to monitor signal strength
        self.monitor_signal_button = QPushButton("Monitor Signal Strength", self)
        self.monitor_signal_button.clicked.connect(self.display_signal_strength)
        layout.addWidget(self.monitor_signal_button)

        # Button to monitor bandwidth usage
        self.monitor_bandwidth_button = QPushButton("Monitor Bandwidth Usage", self)
        self.monitor_bandwidth_button.clicked.connect(self.display_bandwidth_usage)
        layout.addWidget(self.monitor_bandwidth_button)

        # Button to analyze channel interference
        self.analyze_channel_button = QPushButton("Analyze Channel Interference", self)
        self.analyze_channel_button.clicked.connect(self.display_channel_interference)
        layout.addWidget(self.analyze_channel_button)

        # Button to clear the results
        self.clear_button = QPushButton("Clear Results", self)
        self.clear_button.clicked.connect(self.clear_results)
        layout.addWidget(self.clear_button)

        # Matplotlib Figure and Canvas for plotting
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def display_signal_strength(self):
        result = monitor_signal_strength()
        self.result_text.append(f"Signal Strength: {result}\n")

    def display_bandwidth_usage(self):
        duration = 10  # Set duration for monitoring bandwidth usage
        bandwidth_data = monitor_bandwidth_usage(duration)
        self.result_text.append(f"Bandwidth Usage (Duration: {duration}s):\n{bandwidth_data}\n")
        self.plot_bandwidth_usage(bandwidth_data)

    def display_channel_interference(self):
        channel_data = analyze_channel_interference()
        self.result_text.append(f"Channel Interference:\n{channel_data}\n")
        self.plot_channel_interference(channel_data)

    def plot_bandwidth_usage(self, bandwidth_data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(["Download Speed", "Upload Speed"], 
               [float(bandwidth_data["Download Speed"].replace(" B/s", "")), 
                float(bandwidth_data["Upload Speed"].replace(" B/s", ""))])
        ax.set_ylabel("Speed (B/s)")
        ax.set_title("Bandwidth Usage")
        self.canvas.draw()

    def plot_channel_interference(self, channel_data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        channels = list(map(int, channel_data["Channels In Use"]))
        ax.hist(channels, bins=range(1, 13), edgecolor='black')
        ax.set_xticks(range(1, 13))
        ax.set_xlabel("Wi-Fi Channels")
        ax.set_ylabel("Number of Networks")
        ax.set_title(f"Channel Interference (Optimal: {channel_data['Optimal Channel Suggestion']})")
        self.canvas.draw()

    def clear_results(self):
        self.result_text.clear()
        self.figure.clear()
        self.canvas.draw()
