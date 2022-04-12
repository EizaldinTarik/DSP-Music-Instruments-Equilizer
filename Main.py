from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import*
import winsound
import matplotlib.ticker as ticker
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import pyqtgraph as pg
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
import vlc
import queue
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import sourceGuitar
import pygame

import logging
logging.basicConfig(level=logging.INFO, filename='logging.log',format='%(asctime)s %(message)s')
                   #datefmt='%m/%D/%Y %I:%M:%S %p', encoding='utf-8')



pygame.init()
pygame.mixer.init()


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()
        
class MplCanvas_Spec(FigureCanvas):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas_Spec,self).__init__(fig)
		fig.tight_layout()

class Worker(QtCore.QRunnable):

    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
                self.function(*self.args, **self.kwargs)

class Ui_Piano_istrument(object):
    def setupUi(self, Piano_istrument):
        Piano_istrument.setObjectName("Piano_istrument")
        Piano_istrument.resize(1245, 881)
        Piano_istrument.setStyleSheet("#Piano_Button_1,#Piano_Button_2,#Piano_Button_3,#Piano_Button_4,#Piano_Button_5,#Piano_Button_6,#Piano_Button_7\n"
"{\n"
"background-color: rgb(250, 250, 250);\n"
"}\n"
"#Piano_Button_1:hover,#Piano_Button_2:hover,#Piano_Button_3:hover,#Piano_Button_4:hover,#Piano_Button_5:hover,#Piano_Button_6:hover,#Piano_Button_7:hover\n"
"{\n"
"background-color: rgb(240, 240, 250);\n"
"}\n"
"\n"
"#Piano_Button_1:pushed,#Piano_Button_2:pushed,#Piano_Button_3:pushed,#Piano_Button_4:pushed,#Piano_Button_5:pushed,#Piano_Button_6:pushed,#Piano_Button_7:pushed\n"
"{\n"
"background-color: rgb(255, 255, 0)\n"
"}\n"
"\n"
"#Piano_Button_above_1,#Piano_Button_above_2,#Piano_Button_above_3,#Piano_Button_above_4,#Piano_Button_above_5\n"
"{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"#Piano_Button_above_1:hover,#Piano_Button_above_2:hover,#Piano_Button_above_3:hover,#Piano_Button_above_4:hover,#Piano_Button_above_5:hover,DrumbButton:hover\n"
"{\n"
"background-color: rgb(75, 75, 75);\n"
"}\n"
"#Piano_Button_above_1:pushed,#Piano_Button_above_2:pushed,#Piano_Button_above_3:pushed,#Piano_Button_above_4:pushed,#Piano_Button_above_5:pushed,DrumbButton:pushed\n"
"{\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Piano_istrument)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgets = QtWidgets.QTabWidget(Piano_istrument)
        self.tabWidgets.setObjectName("tabWidgets")
        self.musicTab = QtWidgets.QWidget()
        self.musicTab.setWhatsThis("")
        self.musicTab.setObjectName("musicTab")
        self.frameForPiano = QtWidgets.QFrame(self.musicTab)
        self.frameForPiano.setGeometry(QtCore.QRect(40, 50, 371, 211))
        self.frameForPiano.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameForPiano.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameForPiano.setObjectName("frameForPiano")
        self.gridLayout = QtWidgets.QGridLayout(self.frameForPiano)
        self.gridLayout.setObjectName("gridLayout")
        self.backGroundForPiano = QtWidgets.QLabel(self.frameForPiano)
        self.backGroundForPiano.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(148, 118, 254, 255), stop:1 rgba(71, 255, 243, 255))")
        self.backGroundForPiano.setText("")
        self.backGroundForPiano.setObjectName("backGroundForPiano")
        self.gridLayout.addWidget(self.backGroundForPiano, 0, 0, 1, 1)
        self.backGroundForSubPiano = QtWidgets.QLabel(self.frameForPiano)
        self.backGroundForSubPiano.setGeometry(QtCore.QRect(10, 10, 351, 61))
        self.backGroundForSubPiano.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.backGroundForSubPiano.setText("")
        self.backGroundForSubPiano.setObjectName("backGroundForSubPiano")
        self.Piano_Button_above_4 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_above_4.setGeometry(QtCore.QRect(240, 30, 40, 130))
        self.Piano_Button_above_4.setText("")
        self.Piano_Button_above_4.setObjectName("Piano_Button_above_4")
        self.Piano_Button_6 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_6.setGeometry(QtCore.QRect(260, 70, 50, 130))
        self.Piano_Button_6.setText("")
        self.Piano_Button_6.setObjectName("Piano_Button_6")
        self.Piano_Button_above_5 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_above_5.setGeometry(QtCore.QRect(290, 30, 40, 130))
        self.Piano_Button_above_5.setText("")
        self.Piano_Button_above_5.setObjectName("Piano_Button_above_5")
        self.Piano_Button_4 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_4.setGeometry(QtCore.QRect(160, 70, 50, 130))
        self.Piano_Button_4.setText("")
        self.Piano_Button_4.setObjectName("Piano_Button_4")
        self.Piano_Button_7 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_7.setGeometry(QtCore.QRect(310, 70, 50, 130))
        self.Piano_Button_7.setText("")
        self.Piano_Button_7.setObjectName("Piano_Button_7")
        self.Piano_Button_above_1 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_above_1.setGeometry(QtCore.QRect(40, 30, 40, 130))
        self.Piano_Button_above_1.setText("")
        self.Piano_Button_above_1.setObjectName("Piano_Button_above_1")
        self.Piano_Button_above_3 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_above_3.setGeometry(QtCore.QRect(190, 30, 40, 130))
        self.Piano_Button_above_3.setText("")
        self.Piano_Button_above_3.setObjectName("Piano_Button_above_3")
        self.Piano_Button_1 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_1.setGeometry(QtCore.QRect(10, 70, 50, 130))
        self.Piano_Button_1.setText("")
        self.Piano_Button_1.setObjectName("Piano_Button_1")
        self.Piano_Button_2 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_2.setGeometry(QtCore.QRect(60, 70, 50, 130))
        self.Piano_Button_2.setText("")
        self.Piano_Button_2.setObjectName("Piano_Button_2")
        self.Piano_Button_3 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_3.setGeometry(QtCore.QRect(110, 70, 50, 130))
        self.Piano_Button_3.setText("")
        self.Piano_Button_3.setObjectName("Piano_Button_3")
        self.Piano_Button_5 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_5.setGeometry(QtCore.QRect(210, 70, 50, 130))
        self.Piano_Button_5.setText("")
        self.Piano_Button_5.setObjectName("Piano_Button_5")
        self.Piano_Button_above_2 = QtWidgets.QPushButton(self.frameForPiano)
        self.Piano_Button_above_2.setGeometry(QtCore.QRect(90, 30, 40, 130))
        self.Piano_Button_above_2.setText("")
        self.Piano_Button_above_2.setObjectName("Piano_Button_above_2")
        self.backGroundForPiano.raise_()
        self.Piano_Button_6.raise_()
        self.Piano_Button_4.raise_()
        self.Piano_Button_7.raise_()
        self.Piano_Button_1.raise_()
        self.Piano_Button_2.raise_()
        self.Piano_Button_3.raise_()
        self.Piano_Button_5.raise_()
        self.Piano_Button_above_4.raise_()
        self.Piano_Button_above_5.raise_()
        self.Piano_Button_above_1.raise_()
        self.Piano_Button_above_2.raise_()
        self.Piano_Button_above_3.raise_()
        self.backGroundForSubPiano.raise_()
        self.Guitar_widget = QtWidgets.QWidget(self.musicTab)
        self.Guitar_widget.setGeometry(QtCore.QRect(50, 300, 951, 501))
        self.Guitar_widget.setObjectName("Guitar_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Guitar_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Guitar_Picture = QtWidgets.QLabel(self.Guitar_widget)
        self.Guitar_Picture.setStyleSheet("image: url(:/newPrefix/Guitar.png);")
        self.Guitar_Picture.setText("")
        self.Guitar_Picture.setObjectName("Guitar_Picture")
        self.gridLayout_4.addWidget(self.Guitar_Picture, 0, 0, 1, 1)
        self.Guitar_button_4 = QtWidgets.QPushButton(self.Guitar_widget)
        self.Guitar_button_4.setGeometry(QtCore.QRect(240, 280, 16, 16))
        self.Guitar_button_4.setText("")
        self.Guitar_button_4.setObjectName("Guitar_button_4")
        self.Guitar_button_1 = QtWidgets.QPushButton(self.Guitar_widget)
        self.Guitar_button_1.setGeometry(QtCore.QRect(180, 250, 16, 16))
        self.Guitar_button_1.setText("")
        self.Guitar_button_1.setObjectName("Guitar_button_1")
        self.Guitar_button_2 = QtWidgets.QPushButton(self.Guitar_widget)
        self.Guitar_button_2.setGeometry(QtCore.QRect(200, 260, 16, 16))
        self.Guitar_button_2.setText("")
        self.Guitar_button_2.setObjectName("Guitar_button_2")
        self.Guitar_button_3 = QtWidgets.QPushButton(self.Guitar_widget)
        self.Guitar_button_3.setGeometry(QtCore.QRect(220, 270, 16, 16))
        self.Guitar_button_3.setText("")
        self.Guitar_button_3.setObjectName("Guitar_button_3")
        self.Guitar_button_5 = QtWidgets.QPushButton(self.Guitar_widget)
        self.Guitar_button_5.setGeometry(QtCore.QRect(260, 290, 16, 16))
        self.Guitar_button_5.setText("")
        self.Guitar_button_5.setObjectName("Guitar_button_5")
        self.Guitar_button_5.raise_()
        self.Guitar_Picture.raise_()
        self.Guitar_button_4.raise_()
        self.Guitar_button_1.raise_()
        self.Guitar_button_2.raise_()
        self.Guitar_button_3.raise_()
        self.DrumbButton = QtWidgets.QPushButton(self.musicTab)
        self.DrumbButton.setGeometry(QtCore.QRect(710, 110, 111, 111))
        self.DrumbButton.setStyleSheet("#DrumbButton {\n"
"    \n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 50px;\n"
"border-style: outset;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 5px;\n"
"}\n"
"\n"
"#DrumbButton:hover {\n"
"background:qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"#DrumbButton:pushed\n"
"{\n"
"background:qradialgradient(\n"
"cx: 0.8, cy: -0.9, fx: 0.3, fy: -0.5,\n"
"radius: 1.5, stop: 1 #000, stop: 2 #aaa\n"
");\n"
"}\n"
"")
        self.DrumbButton.setText("")
        self.DrumbButton.setObjectName("DrumbButton")
        self.comboBox_for_tunes = QtWidgets.QComboBox(self.musicTab)
        self.comboBox_for_tunes.setGeometry(QtCore.QRect(620, 250, 231, 20))
        self.comboBox_for_tunes.setObjectName("comboBox_for_tunes")
        self.comboBox_for_tunes.addItem("")
        self.comboBox_for_tunes.addItem("")
        self.comboBox_for_tunes.addItem("")
        self.label_for_drumb_picture = QtWidgets.QLabel(self.musicTab)
        self.label_for_drumb_picture.setGeometry(QtCore.QRect(450, 80, 251, 161))
        self.label_for_drumb_picture.setStyleSheet("image: url(:/newPrefix/drumb.png);")
        self.label_for_drumb_picture.setText("")
        self.label_for_drumb_picture.setObjectName("label_for_drumb_picture")
        self.DrumbButton.raise_()
        self.frameForPiano.raise_()
        self.Guitar_widget.raise_()
        self.comboBox_for_tunes.raise_()
        self.label_for_drumb_picture.raise_()
        self.tabWidgets.addTab(self.musicTab, "")
        self.equilizerTab = QtWidgets.QWidget()
        self.equilizerTab.setObjectName("equilizerTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.equilizerTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout_For_spectrogram = QtWidgets.QVBoxLayout()
        self.verticalLayout_For_spectrogram.setObjectName("verticalLayout_For_spectrogram")
        self.gridLayout_3.addLayout(self.verticalLayout_For_spectrogram, 0, 2, 1, 1)
        self.verticalLayout_For_signal = QtWidgets.QVBoxLayout()
        self.verticalLayout_For_signal.setObjectName("verticalLayout_For_signal")
        self.gridLayout_3.addLayout(self.verticalLayout_For_signal, 0, 0, 1, 2)
        self.horizontalLayout_For_Feautures = QtWidgets.QHBoxLayout()
        self.horizontalLayout_For_Feautures.setObjectName("horizontalLayout_For_Feautures")
        self.verticalLayout_For_Buttons = QtWidgets.QVBoxLayout()
        self.verticalLayout_For_Buttons.setObjectName("verticalLayout_For_Buttons")
        self.pushButton_Open = QtWidgets.QPushButton(self.equilizerTab)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.verticalLayout_For_Buttons.addWidget(self.pushButton_Open)
        self.pushButton_Play = QtWidgets.QPushButton(self.equilizerTab)
        self.pushButton_Play.setObjectName("pushButton_Play")
        self.verticalLayout_For_Buttons.addWidget(self.pushButton_Play)
        self.pushButton_pause = QtWidgets.QPushButton(self.equilizerTab)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.verticalLayout_For_Buttons.addWidget(self.pushButton_pause)
        self.Apply_3 = QtWidgets.QPushButton(self.equilizerTab)
        self.Apply_3.setObjectName("Apply_3")
        self.verticalLayout_For_Buttons.addWidget(self.Apply_3)
        self.pushButton_For_Spare = QtWidgets.QPushButton(self.equilizerTab)
        self.pushButton_For_Spare.setObjectName("pushButton_For_Spare")
        self.verticalLayout_For_Buttons.addWidget(self.pushButton_For_Spare)
        self.horizontalLayout_For_Feautures.addLayout(self.verticalLayout_For_Buttons)
        self.verticalSlider_For_volume = QtWidgets.QSlider(self.equilizerTab)
        self.verticalSlider_For_volume.setMinimum(1)
        self.verticalSlider_For_volume.setMaximum(10)
        self.verticalSlider_For_volume.setProperty("value", 10)
        self.verticalSlider_For_volume.setSliderPosition(10)
        self.verticalSlider_For_volume.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_For_volume.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_For_volume.setTickInterval(1)
        self.verticalSlider_For_volume.setObjectName("verticalSlider_For_volume")
        self.horizontalLayout_For_Feautures.addWidget(self.verticalSlider_For_volume, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_For_equilizing = QtWidgets.QVBoxLayout()
        self.verticalLayout_For_equilizing.setObjectName("verticalLayout_For_equilizing")
        self.widget_For_pictures = QtWidgets.QWidget(self.equilizerTab)
        self.widget_For_pictures.setObjectName("widget_For_pictures")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_For_pictures)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Guitar_Picture_4 = QtWidgets.QLabel(self.widget_For_pictures)
        self.Guitar_Picture_4.setStyleSheet("\n"
"image: url(:/newPrefix/piano2.png);")
        self.Guitar_Picture_4.setText("")
        self.Guitar_Picture_4.setObjectName("Guitar_Picture_4")
        self.gridLayout_5.addWidget(self.Guitar_Picture_4, 0, 0, 1, 1)
        self.Guitar_Picture_2 = QtWidgets.QLabel(self.widget_For_pictures)
        self.Guitar_Picture_2.setStyleSheet("image: url(:/newPrefix/Guitar.png);")
        self.Guitar_Picture_2.setText("")
        self.Guitar_Picture_2.setObjectName("Guitar_Picture_2")
        self.gridLayout_5.addWidget(self.Guitar_Picture_2, 0, 1, 1, 1)
        self.Guitar_Picture_5 = QtWidgets.QLabel(self.widget_For_pictures)
        self.Guitar_Picture_5.setStyleSheet("image: url(:/newPrefix/drumb.png);\n"
"")
        self.Guitar_Picture_5.setText("")
        self.Guitar_Picture_5.setObjectName("Guitar_Picture_5")
        self.gridLayout_5.addWidget(self.Guitar_Picture_5, 0, 2, 1, 1)
        self.verticalLayout_For_equilizing.addWidget(self.widget_For_pictures)
        self.horizontalLayout_For_equillizing = QtWidgets.QHBoxLayout()
        self.horizontalLayout_For_equillizing.setObjectName("horizontalLayout_For_equillizing")
        self.horizontalSlider_For_piano = QtWidgets.QSlider(self.equilizerTab)
        self.horizontalSlider_For_piano.setMaximum(10)
        self.horizontalSlider_For_piano.setProperty("value", 1)
        self.horizontalSlider_For_piano.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_For_piano.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_For_piano.setObjectName("horizontalSlider_For_piano")
        self.horizontalLayout_For_equillizing.addWidget(self.horizontalSlider_For_piano)
        self.horizontalSlider_For_Guitar = QtWidgets.QSlider(self.equilizerTab)
        self.horizontalSlider_For_Guitar.setMaximum(10)
        self.horizontalSlider_For_Guitar.setProperty("value", 1)
        self.horizontalSlider_For_Guitar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_For_Guitar.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_For_Guitar.setObjectName("horizontalSlider_For_Guitar")
        self.horizontalLayout_For_equillizing.addWidget(self.horizontalSlider_For_Guitar)
        self.horizontalSlider_For_Drumb = QtWidgets.QSlider(self.equilizerTab)
        self.horizontalSlider_For_Drumb.setMaximum(10)
        self.horizontalSlider_For_Drumb.setProperty("value", 1)
        self.horizontalSlider_For_Drumb.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_For_Drumb.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_For_Drumb.setObjectName("horizontalSlider_For_Drumb")
        self.horizontalLayout_For_equillizing.addWidget(self.horizontalSlider_For_Drumb)
        self.verticalLayout_For_equilizing.addLayout(self.horizontalLayout_For_equillizing)
        self.horizontalLayout_For_Feautures.addLayout(self.verticalLayout_For_equilizing)
        self.gridLayout_3.addLayout(self.horizontalLayout_For_Feautures, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        self.tabWidgets.addTab(self.equilizerTab, "")
        self.verticalLayout.addWidget(self.tabWidgets)

        self.retranslateUi(Piano_istrument)
        self.tabWidgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Piano_istrument)

        self.device = 0
        self.window_length = 200
        self.downsample = 10
        self.channels = [1]
        self.interval = 30
        self.threadpool = QtCore.QThreadPool()
        self.reference_plot = None
        self.q = queue.Queue(maxsize=20)
        self.stop = False

        #device_info = sd.query_devices(self.device, 'input')
        device_info = sd.query_devices(self.device)
        self.samplerate = device_info['default_samplerate']
        length = int(self.window_length*self.samplerate/(1000*self.downsample))
        sd.default.samplerate = self.samplerate

        self.plotdata = np.zeros((length, len(self.channels)))

        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)  # msec
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.pushButton_Open.clicked.connect(self.open_audio_file)
        self.canvas = MplCanvas(self, width=5, height=4,dpi=100)
        self.verticalLayout_For_signal.addWidget(self.canvas,2) ##grid
        self.horizontalSlider_For_Guitar.setSliderPosition(1)
        self.horizontalSlider_For_Drumb.setSliderPosition(1)
        self.horizontalSlider_For_piano.setSliderPosition(1)

        self.Piano_Button_1.clicked.connect(self.pb1)
        self.Piano_Button_2.clicked.connect(self.pb2)
        self.Piano_Button_3.clicked.connect(self.pb3)
        self.Piano_Button_4.clicked.connect(self.pb4)
        self.Piano_Button_5.clicked.connect(self.pb5)
        self.Piano_Button_6.clicked.connect(self.pb6)
        self.Piano_Button_7.clicked.connect(self.pb7)
        self.Piano_Button_above_1.clicked.connect(self.pb8)
        self.Piano_Button_above_2.clicked.connect(self.pb9)
        self.Piano_Button_above_3.clicked.connect(self.pb10)
        self.Piano_Button_above_4.clicked.connect(self.pb11)
        self.Piano_Button_above_5.clicked.connect(self.pb12)
        self.DrumbButton.clicked.connect(self.pb0)
        self.Guitar_button_1.clicked.connect(self.g1)
        self.Guitar_button_2.clicked.connect(self.g2)
        self.Guitar_button_3.clicked.connect(self.g3)
        self.Guitar_button_4.clicked.connect(self.g4)
        self.Guitar_button_5.clicked.connect(self.g5)

        self.pushButton_pause.clicked.connect(self.stop_media)
        self.pushButton_Play.clicked.connect(self.play_media)
        self.verticalSlider_For_volume.valueChanged.connect(self.Volume_Control)

        self.canvasSpec = MplCanvas_Spec(self.verticalLayout_For_spectrogram)
        self.horizontalSlider_For_Guitar.setSliderPosition(1)
        self.horizontalSlider_For_Drumb.setSliderPosition(1)
        self.horizontalSlider_For_piano.setSliderPosition(1)

        self.signal_viewer_widget = pg.PlotWidget()
        pen = pg.mkPen(color=(0, 0, 255))
        self.graph = self.signal_viewer_widget.plot([], [], pen=pen)
        self.Apply_3.clicked.connect(self.equalize)

    def retranslateUi(self, Piano_istrument):
        _translate = QtCore.QCoreApplication.translate
        Piano_istrument.setWindowTitle(_translate("Piano_istrument", "Form"))
        self.tabWidgets.setWhatsThis(_translate("Piano_istrument", "<html><head/><body><p>musicTab</p></body></html>"))
        self.comboBox_for_tunes.setItemText(0, _translate("Piano_istrument", "octave"))
        self.comboBox_for_tunes.setItemText(1, _translate("Piano_istrument", "solo"))
        self.comboBox_for_tunes.setItemText(2, _translate("Piano_istrument", "spare"))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.musicTab), _translate("Piano_istrument", "musicTab"))
        self.pushButton_Open.setText(_translate("Piano_istrument", "Open"))
        self.pushButton_Play.setText(_translate("Piano_istrument", "Play"))
        self.pushButton_pause.setText(_translate("Piano_istrument", "Pause"))
        self.Apply_3.setText(_translate("Piano_istrument", "Apply"))
        self.pushButton_For_Spare.setText(_translate("Piano_istrument", "Spare"))
        self.tabWidgets.setTabText(self.tabWidgets.indexOf(self.equilizerTab), _translate("Piano_istrument", "equilizerTab"))

    def equalize(self):
        # [bass , piano--- , altoSaxophone--- , guitar--- , flute, bell]
        freq_min = [90, 1000, 2000]
        freq_max = [180,2000, 15000]

        Gains = []
        Gains.append(self.horizontalSlider_For_Drumb.value())
        Gains.append(self.horizontalSlider_For_piano.value())
        Gains.append(self.horizontalSlider_For_Guitar.value())

        self.fs, self.data = wavfile.read(self.full_file_path)
        self.data = self.data / 2.0 ** 15
        N = len(self.data)

        rfft_coeff = np.fft.rfft(self.data)
        frequencies = np.fft.rfftfreq(N, 1. / self.fs)

        for i in range(3):
            for j in range(len(frequencies)):
                if frequencies[j] >= freq_min[i] and frequencies[j] <= freq_max[i]:
                    rfft_coeff[j] = rfft_coeff[j] * Gains[i]

        Equalized_signal = np.fft.irfft(rfft_coeff)

        wavfile.write('Equalized.wav', self.fs, Equalized_signal)
        self.media.stop()
        self.playAudioFile('Equalized.wav')
        logging.info('Equalizer initiated')

    def open_audio_file(self):
        self.full_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open Song', QtCore.QDir.rootPath(), 'wav(*.wav)')
        self.playAudioFile(self.full_file_path)
        logging.info('Opened Wav file')


    def playAudioFile(self, full_file_path):
        self.media = vlc.MediaPlayer(full_file_path)
        self.media.play()
        self.fs, self.data = wavfile.read(full_file_path)

