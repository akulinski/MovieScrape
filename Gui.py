import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QVBoxLayout, QHBoxLayout, QGroupBox, QListView
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSlot

import DatabaseController
import Main


class Gui(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #geometry
        self.initText = QStandardItem("Click genreate to select movie")
        self.db=db=DatabaseController.Controller()

        self.left = 500
        self.top = 50
        self.width = 320
        self.height = 300
        self.setUp()
        #self.interface()

        self.show()

    def setUp(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Choose next movie to watch")
        layout = QHBoxLayout()

        # Create textbox
        self.textbox = QListView(self) #dispaly title
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.model = QStandardItemModel(self.textbox)
        self.model.appendRow(self.initText)
        self.textbox.setModel(self.model)
        layout.addWidget(self.textbox)

        buttonBlue = QPushButton('Select Movie', self)
        buttonBlue.clicked.connect(self.selectMovie)
        layout.addWidget(buttonBlue)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def selectMovie(self):
        Main.main()
        #self.commonList=self.db.selectComon()

        '''for x in self.commonList:
            title=x[0]
            rating=x[1]
            info=x[2]
            tmp = QStandardItem(str(title)+str(rating)+str(info))
            self.model.appendRow(tmp)'''
        #self.model.removeRow(0)
        #self.textbox.setModel(self.model)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())