from PyQt5 import QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')
import pygame
from GUI import Ui_Piano_istrument

pygame.init()
pygame.mixer.init()

def pb0(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Drumb/Octave/Bass-Drum-1.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Drumb/Solo/E-Mu-Proteus-FX-Wacky-Snare.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Drumb/Spare/Bamboo.wav')
        pygame.mixer.music.play()
def pb1(ui):
    if ui.comboBox_for_tunes.currentIndex() == 0:
        pygame.mixer.music.load('instruments/Piano/Octave/A.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/1.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/1.wav')
        pygame.mixer.music.play()
def pb2(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/e.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/2.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/2.wav')
        pygame.mixer.music.play()
def pb3(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/f#.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/3.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/3.wav')
        pygame.mixer.music.play()
def pb4(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/f.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/4.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/4.wav')
        pygame.mixer.music.play()
def pb5(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g#.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/5.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/5.wav')
        pygame.mixer.music.play()
def pb6(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/6.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/6.wav')
        pygame.mixer.music.play()
def pb7(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g1.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/7.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/7.wav')
        pygame.mixer.music.play()
def pb8(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g2.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/8.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/8.wav')
        pygame.mixer.music.play()
def pb9(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g3.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/9.wav') ##unknow wave data format
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/9.wav')
        pygame.mixer.music.play()
def pb10(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g4.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/10.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/10.wav')
        pygame.mixer.music.play()
def pb11(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/g5.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex() == 1:
        pygame.mixer.music.load('instruments/Piano/Solo/11.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/11.wav')
        pygame.mixer.music.play()
def pb12(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Piano/Octave/a#.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Piano/Solo/12.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Piano/Spare/12.wav')
        pygame.mixer.music.play()

def g1(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Guitar/Octave/GTR1.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Guitar/Solo/1.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Guitar/Spare/1.wav')
        pygame.mixer.music.play()

def g2(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Guitar/Octave/cleanchord-B-02.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Guitar/Solo/5.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Guitar/Spare/2.wav')
        pygame.mixer.music.play()

def g3(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-B02-slap.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Guitar/Solo/2.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Guitar/Spare/3.wav')
        pygame.mixer.music.play()
def g4(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-E01-slap.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Guitar/Solo/3.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Guitar/Spare/4.wav')
        pygame.mixer.music.play()
def g5(ui):
    if ui.comboBox_for_tunes.currentIndex()==0:
        pygame.mixer.music.load('instruments/Guitar/Octave/chord-G.wav')
        pygame.mixer.music.play()
    elif ui.comboBox_for_tunes.currentIndex()==1:
        pygame.mixer.music.load('instruments/Guitar/Solo/4.wav')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('instruments/Guitar/Spare/5.wav')
        pygame.mixer.music.play()