'''

下拉列表控件（QComboBox）

1. 如果将列表项添加到QComboBox控件中

2. 如何获取选中的列表项

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')

        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby'])

        self.cb.currentIndexChanged.connect(self.selectionChange)
        # self.cb.currentIndexChanged.connect(lambda idx: self.selectionChange(idx))  # 同样的作用， self.cb.currentIndexChanged 会传回一个
        # idx索引给idx， 让lambda接收。此处 下拉索引发生改变时发射信号 传给selectionChange方法的 i
         
       

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))

        print('current index',i,'selection changed', self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
