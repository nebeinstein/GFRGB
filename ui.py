from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QDockWidget

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import sys
import loader as ld
class MainWin(QMainWindow):
	lis = None
	img = None
	lay = None
	button = None
	edge_cut_text_field = None
	edge_cut_label = None
	blur_radius_text_field = None

	left_cut_text_field = None
	right_cut_text_field = None
	top_cut_text_field = None
	bottom_cut_text_field = None

	bottom_cut_text_label = None
	top_cut_text_label = None
	left_cut_text_label = None
	right_cut_text_label = None
	
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.lay = QHBoxLayout()
		self.setLayout(self.lay)
		self.statusBar().showMessage('Ready')
		self.setGeometry(100, 100, 900, 900)
		self.setMinimumSize(500, 500)
		self.setWindowTitle('Gluten Free Radioactive Green Beans')

		self.init_file_menu()
		self.init_list_view()
		self.init_image_viewer()
		self.init_manipulate_widget()
		
		self.show()

	def init_image_viewer(self):
		self.img = QLabel(self)
		self.img.resize(800,800)
		self.img.move(200,20)
		self.setCentralWidget(self.img)

	def init_list_view(self):
		dock = QDockWidget("Files", self)
		dock.setFeatures(QDockWidget.DockWidgetMovable)
		self.lis = QListWidget(self)
		self.lis.move(0, 20)
		self.lis.currentItemChanged.connect(self.list_selection_changed)
		dock.setWidget(self.lis)
		self.addDockWidget(1,dock)

	def init_file_menu(self):
		exit_item = QAction('&Exit', self)
		exit_item.setShortcut('Ctrl+Q')
		exit_item.setStatusTip('Exit Application')
		exit_item.triggered.connect(qApp.quit)

		import_item = QAction('&Import', self)
		import_item.setShortcut('Ctrl+I')
		import_item.triggered.connect(self.import_action)

		menubar = self.menuBar()
		file_menu = menubar.addMenu('&File')
		
		file_menu.addAction(import_item)
		file_menu.addAction(exit_item)

	def init_manipulate_widget(self):
		dock = QDockWidget("Manipulation")
		dock.setFeatures(QDockWidget.DockWidgetMovable)
		panel = QWidget()
		grid = QGridLayout()
		
		self.bottom_cut_text_field = QLineEdit()
		self.bottom_cut_text_field.textChanged.connect(self.bottom_cut_text_field_changed)
		self.bottom_cut_text_label = QLabel()
		self.bottom_cut_text_label.setText("Bottom Cut")

		self.top_cut_text_field = QLineEdit()
		self.top_cut_text_field.textChanged.connect(self.top_cut_text_field_changed)
		self.top_cut_text_label = QLabel()
		self.top_cut_text_label.setText("Top Cut")

		self.left_cut_text_field = QLineEdit()
		self.left_cut_text_field.textChanged.connect(self.left_cut_text_field_changed)
		self.left_cut_text_label = QLabel()
		self.left_cut_text_label.setText("Left Cut")

		self.right_cut_text_field = QLineEdit()
		self.right_cut_text_field.textChanged.connect(self.right_cut_text_field_changed)
		self.right_cut_text_label = QLabel()
		self.right_cut_text_label.setText("Right Cut")

		self.button = QPushButton("Process Image")
		self.button.setToolTip("This will process the given image and save it.")
		self.button.move(200, 850)
		self.button.clicked.connect(self.process_button_pressed)

		grid.addWidget(self.right_cut_text_field, 1, 1)
		grid.addWidget(self.left_cut_text_field, 2, 1)
		grid.addWidget(self.top_cut_text_field, 3, 1)
		grid.addWidget(self.bottom_cut_text_field, 4, 1)

		grid.addWidget(self.right_cut_text_label, 1, 0)
		grid.addWidget(self.left_cut_text_label, 2, 0)
		grid.addWidget(self.top_cut_text_label, 3, 0)
		grid.addWidget(self.bottom_cut_text_label, 4, 0)

		grid.addWidget(self.button, 5, 1)

		panel.setLayout(grid)
		dock.setWidget(panel)
		self.addDockWidget(Qt.LeftDockWidgetArea, dock)

	def bottom_cut_text_field_changed(self):
		try:
			ld.set_preproc_bottom_cut(int(self.bottom_cut_text_field.text()))
		except:
			pass
	def top_cut_text_field_changed(self):
		try:
			ld.set_preproc_top_cut(int(self.top_cut_text_field.text()))
		except:
			pass
	def left_cut_text_field_changed(self):
		try:
			ld.set_preproc_left_cut(int(self.left_cut_text_field.text()))
		except:
			pass
	def right_cut_text_field_changed(self):
		try:
			ld.set_preproc_right_cut(int(self.right_cut_text_field.text()))
		except:
			pass
	def edge_cut_changed(self):
		try:
			ld.set_preproc_edge_cut(int(self.edge_cut_text_field.text()))
		except:
			pass
	def import_action(self):
		filepath = self.show_import_folder_dialog()
		if(filepath == ''):
			return
		file_list = ld.clean_file_list(ld.get_files_in(filepath))
		self.lis.addItems(file_list)
		
	def show_import_folder_dialog(self):
		options = QFileDialog.Options()
		return QFileDialog.getExistingDirectory(self,"QFileDialog.getOpenFileName()", options=options)

	def resizeEvent(self,event):
		self.respond_to_resize()

	def respond_to_resize(self):
		pass

	def list_selection_changed(self):
		if(self.lis.currentItem() == None):
			return
		qpm = QPixmap(self.lis.currentItem().text())
		self.img.resize(qpm.width(),qpm.height())
		self.img.setPixmap(qpm)
		QApplication.processEvents()
	
	def process_button_pressed(self):
		self.process_image()

	def process_image(self):
		if(self.lis.currentItem() == None):
			return
		current_selection = self.lis.currentItem().text()
		ld.process_image(current_selection)
		filepath = current_selection[:current_selection.rfind('/')]
		file_list = ld.clean_file_list(ld.get_files_in(filepath))
		self.lis.clear()
		self.lis.addItems(file_list)

if(__name__ == '__main__'):
	app = QApplication(sys.argv)
	main = MainWin()
	sys.exit(app.exec_())
