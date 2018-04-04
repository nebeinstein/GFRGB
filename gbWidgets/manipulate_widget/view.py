from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit

print("importing ManipulateWidget...")
class ManipulateWidget(QWidget):
	grid = QGridLayout()
	# Button
	button = None
	# fields
	left_cut_text_field = None
	right_cut_text_field = None
	top_cut_text_field = None
	bottom_cut_text_field = None
	# field labels
	bottom_cut_text_label = None
	top_cut_text_label = None
	left_cut_text_label = None
	right_cut_text_label = None
	def __init__(self, ctrl):
		super().__init__()
		panel = self
		grid = QGridLayout()
		
		self.bottom_cut_text_field = QLineEdit()
		self.bottom_cut_text_field.textChanged.connect(ctrl.bottom_cut_text_field_changed)
		self.bottom_cut_text_label = QLabel()
		self.bottom_cut_text_label.setText("Bottom Cut")

		self.top_cut_text_field = QLineEdit()
		self.top_cut_text_field.textChanged.connect(ctrl.top_cut_text_field_changed)
		self.top_cut_text_label = QLabel()
		self.top_cut_text_label.setText("Top Cut")

		self.left_cut_text_field = QLineEdit()
		self.left_cut_text_field.textChanged.connect(ctrl.left_cut_text_field_changed)
		self.left_cut_text_label = QLabel()
		self.left_cut_text_label.setText("Left Cut")

		self.right_cut_text_field = QLineEdit()
		self.right_cut_text_field.textChanged.connect(ctrl.right_cut_text_field_changed)
		self.right_cut_text_label = QLabel()
		self.right_cut_text_label.setText("Right Cut")

		self.button = QPushButton("Process Image")
		self.button.setToolTip("This will process the given image and save it.")
		self.button.move(200, 850)
		self.button.clicked.connect(ctrl.process_button_pressed)

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

	