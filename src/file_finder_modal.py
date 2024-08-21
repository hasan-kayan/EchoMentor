# gui/dialogs.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox

class InputDialog(QDialog):
    def __init__(self, prompt, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Input Required')
        
        layout = QVBoxLayout()
        self.label = QLabel(prompt)
        layout.addWidget(self.label)
        
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)
        
        # OK and Cancel buttons
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)
        
        self.setLayout(layout)
    
    def get_input(self):
        return self.input_field.text()
