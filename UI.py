# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtWidgets


class UiFrame(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InitFolder = QtWidgets.QPushButton(self.centralwidget)
        self.InitFolder.setGeometry(QtCore.QRect(90, 60, 90, 60))
        self.InitFolder.setObjectName("InitFolder")
        self.GenTXT = QtWidgets.QPushButton(self.centralwidget)
        self.GenTXT.setGeometry(QtCore.QRect(90, 180, 90, 60))
        self.GenTXT.setObjectName("GenTXT")
        self.GenPDF = QtWidgets.QPushButton(self.centralwidget)
        self.GenPDF.setGeometry(QtCore.QRect(420, 180, 90, 60))
        self.GenPDF.setObjectName("GenPDF")
        self.ReadTxt = QtWidgets.QPushButton(self.centralwidget)
        self.ReadTxt.setGeometry(QtCore.QRect(420, 60, 90, 60))
        self.ReadTxt.setObjectName("ReadTxt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "印卡生成器"))
        self.InitFolder.setText(_translate("MainWindow", "初始化"))
        self.GenTXT.setText(_translate("MainWindow", "生成卡组"))
        self.GenPDF.setText(_translate("MainWindow", "生成PDF"))
        self.ReadTxt.setText(_translate("MainWindow", "读取"))


class NewWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("N")
        self.resize(400, 200)
        self.TextLabel = QtWidgets.QLabel(self)
        self.TextLabel.setGeometry(QtCore.QRect(100, 50, 200, 100))
        self.TextLabel.setText("操作成功")
        self.TextLabel.setAlignment(QtCore.Qt.AlignHCenter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    newWin = NewWindow()
    newWin.show()
    sys.exit(app.exec_())
