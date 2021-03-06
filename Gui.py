import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QVBoxLayout, QHBoxLayout, QGroupBox, QListView
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSlot

import DatabaseController
import Main
import threading
import logging

class Gui(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='example.log', level=logging.DEBUG)

        #geometry
        self.initText = QStandardItem("Click genreate to select movie")
        self.db = DatabaseController.Controller()
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
        self.mainThread=threading.Thread(target=Main.main(self.db))
        self.mainThread.start()
        self.mainThread.join()

        self.commonList = self.db.selectComon()


        #print("LEN: "+len(self.commonList))
        x=self.commonList[0]
        title=x[0]
        rating=x[1]
        info=x[2]
        tmp = QStandardItem(str(title)+str(rating)+str(info))
        logtmp=(str(title)+str(rating)+str(info)).encode("utf-8")

        self.logger.debug("Napis=%s",logtmp)
        #print("GUI: "+str(tmp))
        self.model.appendRow(tmp)

        self.model.removeRow(0)
        self.textbox.setModel(self.model)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())