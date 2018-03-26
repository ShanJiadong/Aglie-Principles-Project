# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Starbucks.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        tmp = QWebEngineView()
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(tmp)

        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("星巴克数据分析")
        #tmp.load(QUrl('http://www.cnblogs.com/misoag/archive/2013/01/09/2853515.html'))
        tmp.load(QUrl('C:/Users/john/Desktop/data.html'))
        tmp.show()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 484)
        self.mapview = QtWidgets.QPushButton(Dialog)
        self.mapview.setGeometry(QtCore.QRect(640, 160, 111, 41))
        self.mapview.setObjectName("mapview")
        self.country_count = QtWidgets.QPushButton(Dialog)
        self.country_count.setGeometry(QtCore.QRect(640, 210, 111, 41))
        self.country_count.setObjectName("country_count")
        self.different_timezone = QtWidgets.QPushButton(Dialog)
        self.different_timezone.setGeometry(QtCore.QRect(640, 110, 111, 41))
        self.different_timezone.setObjectName("different_timezone")
        self.choropleth_map = QtWidgets.QPushButton(Dialog)
        self.choropleth_map.setGeometry(QtCore.QRect(640, 62, 111, 41))
        self.choropleth_map.setObjectName("choropleth_map")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "星巴克数据分析软件"))
        self.mapview.setText(_translate("Dialog", "查看世界分布"))
        self.country_count.setText(_translate("Dialog", "各国星巴克密度"))
        self.different_timezone.setText(_translate("Dialog", "标识不同时区"))
        self.choropleth_map.setText(_translate("Dialog", "国家密度渐变图"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    #widget = QtWidgets.QWidget()
    #screen = Ui_Dialog()
    #screen.setupUi(widget)
    #widget.show()
    screen.show()
    sys.exit(app.exec_())



