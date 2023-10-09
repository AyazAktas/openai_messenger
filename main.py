import sys
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont

openai.api_key = "##"

class MessengerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('OpenAI Messenger')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.message_area = QTextEdit(self)
        self.message_area.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.message_area)

        self.input_area = QLineEdit(self)
        self.input_area.setFont(QFont("Arial", 12))
        self.input_area.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_area)

        self.send_button = QPushButton('Gönder', self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        self.conversation = ""

    def send_message(self):
        user_message = self.input_area.text()
        self.conversation += f'You: {user_message}\n\n'  # Boşluk ekledik
        self.message_area.setText(self.conversation)

        if 'çıkış' in user_message or 'quit' in user_message:
            self.close()
        else:
            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_message,
                max_tokens=4000,
                n=1,
                stop=None,
            )
            response = completion.choices[0].text
            self.conversation += f'AI: {response}\n\n'  # Boşluk ekledik
            self.message_area.setText(self.conversation)

def main():
    app = QApplication(sys.argv)
    ex = MessengerApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
