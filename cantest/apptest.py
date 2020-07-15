from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5 import QtWidgets,Qt
from cantest.camtest import Ui_Form
from PyQt5.QtGui import QIcon
import sys


class myapptest(QWidget,Ui_Form):
    def __init__(self):
        super(myapptest, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("CAMTEST")
        self.setWindowIcon(QIcon("timg.jpg"))

        #self.setStatusTip("请保持互联网连接")


        # desktop_geomtry = QtWidgets.QApplication.deleteLater(self)
        # #print(desktop_geomtry)
        rect=self.geometry()#获取窗口界面的大小
        window_width=rect.width()  #窗口宽
        window_height=rect.height()   #窗口高
        print(window_height,window_width)






if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=myapptest()
    win.show()

    sys.exit(app.exec_())