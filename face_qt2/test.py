from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
from face_qt2.untitled import Ui_MainWindow


class window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("测试")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=window()
    win.show()
    sys.exit(app.exec_())