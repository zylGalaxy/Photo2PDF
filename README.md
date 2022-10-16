# Yo-Gi-Oh Card print assistant

- What is this?

  It is a small toy that can help you generate PDF files with A4 size using the Yo-Gi-Oh card photos you download.

- How to use this?

  You can download CardPrintAssistant.exe from [here]:https://github.com/zylGalaxy/Photo2PDF/raw/main/CardPrintAssistance.exe

  When you run the program, you can read the help.txt file and follow the instructions.

- Something about the source code.

  `UI.py` contains the source code of GUI part (using pyqt5) and `ImgageEdit.py` contains the whole process from reading all the photo names to generate the pdf file.

  If you want to run the code, remember to install PIL (Pillow), reportlab and PyQt5 packages.

- Notification.

  If you are using MacOS or Linux, remember to modify the following code in 53th line of main.py.

  ```python
  os.system('notepad help.txt')
  ```

  Also, there may be some problems because of my carelessness and if you find them, please contact me.

  My email is 675211085@qq.com.

