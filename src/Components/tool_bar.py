from PyQt6.QtWidgets import QToolBar, QMainWindow, QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtGui import QAction, QIcon

class ToolBar(QToolBar):
    def __init__(self, parent: QMainWindow):
        super(ToolBar, self).__init__(parent)
        self.setWindowTitle("Toolbar")

        # Define actions/buttons
        self.openModalAction = QAction(QIcon(None), "Open Modal", self)
        self.triggerWidgetAction = QAction(QIcon(None), "Trigger Widget", self)
        self.showInfoAction = QAction(QIcon(None), "Show Info", self)

        # Add actions to the toolbar
        self.addAction(self.openModalAction)
        self.addAction(self.triggerWidgetAction)
        self.addAction(self.showInfoAction)

        # Connect actions to their corresponding functions
        self.openModalAction.triggered.connect(self.open_modal)
        self.triggerWidgetAction.triggered.connect(self.trigger_widget)
        self.showInfoAction.triggered.connect(self.show_info)

    def open_modal(self):
        modal = QDialog(self)
        modal.setWindowTitle("Custom Modal")
        layout = QVBoxLayout()
        label = QLabel("This is a custom modal!", modal)
        closeButton = QPushButton("Close", modal)
        closeButton.clicked.connect(modal.accept)
        layout.addWidget(label)
        layout.addWidget(closeButton)
        modal.setLayout(layout)
        modal.exec()

    def trigger_widget(self):
        QMessageBox.information(self, "Trigger Widget", "Widget has been triggered!")

    def show_info(self):
        info_msg = QMessageBox(self)
        info_msg.setIcon(QMessageBox.Icon.Information)
        info_msg.setText("This is some information.")
        info_msg.setWindowTitle("Information")
        info_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        info_msg.exec()
