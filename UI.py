# -*- coding: utf-8 -*-
import sys
import typing

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget


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
'''
class NewWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("提示")
        self.resize(400, 250)
        self.TextLabel = QtWidgets.QLabel(self)
        self.TextLabel.setGeometry(QtCore.QRect(100, 50, 200, 100))
        self.TextLabel.setText("操作成功")
        self.TextLabel.setAlignment(QtCore.Qt.AlignHCenter)

        #self.Confirm = QtWidgets.QPushButton(self.centralwidget)
        #self.Confirm.setGeometry(QtCore.QRect(75, 200, 50, 25))
        #self.Confirm.setObjectName("Confirm")
'''
class NewWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("提示")
        self.resize(400, 250)
        self.TextLabel = QtWidgets.QLabel(self)
        self.TextLabel.setGeometry(QtCore.QRect(100, 50, 200, 100))
        self.TextLabel.setText("操作成功")
        self.TextLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.Confirm = QtWidgets.QPushButton("确定",self)
        self.Confirm.setGeometry(QtCore.QRect(175, 150, 50, 25))
        self.Confirm.setObjectName("Confirm")
        self.Confirm.clicked.connect(self.close)

class AssistWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("操作指南")
        self.resize(700,500)
        self.TextLabel = QtWidgets.QLabel(self)
        self.TextLabel.setGeometry(QtCore.QRect(100,100,500,400))
        self.TextLabel.setText("""
这是一个印卡生成器，如果遇到什么bug欢迎联系675211085@qq.com。
使用方法:
使用时先点击初始化，创建photo和temp目录;
将你要印的卡放入photo目录中;
点击生成卡组，此时当前目录下会生成名为"deck.txt"文件;
打开"deck.txt"编辑名称后对应的数字来确定印卡数量;
编辑完成后点击"读取"获得各卡牌的数量;
以上操作完成后点击"生成PDF"生成"deck.pdf。
你也可以在文件夹中找到help.txt来获得帮助。
                               """)
        self.TextLabel.setAlignment(QtCore.Qt.AlignHCenter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    newWin = NewWindow()
    newWin.show()
    sys.exit(app.exec_())
