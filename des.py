# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 263)
        MainWindow.setMinimumSize(QtCore.QSize(322, 224))
        MainWindow.setMaximumSize(QtCore.QSize(322, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setGeometry(QtCore.QRect(140, 80, 41, 31))
        self.pushButton_right.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ArrowR1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_right.setIcon(icon)
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setGeometry(QtCore.QRect(140, 120, 41, 31))
        self.pushButton_left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/ArrowL1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_left.setIcon(icon1)
        self.pushButton_left.setObjectName("pushButton_left")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 121, 171))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(190, 80, 121, 171))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter.setGeometry(QtCore.QRect(270, 50, 41, 23))
        self.pushButton_enter.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/enter-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_enter.setIcon(icon2)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(60, 10, 41, 31))
        self.pushButton_save.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon3)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.pushButton_open.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon_open_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon4)
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.pushButton_exit.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon5)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_dalete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dalete.setGeometry(QtCore.QRect(140, 220, 41, 31))
        self.pushButton_dalete.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon_garbage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dalete.setIcon(icon6)
        self.pushButton_dalete.setObjectName("pushButton_dalete")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import res_rc
