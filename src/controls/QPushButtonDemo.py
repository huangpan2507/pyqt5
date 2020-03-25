'''
相关解读：https://www.jb51.net/article/181612.htm
按钮控件（QPushButton）

父类：QAbstractButton
以下为子类：
QPushButton
AToolButton
QRadioButton
QCheckBox


'''


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog) :
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))

        layout.addWidget(self.button1)

        # 在文本前面显示图像

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)                                        # 此属性确认按钮是否为默认按钮，如果按钮被设置为默认按钮，当按下回车键时，此属性设置为True的按钮（即对话框的默认按钮）将自动被按下。
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))   # 还可以通过lambda表达式来传递额外的参数btn，将clicked信号发送给槽函数whichButton（）
        # self.button4.clicked.connect(lambda button:self.whichButton(self.button4))    # lamdba 后面的button没有作用,可以忽略
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>') 
        
    """  
    def buttonState(self, button):
        if button.isChecked():
            print(button.text() + '已经被选中')
        else:
            print(button.text() + '未被选中')
            
            
           则，可以改为 self.button1.clicked.connect(lambda :self.buttonState(self.button1))
   
  """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
