# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 470)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 390, 61, 31))
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(406, 57, 71, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 114, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 100, 291, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 390, 371, 41))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(23, 440, 461, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label.setBuddy(self.textEdit)

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.tupian)
        self.pushButton.clicked.connect(Form.jiance)
        self.pushButton_2.clicked.connect(Form.clean)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸检测"))
        self.label_3.setText(_translate("Form", "检测信息"))
        self.toolButton.setText(_translate("Form", "图片选择"))
        self.label_2.setText(_translate("Form", "人脸检测系统"))
        self.comboBox.setItemText(0, _translate("Form", "年龄"))
        self.comboBox.setItemText(1, _translate("Form", "颜值"))
        self.comboBox.setItemText(2, _translate("Form", "表情"))
        self.comboBox.setItemText(3, _translate("Form", "脸型"))
        self.comboBox.setItemText(4, _translate("Form", "性别"))
        self.comboBox.setItemText(5, _translate("Form", "情绪"))
        self.pushButton_2.setText(_translate("Form", "清除"))
        self.pushButton.setText(_translate("Form", "测试人脸"))