######## Start Spec
        self.verticalLayout_For_spectrogram.addWidget(self.canvasSpec)
        self.canvasSpec.axes.cla()
        spec = self.canvasSpec.axes
        self.spec_Fig = spec.specgram(self.data, self.fs)
        logging.info('Spectrogram appeared')
######## End Spec

        worker = Worker(self.start_stream,)
        self.threadpool.start(worker)

    def start_stream(self):
        try:
            def audio_callback(indata, frames, time, status):
                self.q.put(indata[::self.downsample, [0]])
            stream = sd.InputStream(device=self.device, channels=max(
                self.channels), samplerate=self.samplerate, callback=audio_callback)
            with stream:
                input()
        except Exception as e:
            print("ERROR: ", e)
        logging.info('Live Ploter Initialized')


    def update_plot(self):
        try:
            data = [0]

            while True:
                try:
                    data = self.q.get_nowait()
                except queue.Empty:
                    break
                shift = len(data)
                self.plotdata = np.roll(self.plotdata, -shift, axis=0)
                self.plotdata[-shift:, :] = data
                self.ydata = self.plotdata[:]
                self.canvas.axes.set_facecolor((0, 0, 0))

                if self.reference_plot is None:
                    plot_refs = self.canvas.axes.plot(
                        self.ydata, color=(0, 1, 0.29))
                    self.reference_plot = plot_refs[0]
                else:
                    self.reference_plot.set_ydata(self.ydata)

            self.canvas.axes.yaxis.grid(True, linestyle='--')
            start, end = self.canvas.axes.get_ylim()
            self.canvas.axes.yaxis.set_ticks(np.arange(start, end, 0.1))
            self.canvas.axes.yaxis.set_major_formatter(
                ticker.FormatStrFormatter('%0.1f'))
            self.canvas.axes.set_ylim(ymin=-0.5, ymax=0.5)
            if self.stop == False:
                self.canvas.draw()
        except:
            pass


    def pb0(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Drumb/Octave/Bass-Drum-1.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Drumb/Solo/E-Mu-Proteus-FX-Wacky-Snare.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Drumb/Spare/Bamboo.wav')
            pygame.mixer.music.play()
    def pb1(self):
        if self.comboBox_for_tunes.currentIndex() == 0:
            pygame.mixer.music.load('instruments/Piano/Octave/A.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/1.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/1.wav')
            pygame.mixer.music.play()
    def pb2(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/e.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/2.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/2.wav')
            pygame.mixer.music.play()
    def pb3(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/f#.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/3.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/3.wav')
            pygame.mixer.music.play()
    def pb4(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/f.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/4.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/4.wav')
            pygame.mixer.music.play()
    def pb5(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g#.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/5.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/5.wav')
            pygame.mixer.music.play()
    def pb6(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/6.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/6.wav')
            pygame.mixer.music.play()
    def pb7(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g1.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/7.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/7.wav')
            pygame.mixer.music.play()
    def pb8(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g2.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/8.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/8.wav')
            pygame.mixer.music.play()
    def pb9(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g3.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/9.wav') ##unknow wave data format
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/9.wav')
            pygame.mixer.music.play()
    def pb10(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g4.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/10.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/10.wav')
            pygame.mixer.music.play()
    def pb11(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/g5.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex() == 1:
            pygame.mixer.music.load('instruments/Piano/Solo/11.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Piano/Spare/11.wav')
            pygame.mixer.music.play()
    def pb12(self):
         if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Piano/Octave/a#.wav')
            pygame.mixer.music.play()
         elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Piano/Solo/12.wav')
            pygame.mixer.music.play()
         else:
            pygame.mixer.music.load('instruments/Piano/Spare/12.wav')
            pygame.mixer.music.play()

    def g1(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/GTR1.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/1.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/1.wav')
            pygame.mixer.music.play()

    def g2(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanchord-B-02.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/5.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/2.wav')
            pygame.mixer.music.play()

    def g3(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-B02-slap.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/2.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/3.wav')
            pygame.mixer.music.play()
    def g4(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-E01-slap.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/3.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/4.wav')
            pygame.mixer.music.play()
    def g5(self):
        if self.comboBox_for_tunes.currentIndex()==0:
            pygame.mixer.music.load('instruments/Guitar/Octave/chord-G.wav')
            pygame.mixer.music.play()
        elif self.comboBox_for_tunes.currentIndex()==1:
            pygame.mixer.music.load('instruments/Guitar/Solo/4.wav')
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load('instruments/Guitar/Spare/5.wav')
            pygame.mixer.music.play()
    

    def Volume_Control(self):
        value = int(self.verticalSlider_For_volume.value())
        self.media.audio_set_volume(value*10)
        logging.info('volume changed')


    def stop_media(self):
        self.media.pause()
        logging.info('media paused')
         
    def play_media(self):
        self.media.play()
        logging.info('media played')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Piano_istrument = QtWidgets.QWidget()
    ui = Ui_Piano_istrument()
    ui.setupUi(Piano_istrument)
    Piano_istrument.show()
    sys.exit(app.exec_())
