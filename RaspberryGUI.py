# -*- coding: utf-8 -*-

from src.mainWindow import Window
from PyQt5.QtWidgets import QApplication
from src.IoController import initIO
from src.mediaPlayer import MediaPlayer
from src.yamlReader import YamlReader
import sys




if __name__ == "__main__":
    
    initIO()
    app = QApplication(sys.argv)
    player = MediaPlayer()
    mainWin = Window()


    sys.exit(app.exec_())

