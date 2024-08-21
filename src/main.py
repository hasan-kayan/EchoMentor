# gui/main_window.py

from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('EchoMentor - Network & Wi-Fi Security')
        
        # Layout
        layout = QVBoxLayout()

        # Example button for getting detailed network info
        self.network_info_btn = QPushButton('Get Network Info')
        self.network_info_btn.clicked.connect(self.get_network_info)
        layout.addWidget(self.network_info_btn)
        
        # More buttons for other functionalities...

        # Set layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_network_info(self):
        # Call your library function here
        from lib import get_detailed_network_info
        info = get_detailed_network_info()
        
        # Show the result in a message box
        QMessageBox.information(self, "Network Info", str(info))

    # Define more methods to handle other button clicks...
