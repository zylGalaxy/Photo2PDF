import os
import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import ImageEdit
import UI


class GUI(QMainWindow, UI.UiFrame):
    def __init__(self):
        super(GUI, self).__init__()
        self.editor = ImageEdit.ImgEditor()
        self.ChildrenWindow = UI.NewWindow()
        self.MainWindow = QMainWindow
        self.setupUi(self)
        self.retranslateUi(self)
        self.InitFolder.clicked.connect(self.InitFolderFunc)
        self.GenTXT.clicked.connect(self.GenTxtFunc)
        self.GenPDF.clicked.connect(self.GenPDFFunc)
        self.ReadTxt.clicked.connect(self.ReadTextFunc)

    def InitFolderFunc(self):
        self.editor.cleanFolder()
        self.ChildrenWindow.show()

    def GenTxtFunc(self):
        self.editor.generateTxtFile()
        self.ChildrenWindow.show()

    def GenPDFFunc(self):
        self.editor.generatePDF()
        self.ChildrenWindow.show()

    def ReadTextFunc(self):
        self.editor.initPathListAndDict()
        self.editor.readTxtFile()
        self.ChildrenWindow.show()


if __name__ == '__main__':
    if not os.path.exists('./help.txt'):
        HelpTxt = open('./help.txt', 'w', encoding="utf-8")
        helpList = ['这是一个印卡生成器，如果遇到什么bug欢迎联系675211085@qq.com\n',
                    '使用方法:\n',
                    '使用时先点击初始化，创建photo和temp目录;\n',
                    '将你要印的卡放入photo目录中;\n',
                    '点击生成卡组，此时当前目录下会生成名为"deck.txt"文件;\n',
                    '打开"deck.txt"编辑名称后对应的数字来确定印卡数量;\n',
                    '编辑完成后点击"读取"获得各卡牌的数量;\n',
                    '以上操作完成后点击"生成PDF"生成"deck.pdf。"']
        HelpTxt.writelines(helpList)
        HelpTxt.close()
    os.system('notepad help.txt')
    if not os.path.exists('./photo'):
        os.mkdir('./photo')
    if not os.path.exists('./temp'):
        os.mkdir('./temp')
    if not os.path.exists('./deck.txt'):
        deck = open('./deck.txt', 'w', encoding="utf-8")
        deck.close()
    app = QApplication(sys.argv)
    mainWindow = GUI()
    mainWindow.show()
    assistWindow = UI.AssistWindow()
    assistWindow.show()
    sys.exit(app.exec_())
