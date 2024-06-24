import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class SMSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SMS App')
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.label = QLabel('Enter your message:', self)
        layout.addWidget(self.label)

        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.send_button = QPushButton('Send SMS', self)
        layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.on_click)

        self.central_widget.setLayout(layout)

    pyqtSlot()
    def on_click(self):
        message = self.textbox.text()
        print(f'SMS Sent: {message}')
        self.label.setText(f'SMS Sent: {message}')
        self.textbox.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SMSApp()
    ex.show()
    sys.exit(app.exec_())
