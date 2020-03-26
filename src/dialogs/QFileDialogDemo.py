'''
代码分析博客： https://www.jb51.net/article/181511.htm

文件对话框：QFileDialog

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框演示 ')

    def loadImage(self):
        
        # 第一个参数self：用于指定父组件
        # 第二个参数‘open file’：是QFileDialog对话框的标题
        # 第三个参数‘C:\’默认打开的目录，‘.’代表程序运行的目录，‘/’代表当前盘下的根目录(window.linux系统),需要注意的是不同路径的显示方式，比如window平台下的C盘“C:\”等
        # 第四个参数是对话框中文件扩展名过滤器（fliter）,比如使用’Image files (.jpg .gif .png .jpeg)’表示只能显示扩展名为.jpg,.gif等文件
        
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')    
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        
        #　exec():显示一个模式对话框，并且锁住程序直到用户关闭该对话框为止。函数返回一个DialogCode结果（int型）。打开返回1  取消返回 0
        # 在对话框弹出期间，用户不可以切换同程序下的其它窗口，直到该对话框被关闭。
        # 模式与非模式 。模式对话框，就是在弹出窗口的时候，整个程序就被锁定了，处于等待状态，直到对话框被关闭。
        # 这时往往是需要对话框的返回值进行下面的操作。如：确认窗口（选择“是”或“否”）。
        # 非模式对话框，在调用弹出窗口之后，调用即刻返回，继续下面的操作。这里只是一个调用指令的发出，不等待也不做任何处理。如：查找框。

        if dialog.exec():
            filenames = dialog.selectedFiles()              # filenames为返回的地址
            
            f = open(filenames[0],encoding='utf-8',mode='r')
            with f:                                         # with open 自带close()方法
                data = f.read()
                self.contents.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
