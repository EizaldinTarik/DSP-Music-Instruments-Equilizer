from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import*
import matplotlib.ticker as ticker
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import pyqtgraph as pg
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import sourceGuitar
import pygame
from GUI import Ui_Piano_istrument
pygame.init()
pygame.mixer.init()
class Tones(QtWidgets.QWidget):
    def __init__(self) :
        super(Tones,self).__init__()
        self.ui = Ui_Piano_istrument()
        self.ui.setupUi(self)
        self.ui.Piano_Button_1.clicked.connect(self.pb1)
        self.ui.Piano_Button_2.clicked.connect(self.pb2)
        self.ui.Piano_Button_3.clicked.connect(self.pb3)
        self.ui.Piano_Button_4.clicked.connect(self.pb4)
        self.ui.Piano_Button_5.clicked.connect(self.pb5)
        self.ui.Piano_Button_6.clicked.connect(self.pb6)
        self.ui.Piano_Button_7.clicked.connect(self.pb7)
        self.ui.Piano_Button_above_1.clicked.connect(self.pb8)
        self.ui.Piano_Button_above_2.clicked.connect(self.pb9)
        self.ui.Piano_Button_above_3.clicked.connect(self.pb10)
        self.ui.Piano_Button_above_4.clicked.connect(self.pb11)
        self.ui.Piano_Button_above_5.clicked.connect(self.pb12)
        self.ui.DrumbButton.clicked.connect(self.pb0)
        self.ui.Guitar_button_1.clicked.connect(self.g1)
        self.ui.Guitar_button_2.clicked.connect(self.g2)
        self.ui.Guitar_button_3.clicked.connect(self.g3)
        self.ui.Guitar_button_4.clicked.connect(self.g4)
        self.ui.Guitar_button_5.clicked.connect(self.g5)
    print('lol2')
    def pb0(self):
        print('lol')
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Drumb/Octave/Bass-Drum-1.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Drumb/Solo/E-Mu-Proteus-FX-Wacky-Snare.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Drumb/Spare/Bamboo.wav')
            pygame.mixer.music.play()
    def pb1(self):
        if self.ui.comboBox_for_tunes.currentIndex() == 0:
            pygame.mixer.music.load('instruments/Piano/Octave/A.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/1.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/1.wav')
            pygame.mixer.music.play()
    def pb2(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/e.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/2.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/2.wav')
            pygame.mixer.music.play()
    def pb3(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/f#.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/3.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/3.wav')
            pygame.mixer.music.play()
    def pb4(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/f.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/4.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/4.wav')
            pygame.mixer.music.play()
    def pb5(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g#.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/5.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/5.wav')
            pygame.mixer.music.play()
    def pb6(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/6.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/6.wav')
            pygame.mixer.music.play()
    def pb7(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g1.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/7.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/7.wav')
            pygame.mixer.music.play()
    def pb8(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g2.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/8.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/8.wav')
            pygame.mixer.music.play()
    def pb9(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g3.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/9.wav') ##unknow wave data format
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/9.wav')
            pygame.mixer.music.play()
    def pb10(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g4.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/10.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/10.wav')
            pygame.mixer.music.play()
    def pb11(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g5.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/11.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/11.wav')
            pygame.mixer.music.play()
    def pb12(self):
         if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/a#.wav')
            pygame.mixer.music.play()
         elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Piano/Solo/12.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/12.wav')
            pygame.mixer.music.play()

    def g1(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/GTR1.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/1.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/1.wav')
            pygame.mixer.music.play()

    def g2(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanchord-B-02.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/5.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/2.wav')
            pygame.mixer.music.play()

    def g3(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-B02-slap.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/2.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/3.wav')
            pygame.mixer.music.play()
    def g4(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-E01-slap.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/3.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/4.wav')
            pygame.mixer.music.play()
    def g5(self):
        if self.ui.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/chord-G.wav')
            pygame.mixer.music.play()
        elif self.ui.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/4.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/5.wav')
            pygame.mixer.music.play()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Tones()
    application.show()
    app.exec_()

if __name__=="__main__":
    main()