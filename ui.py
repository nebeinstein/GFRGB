from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QFileDialog, QListWidget, QListView, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import *
import sys
import loader as ld
class MainWin(QMainWindow):
    lis = None
    img = None
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.statusBar().showMessage('Ready')
        self.setGeometry(100, 100, 900, 900)
        self.setMinimumSize(500, 500)
        self.setWindowTitle('Gluten Free Radioactive Green Beans')

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

        self.lis=QListWidget(self)
        self.lis.move(0, 20)
        x = None
        self.lis.currentItemChanged.connect(self.list_selection_changed)
        layout.addWidget(self.lis)

        self.img = QLabel(self)
        self.img.resize(800,800)
        self.img.move(200,20)
        layout.addWidget(self.img)
        self.show()

    def create_image_viewer(self, filepath):
        
        pass

    def import_action(self):
        filepath = self.show_import_folder_dialog()
        if(filepath == ''):
            return
        file_list = ld.clean_file_list(ld.get_files_in(filepath))
        print(file_list)
        self.lis.addItems(file_list)
        
    def show_import_folder_dialog(self):
        options = QFileDialog.Options()
        return QFileDialog.getExistingDirectory(self,"QFileDialog.getOpenFileName()", options=options)

    def resizeEvent(self,event):
        self.respond_to_resize()
    
    def respond_to_resize(self):
        self.lis.setGeometry(0, 20, 200, self.frameGeometry().height()-80)
    
    def list_selection_changed(self):
        print('List changed!')
        qpm = QPixmap(self.lis.currentItem().text())
        self.img.resize(qpm.width(),qpm.height())
        self.img.setPixmap(qpm)
        QApplication.processEvents()
    
    def process_image(self):
        processed = []
        current_selection = self.lis.currentItem().text()
        processed.append(current_selection)
        ld.process_image(current_selection)

        
if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    main = MainWin()
    sys.exit(app.exec_())
