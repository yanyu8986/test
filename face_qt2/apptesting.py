import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
from PyQt5 import QtGui
from PyQt5 import Qt
from face_qt2.face_test2 import Ui_Form
from face.auth import auth
from face.options import options,images
import time
import cv2

class mywindow(QWidget,Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)




    def openfile(self):
        global imgName
        imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "图片选择",
                                                       "",
                                                       " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        # 利用qlabel显示图片
        global png
        png = QtGui.QPixmap(imgName).scaled(self.ui.label_2.width(), self.ui.label_2.height())
        self.ui.label_2.setPixmap(png)

        self.ui.lineEdit.setText(imgName)

    def face_field(self):
        face_field_list = []
        try:

            cilent=auth()
            if self.ui.checkBox.isChecked()==True:
                face_field_list.append("age")
            else:
                pass

            if self.ui.checkBox_2.isChecked()==True:
                face_field_list.append("beauty")
            else:
                pass

            if self.ui.checkBox_3.isChecked():
                face_field_list.append("expression")
            else:
                pass

            if self.ui.checkBox_4.isChecked():
                face_field_list.append('face_shape')
            else:
                pass

            if self.ui.checkBox_5.isChecked():
                face_field_list.append("emotion")
            else:
                pass

            if self.ui.checkBox_6.isChecked():
                face_field_list.append('gender')
            else:
                pass
        except:
            pass

        return face_field_list



    def echocv(self):
        try:
            # cvfile=cv2.imread(imgName)
            # cv2.namedWindow("AI",cv2.WINDOW_GUI_NORMAL)
            # cv2.imshow("AI",cvfile)
            # cvtest=auth()
            # cv=cvtest.detect(images(imgName),"BASE64")
            # cvdate=cv['result']["face_list"][0]['location']
            # cvdateleft=cvdate['left']
            # cvdatetop=cvdate['top']
            # cvdatew=cvdate['left']+cvdate['width']
            # cvdateh=cvdate['top']+cvdate['height']
            # print(cvdateh)
            # return cvdateleft,cvdatetop,cvdatew,cvdateh
            # cv2.rectangle(cvfile,(cvdateleft,cvdatetop),(cvdatew,cvdateh),(0, 0, 255), 3)
            #
            #
            #
            # cv2.waitKey()
            # cv2.destroyAllWindows()

            pass
        except:
            pass
        # cv2.rectangle(png, (384, 0), (510, 128), (0, 255, 0), 3)
        pass


    def face_72(self):
        pass


    def facetest(self):
        facedate={}
        face_list=self.face_field()
        print(face_list)
        facetest=auth()
        self.ui.textBrowser.append("检测中，请稍等...")

        for face in face_list:

            facexins=facetest.detect(images(imgName),"BASE64",options(face))
            print(facexins)
            facefield=facexins['result']["face_list"][0][face]
            print(facefield)
            facedate[face]=facefield
            time.sleep(1)
        for name in facedate.keys():
            try:
                if name=="age":

                    age="图片种检测到的人脸的年龄 {}".format(facedate["age"])
                    self.ui.textBrowser.append(age)

                if name=='beauty':
                    beauty="图片中检测到的人脸的颜值 {}".format(facedate["beauty"])
                    self.ui.textBrowser.append(beauty)
                if name=="expression":
                    if facedate["expression"]["type"]=="none":
                        expression="图片中检测到的人脸的表情为 不笑"
                    elif facedate["expression"]["type"]=="smile":
                        expression = "图片中检测到的人脸的表情为 微笑"
                    elif facedate["expression"]["type"]=="laugh":
                        expression = "图片中检测到的人脸的表情为 大笑"
                    self.ui.textBrowser.append(expression)
                else:
                    pass
                if name=="face_shape":
                    if facedate['face_shape']["type"]=="square":
                        face_shape="图片中检测到人脸的脸型为 正方形"
                    elif facedate['face_shape']["type"]=="triangle":
                        face_shape="图片中检测到人脸的脸型为 三角形"
                    elif facedate['face_shape']["type"]=="oval":
                        face_shape="图片中检测到人脸的脸型为 椭圆形"
                    elif facedate['face_shape']["type"]=="heart":
                        face_shape="图片中检测到人脸的脸型为 心形"
                    elif facedate['face_shape']["type"]=="round":
                        face_shape="图片中检测到人脸的脸型为 圆形"
                    self.ui.textBrowser.append(face_shape)
                else:
                    pass

                if name=="gender":
                    if facedate['gender']['type']=="male":
                        gender="图片中检测到的人脸的性别为 男性"
                    elif facedate['gender']['type']=="female":
                        gender="图片中检测到的人脸的性别为 女性"
                    self.ui.textBrowser.append(gender)
                else:
                    pass

                if name=="emotion":
                    if facedate['emotion']['type']=="angry":
                        emotion="图片中检测到人脸的情绪为 愤怒"
                    elif facedate['emotion']['type']=="disgust":
                        emotion="图片中检测到人脸的情绪为 厌恶"
                    elif facedate['emotion']['type']=="fear":
                        emotion="图片中检测到人脸的情绪为 恐惧"
                    elif facedate['emotion']['type']=="happy":
                        emotion="图片中检测到人脸的情绪为 高兴"
                    elif facedate['emotion']['type']=="sad":
                        emotion="图片中检测到人脸的情绪为 伤心"
                    elif facedate['emotion']['type']=="surprise":
                        emotion="图片中检测到人脸的情绪为 惊讶"
                    elif facedate['emotion']['type']=="neutral":
                        emotion="图片中检测到人脸的情绪为 无情绪"
                    self.ui.textBrowser.append(emotion)
                else:
                    pass
            except:
                pass
        self.ui.textBrowser.append("检测完成")
    def face_clear(self):
        self.ui .textBrowser.clear()
        self.ui.label_2.clear()
        self.ui.lineEdit.clear()
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_4.setChecked(False)
        self.ui.checkBox_5.setChecked(False)
        self.ui.checkBox_6.setChecked(False)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec_())
