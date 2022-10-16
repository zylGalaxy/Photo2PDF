import PIL.Image
import os
import shutil

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


class ImgEditor:
    def __init__(self):
        self.PhotoPath = './photo/'
        self.TempPath = './temp/'
        if not os.path.isdir(self.TempPath):
            os.mkdir(self.TempPath)  # create the temp folder
        if not os.path.isdir(self.PhotoPath):
            os.mkdir(self.PhotoPath)  # create the folder
        self.imgDict = {}  # card path is the key and card number is the value
        self.imgPathList = []

    def cleanFolder(self):
        if os.path.isdir(self.TempPath):
            shutil.rmtree(self.TempPath)  # clean the './temp/' folder

        os.mkdir(self.TempPath)

    def initPathListAndDict(self):
        self.getImg()
        self.imgPathList = [self.transferImg(img) for img in self.imgPathList]
        self.imgDict = {imgName: 1 for imgName in self.imgPathList}

    def transferImg(self, img):
        # move images to './temp/' file and transfer .png file to .jpg file
        # to make the generated pdf file smaller
        imgName = os.path.splitext(img)[0]
        imgName = imgName.split('/')[-1]
        if not os.path.isdir(self.TempPath):
            os.mkdir(self.TempPath)  # create the folder

        storePath = self.TempPath + imgName + ".jpg"
        im = PIL.Image.open(img)
        if os.path.splitext(img)[1] == '.png':
            im = im.convert('RGB')
            im.save(storePath, quality=95)  # convert png files to jpg files
        else:
            im.save(storePath)
        # print("save successful")
        return storePath

    def getImg(self):
        # get the images from './photo/' path and store them in imgPathList
        if not os.path.isdir(self.PhotoPath):
            os.mkdir(self.PhotoPath)
            return []
        imgFormate = ['.jpg', '.png']
        self.imgPathList = [self.PhotoPath + name for name in os.listdir(self.PhotoPath) for item in imgFormate if
                            os.path.splitext(name)[1] == item]

    def generateTxtFile(self):
        # generate the 'deck.txt' file
        self.initPathListAndDict()
        txtPath = './deck.txt'
        if os.path.exists(txtPath):
            os.remove(txtPath)
        txtFile = open(txtPath, 'a', encoding="utf-8")
        for (cardName, cardNum) in self.imgDict.items():
            txtFile.write(os.path.splitext(cardName)[0].split('/')[-1] + ' ' + str(cardNum) + '\n')
        txtFile.close()
        # print("generate txt successful")

    def readTxtFile(self):
        # read the card names and numbers in 'deck.txt' file
        txtPath = './deck.txt'
        txtFile = open(txtPath, 'r', encoding='utf-8')
        for line in txtFile:
            if not line:
                continue
            lineList = line.split()
            cardNum = lineList[-1]
            cardName = line.split(cardNum)[0]
            cardNum = int(cardNum)
            cardPath = self.TempPath + cardName + ".jpg"
            cardNum = int(cardNum)
            if os.path.exists(cardPath):
                self.imgDict[cardPath] = cardNum
        txtFile.close()

    def generatePDF(self):
        # generate 'deck.pdf' that can be used for printing
        if os.path.exists('./deck.pdf'):
            os.remove('./deck.pdf')
        cardCanvas = canvas.Canvas("./deck.pdf", pagesize=A4)
        width, height = A4
        cardWidth = 59 * mm  # 59 * 86
        cardHeight = 86 * mm
        widthMargin = (width - cardWidth * 3) / 2
        heightMargin = (height - cardHeight * 3) / 2
        count = 0
        for cardPath, cardNum in self.imgDict.items():
            cardNum = int(cardNum)
            for i in range(cardNum):
                widthIdx = count % 3
                heightIdx = count // 3
                count = count + 1
                cardCanvas.drawImage(cardPath, widthMargin + cardWidth * widthIdx,
                                     heightMargin + cardHeight * heightIdx, cardWidth, cardHeight)
                if count == 9:
                    cardCanvas.showPage()
                    count = 0
        cardCanvas.save()


if __name__ == "__main__":
    editor = ImgEditor()
    editor.cleanFolder()
    editor.initPathListAndDict()
    editor.generateTxtFile()
    editor.readTxtFile()
    editor.generatePDF()