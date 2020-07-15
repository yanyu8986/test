from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
from PyQt5 import QtGui
from face_qt.face_ui import Ui_Form
import sys

from face.auth import auth
from face.options import options,images


class face_test(QWidget,Ui_Form):
    def __init__(self):
        super(face_test, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)


    def tupian(self):
        global imgName
        imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "图片选择",
                                                       "",
                                                       " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        # 利用qlabel显示图片
        png = QtGui.QPixmap(imgName).scaled(self.ui.label.width(), self.ui.label.height())
        self.ui.label.setPixmap(png)
        self.ui.lineEdit.setText(imgName)

    def jiance(self):
        face_fieldname = self.ui.comboBox.currentText()
        print(face_fieldname)
        facecodename = self.facename(face_fieldname)

        au = auth()
        cilent = au.detect(images(imgName), "BASE64", options(facecodename))
        print(len(cilent["result"]))

        #print(facecodename)
        jcxi=cilent['result']['face_list'][0][facecodename]
        print(type(jcxi))
        self.ui.textEdit.setText(str(jcxi))

    def clean(self):

        self.ui.textEdit.clear()


    def facename(self,face_fieldname):
        facecodename=""
        if face_fieldname=="年龄":
            facecodename="age"
        elif face_fieldname=="颜值":
            facecodename="beauty"
        elif face_fieldname=='表情':
            facecodename="expression"
        elif face_fieldname=='脸型':
            facecodename="face_shape"
        elif face_fieldname=="性别":
            facecodename='gender'
        elif face_fieldname=='情绪':
            facecodename="emotion"

        return facecodename

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=face_test()
    window.show()
    sys.exit(app.exec())