'''
代码分析博客：https://www.jb51.net/article/181509.htm
QInputDialog控件是一个标准对话框，有一个文本框和两个按钮（ok和cancel）组成，当用户单击ok或enter键后，在父窗口可以收集通过QInputDialog控件输入
的信息，QInputDialog控件是QDialog标准对话框的一部分。在QInpuTDialog控件中可以输入数字，字符串或列表中的选项，标签用于提示必要的信息
输入对话框：QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')
        layout = QFormLayout()

        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.button1, self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.lineEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
       
        #获取item输入的值，以及ok键的点击与否（True 或False）
        #QInputDialog.getItem(self,标题,文本,元组,元组默认index,是否允许更改)
        #　当调用QInputDialog.getItem（）函数时，QInputDialog控件包含一个QComboBox控件和两个按钮，用户从QComboBox中选择一个选项后，
        # 允许用户确认或取消操作
       
        
        item, ok =QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)
    def getText(self):
        text, ok =QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)
    def getInt(self):
        num, ok =QInputDialog.getInt(self,'整数输入框','输入数字')
        if ok and num:
            self.lineEdit3.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
