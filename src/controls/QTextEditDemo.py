'''

QTextEdit控件

'''

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget) :
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.resize(300,320)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')

        self.buttonShowText = QPushButton('获取文本')
        self.buttonShowHTML = QPushButton('获取HTML')


        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonShowText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonShowHTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)

        self.buttonShowText.clicked.connect(self.onClick_ButtonToText)
        self.buttonShowHTML.clicked.connect(self.onClick_ButtonToHTML)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello World，世界你好吗？')           # 设置文字

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())                               # 获取文字，在控制台打印出来

    def onClick_ButtonHTML(self):                                        # 设置HTML
        self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')
    def onClick_ButtonToHTML(self):                                      # 获取HTML
        print(self.textEdit.toHtml())   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
