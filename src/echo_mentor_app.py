import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from Components.tool_bar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the main window properties
        self.setWindowTitle("EchoMentor")
        self.setGeometry(300, 300, 800, 600)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the main layout for the central widget
        main_layout = QVBoxLayout(central_widget)

        # Create a horizontal layout to center the toolbar
        toolbar_layout = QHBoxLayout()

        # Initialize the toolbar
        self.toolBar = ToolBar(self)

        # Add the toolbar to the horizontal layout (centered)
        toolbar_layout.addStretch(1)
        toolbar_layout.addWidget(self.toolBar)
        toolbar_layout.addStretch(1)

        # Add the toolbar layout to the main layout
        main_layout.addLayout(toolbar_layout)

        # Add stretch to push the toolbar to the top middle
        main_layout.addStretch(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
