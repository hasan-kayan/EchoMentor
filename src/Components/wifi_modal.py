from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt6.QtCore import Qt
import sys
import os

# Add the parent directory of 'lib' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from lib import check_wpa3_support, check_wifi_encryption, detect_weak_encryption, save_security_protocol_history, get_security_protocol_history


class WifiSecurityModal(QDialog):
    def __init__(self, parent=None):
        super(WifiSecurityModal, self).__init__(parent)
        self.setWindowTitle("Wi-Fi Security Check")

        # Layout for the modal
        layout = QVBoxLayout(self)

        # Label
        self.label = QLabel("Wi-Fi Security Check Tool", self)
        layout.addWidget(self.label)

        # Text area to display results
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        # Button to check WPA3 support
        self.check_wpa3_button = QPushButton("Check WPA3 Support", self)
        self.check_wpa3_button.clicked.connect(self.check_wpa3_support)
        layout.addWidget(self.check_wpa3_button)

        # Button to check Wi-Fi encryption
        self.check_encryption_button = QPushButton("Check Wi-Fi Encryption", self)
        self.check_encryption_button.clicked.connect(self.check_wifi_encryption)
        layout.addWidget(self.check_encryption_button)

        # Button to detect weak encryption
        self.detect_weak_encryption_button = QPushButton("Detect Weak Encryption", self)
        self.detect_weak_encryption_button.clicked.connect(self.detect_weak_encryption)
        layout.addWidget(self.detect_weak_encryption_button)

        # Button to show security protocol history
        self.show_history_button = QPushButton("Show Security Protocol History", self)
        self.show_history_button.clicked.connect(self.show_security_protocol_history)
        layout.addWidget(self.show_history_button)

        # Button to save current security protocol to history
        self.save_history_button = QPushButton("Save Current Security Protocol to History", self)
        self.save_history_button.clicked.connect(self.save_security_protocol)
        layout.addWidget(self.save_history_button)

        # Button to clear the results
        self.clear_button = QPushButton("Clear Results", self)
        self.clear_button.clicked.connect(self.clear_results)
        layout.addWidget(self.clear_button)

    def check_wpa3_support(self):
        result = check_wpa3_support()
        self.result_text.append(f"WPA3 Support: {result}\n")

    def check_wifi_encryption(self):
        result = check_wifi_encryption()
        self.result_text.append(f"Wi-Fi Encryption: {result}\n")

    def detect_weak_encryption(self):
        result = detect_weak_encryption()
        self.result_text.append(f"Weak Encryption: {result}\n")

    def save_security_protocol(self):
        security_info = check_wifi_encryption()
        save_security_protocol_history(security_info)
        self.result_text.append("Security protocol information saved to history.\n")

    def show_security_protocol_history(self):
        history = get_security_protocol_history()
        if history:
            self.result_text.append("Security Protocol History:\n")
            for entry in history:
                self.result_text.append(f"{entry['timestamp']}: {entry['security_info']}\n")
        else:
            self.result_text.append("No security protocol history available.\n")

    def clear_results(self):
        self.result_text.clear()
