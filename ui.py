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
		self.init_text_fields()
		self.button = QPushButton("Process Image", self)
		self.button.setToolTip("This will process the given image and save it.")
		self.button.move(200, 850)
		self.button.clicked.connect(self.process_button_pressed)
		self.show()

	def init_image_viewer(self):
		self.img = QLabel(self)
		self.img.resize(800,800)
		self.img.move(200,20)
		self.lay.addWidget(self.img)

	def init_list_view(self):
		self.lis=QListWidget(self)
		self.lis.move(0, 20)
		self.lis.currentItemChanged.connect(self.list_selection_changed)
		self.lay.addWidget(self.lis)

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

	def init_text_fields(self):
		self.edge_cut_text_field = QLineEdit(self)
		self.edge_cut_text_field.resize(50,24)
		self.edge_cut_text_field.textChanged.connect(self.edge_cut_changed)
		self.edge_cut_label = QLabel(self)
		self.edge_cut_label.setText("Edge Cut")
		self.edge_cut_label.resize(50,24)
		

	def edge_cut_changed(self):
		ld.set_preproc_edge_cut(int(self.edge_cut_text_field.text()))

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
		self.lis.setGeometry(0, 20, self.frameGeometry().width() // 5, self.frameGeometry().height() - 80)
		self.button.move(self.frameGeometry().width() // 5, 850)
		self.img.move(self.frameGeometry().width() // 5, 20)
		self.edge_cut_text_field.move((self.frameGeometry().width() // 4) + 150, 850)
		self.edge_cut_label.move(self.frameGeometry().width()//4 + 100 , 850)

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
