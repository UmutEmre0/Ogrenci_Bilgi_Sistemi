# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogr_ana_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 563)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 10, 91, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 195, 99);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("çıkış.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 181, 541))
        self.groupBox_3.setStyleSheet("background-color: rgb(164, 213, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 60, 161, 28))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 90, 161, 28))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 120, 161, 28))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 210, 551, 111))
        self.groupBox_2.setStyleSheet("background-color: rgb(164, 213, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 55, 281, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_RENC_G_R = QtWidgets.QMenu(self.menubar)
        self.menu_RENC_G_R.setTitle("")
        self.menu_RENC_G_R.setObjectName("menu_RENC_G_R")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_RENC_G_R.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ÖĞRENCİ ANA MENÜ"))
        self.pushButton_4.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.groupBox_3.setTitle(_translate("MainWindow", "MENÜ"))
        self.pushButton_5.setText(_translate("MainWindow", "GENEL BİLGİLER"))
        self.pushButton_6.setText(_translate("MainWindow", "NOTLAR"))
        self.pushButton_7.setText(_translate("MainWindow", "DEVAMSIZLIK"))
        self.groupBox_2.setTitle(_translate("MainWindow", "AKTİF AKADEMİK DÖNEM BİLGİLERİ"))
        self.label.setText(_translate("MainWindow", "2023-2024 GÜZ DÖNEMİ"))
