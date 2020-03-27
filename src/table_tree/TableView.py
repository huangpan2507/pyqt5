'''
在通常情况下，一个应用需要和一批数据进行交互，然后以表格的形式输出这些信息，这时就需要用到QTableView类了，在QTableView中可以使用自定义的数据模型
来显示内容，通过setModel来绑定数据源
QTableWidget继承自QTableView，主要区别是QTableView可以使用自定义的数据模型来显示内容（先通setModel来绑定数据源），而QTableWidget自能使用标准
的数据模型，并且其单元格数据是通过QTableWidgetItem对象实现的，通常QTableWidget就能够满足我们的要求。

显示二维表数据（QTableView控件）

数据源

Model

需要创建QTableView实例和一个数据源（Model），然后将两者关联

MVC：Model   Viewer   Controller

MVC的目的是将后端的数据和前端页面的耦合度降低



'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableView(QWidget):

	def __init__(self, arg=None):
		super(TableView, self).__init__(arg)
		self.setWindowTitle("QTableView表格视图控件演示")
		self.resize(500,300);

		self.model = QStandardItemModel(4,3)
		self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])

		self.tableview = QTableView()
		# 关联QTableView控件和Model
		self.tableview.setModel(self.model)

		# 添加数据
		item11 = QStandardItem('10')
		item12 = QStandardItem('雷神')
		item13 = QStandardItem('2000')
		self.model.setItem(0,0,item11)
		self.model.setItem(0,1, item12)
		self.model.setItem(0,2, item13)

		item31 = QStandardItem('30')
		item32 = QStandardItem('死亡女神')
		item33 = QStandardItem('3000')
		self.model.setItem(2,0,item31)
		self.model.setItem(2,1, item32)
		self.model.setItem(2,2, item33)

		layout = QVBoxLayout()
		layout.addWidget(self.tableview)
		self.setLayout(layout)

		


if __name__ == '__main__':
	app = QApplication(sys.argv)	
	table = TableView()
	table.show()
	sys.exit(app.exec_())
