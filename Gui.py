import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Gui(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #geometry
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
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
        self.textbox = QLineEdit(self) #dispaly title
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        self.textbox.setReadOnly(True)
        self.textbox.setText("Started")

        layout.addWidget(self.textbox)

        buttonBlue = QPushButton('Select Movie', self)
        buttonBlue.clicked.connect(self.selectMovie)
        layout.addWidget(buttonBlue)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def selectMovie(self):
        self.textbox.setText("clicked")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())