'''

单选按钮控件（QRadioButton）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        
        layout.addWidget(self.button2)
        self.setLayout(layout)


    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')
    """
    def btnstate(self,btn):
        if btn.isChecked() == True:
               print('<' + btn.text() + '> 被选中')
        else:
            print('<' + btn.text() + '> 被取消选中状态')
            
      # 当选择两个按钮相互切换时，按钮的状态发生改变，将触发toggle信号，并与槽函数btnstate（）连接。使用lamdba的方式允许将源信号传递给槽函数，将按钮作为参数     
      则 可以改为 self.btn1.toggled.connect(lambda :self.btnstate(self.btn1))
      self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))            
      
    """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
