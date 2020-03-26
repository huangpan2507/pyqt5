'''
代码分析博客： https://www.jb51.net/article/181522.htm
让控件支持拖拽动作
A.setDragEnabled(True)

B.setAcceptDrops(True)

B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发


'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox) :　　　　          #　我们需要重新实现某些方法才能使QComboBox接受拖放操作。因此我们创建了继承自QComboBox的MyComboBox类。
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):               # 拖动开始时，以及刚进入目标控件时调用
        print(e)
        #检测拖曳进来的数据是否包含文本，如有则接受，无则忽略
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self,e):                     # 重新实现了dragEnterEvent()方法
        self.addItem(e.mimeData().text())      # 我们定义了在drop事件发生时的行为。这里我们改变了按钮的文字。

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo,self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让QLineEdit控件可拖动 ,QLineEdit内置了对drag(拖动)操作的支持。我们只需要调用setDragEnabled()方法就可以了。

        combo = MyComboBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())
