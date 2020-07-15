from PyQt5.QtWidgets import QMainWindow,QApplication
from windowtest.main import Ui_MainWindow
import sys
import os
import time

class mainwin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.status=self.statusBar()
        self.status.showMessage('请保持互联网连接')
        self.setWindowTitle("主窗口测试程序")
        #time.sleep(5)


        #self.setStatusTip("确认已连接互联网")
    def status(self):
        if os.system("ping www.baidu.com")==True:
            self.status.showMessage("互联网已连接")
        else:
            self.status.showMessage("请检查网络连接")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=mainwin()
    form.show()

    sys.exit(app.exec_())