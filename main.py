from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QSizePolicy, QLineEdit

import sys, platform, subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("uCalc")
        self.setGeometry(100, 100, 250, 450)

        buttons = ["%", "CE", "C", "⌫", "1/x", "x²", "√", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]
        self.numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
        self.operators = ["+", "-", "*", "/", "x²", "√", "1/x", "%"]

        layout = QVBoxLayout()
        layout.setSpacing(0)

        self.textbox = QLineEdit()
        self.textbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.textbox.setFixedHeight(75)
        self.textbox.setContentsMargins(0, 0, 0, 10)
        self.textbox.returnPressed.connect(self.buttonClicked)
        font = self.textbox.font()
        font.setPointSize(30)
        self.textbox.setFont(font)
        layout.addWidget(self.textbox)

        for i in range(0, len(buttons), 4):
            row = QHBoxLayout()
            row.setSpacing(0)
            for j in range(4):
                if i + j < len(buttons):
                    button = QPushButton(buttons[i + j])
                    button.clicked.connect(self.buttonClicked)
                    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    if buttons[i + j] == "=":
                        button.setStyleSheet("background-color: #4bc3ff; color: white;")
                    row.addWidget(button)
            layout.addLayout(row)

        self.setLayout(layout)

    def buttonClicked(self):
        button = self.sender()
        if button.text() in self.numbers:
            self.textbox.setText(self.textbox.text() + button.text())
        elif button.text() in self.operators:
            self.textbox.setText(self.textbox.text() + " " + button.text() + " ")
        elif button.text() == "CE":
            self.textbox.setText("")
        elif button.text() == "C":
            self.textbox.setText("")
        elif button.text() == "⌫":
            self.textbox.setText(self.textbox.text()[:-1])
        elif button.text() == "=" or "QLineEdit" in str(button):
            try:        
                result = eval(self.textbox.text().replace("x²", "**2").replace("√", "**0.5").replace("1/x", "**-1").replace("%", "/100"))
                try:
                    result = round(result, 13)
                except:
                    pass
                self.textbox.setText(str(result))
                self.textbox.setCursorPosition(0)
            except Exception as e:
                self.textbox.setText("Error: " + str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.setStyle("Windows")
    app.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 10px; background-color: transparent; font-size: 20px; margin: 2px}")
    sys.exit(app.exec_())
