'''
代码分析博客： https://blog.csdn.net/jia666666/article/details/81539733?utm_source=blogxgwz1

对话框：QDialog

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

QMainWindow ： 基本对话框上增加了菜单栏， 工具栏， 状态栏， 标题栏
QWidget ： 基本框口
QDialog ： 对话窗框口

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        
        # Qt.ApplicationModal： Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互，用户只有关闭弹窗后，才能关闭主界面
        # Qt.WindowModal:窗口模态，程序在未处理玩当前对话框时，将阻止和对话框的父窗口进行交互，可以直接关闭主界面，而不用先关闭弹窗
        # Qt.NonModal：非模态，可以和程序的其他窗口进行交互，用户只有关闭弹窗后，才能关闭主界面
        # 模态对话框（Modal Dialogue Box），一旦弹出，就不能对话框以外的窗口进行操作，必须先关闭对话框。

        dialog.exec()
        # 根据exec_()方法的返回值判断用户是【确定】还是【取消】了，当然也可以其他返回值，具体看文档。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())

