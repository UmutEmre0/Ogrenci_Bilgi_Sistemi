# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogr_ders_prog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(947, 629)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 30, 701, 541))
        self.tableWidget.setStyleSheet("background-color: rgb(198, 211, 255);\n"
"background-color: rgb(208, 227, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 20, 71, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 195, 99);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri dönme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ÖĞRENCİ DERS PROGRAMI"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1. Ders"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2. Ders"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PAZARTESİ"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "SALI "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ÇARŞAMBA"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "PERŞEMBE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "CUMA"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "Python Programlama"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "Yazılım Tasarımı Ve Mimarisi"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "Biçimsel Diller"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "Veri Tabanı"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "Algoritma Analizi"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "GERİ"))
