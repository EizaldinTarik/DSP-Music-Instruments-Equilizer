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
from Tones import *
from GUI import Ui_Piano_istrument

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

class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self) :
        super(ApplicationWindow,self).__init__()
        self.ui = Ui_Piano_istrument()
        self.ui.setupUi(self)
        self.device = 0
        self.window_length = 200
        self.downsample = 10
        self.channels = [1]
        self.interval = 30
        self.threadpool = QtCore.QThreadPool()
        self.reference_plot = None
        self.q = queue.Queue(maxsize=20)
        self.stop = False

        #device_info = sd.query_devices(self.ui.device, 'input')
        device_info = sd.query_devices(self.device)
        print(device_info)
        self.samplerate = device_info['default_samplerate']
        length = int(self.window_length*self.samplerate/(1000*self.downsample))
        sd.default.samplerate = self.samplerate

        self.plotdata = np.zeros((length, len(self.channels)))

        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)  # msec
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.ui.pushButton_Open.clicked.connect(self.open_audio_file)
        self.canvas = MplCanvas(self.ui, width=5, height=4,dpi=100)
        self.ui.verticalLayout_For_signal.addWidget(self.canvas,2) ##grid
        self.ui.horizontalSlider_For_Guitar.setSliderPosition(1)
        self.ui.horizontalSlider_For_Drumb.setSliderPosition(1)
        self.ui.horizontalSlider_For_piano.setSliderPosition(1)

        # self.ui.Piano_Button_1.clicked.connect(self.ui.pb1)
        # self.ui.Piano_Button_2.clicked.connect(self.ui.pb2)
        # self.ui.Piano_Button_3.clicked.connect(self.ui.pb3)
        # self.ui.Piano_Button_4.clicked.connect(self.ui.pb4)
        # self.ui.Piano_Button_5.clicked.connect(self.ui.pb5)
        # self.ui.Piano_Button_6.clicked.connect(self.ui.pb6)
        # self.ui.Piano_Button_7.clicked.connect(self.ui.pb7)
        # self.ui.Piano_Button_above_1.clicked.connect(self.ui.pb8)
        # self.ui.Piano_Button_above_2.clicked.connect(self.ui.pb9)
        # self.ui.Piano_Button_above_3.clicked.connect(self.ui.pb10)
        # self.ui.Piano_Button_above_4.clicked.connect(self.ui.pb11)
        # self.ui.Piano_Button_above_5.clicked.connect(self.ui.pb12)
        # self.ui.DrumbButton.clicked.connect(self.ui.pb0)
        # self.ui.Guitar_button_1.clicked.connect(self.ui.g1)
        # self.ui.Guitar_button_2.clicked.connect(self.ui.g2)
        # self.ui.Guitar_button_3.clicked.connect(self.ui.g3)
        # self.ui.Guitar_button_4.clicked.connect(self.ui.g4)
        # self.ui.Guitar_button_5.clicked.connect(self.ui.g5)

        self.ui.pushButton_pause.clicked.connect(self.stop_media)
        self.ui.pushButton_Play.clicked.connect(self.play_media)
        self.ui.verticalSlider_For_volume.valueChanged.connect(self.Volume_Control)

        self.canvasSpec = MplCanvas_Spec(self.ui.verticalLayout_For_spectrogram)
        self.ui.horizontalSlider_For_Guitar.setSliderPosition(1)
        self.ui.horizontalSlider_For_Drumb.setSliderPosition(1)
        self.ui.horizontalSlider_For_piano.setSliderPosition(1)

        self.signal_viewer_widget = pg.PlotWidget()
        pen = pg.mkPen(color=(0, 0, 255))
        self.graph = self.signal_viewer_widget.plot([], [], pen=pen)
        self.ui.Apply_3.clicked.connect(self.equalize)

    def equalize(self):
        # [bass , piano--- , altoSaxophone--- , guitar--- , flute, bell]
        freq_min = [90, 1000, 2000]
        freq_max = [180,2000, 15000]

        Gains = []
        Gains.append(self.ui.horizontalSlider_For_Drumb.value())
        Gains.append(self.ui.horizontalSlider_For_piano.value())
        Gains.append(self.ui.horizontalSlider_For_Guitar.value())

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
        self.ui.verticalLayout_For_spectrogram.addWidget(self.canvasSpec)
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


    # def pb0(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Drumb/Octave/Bass-Drum-1.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Drumb/Solo/E-Mu-Proteus-FX-Wacky-Snare.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Drumb/Spare/Bamboo.wav')
    #         pygame.mixer.music.play()
    # def pb1(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex() == 0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/A.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/1.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/1.wav')
    #         pygame.mixer.music.play()
    # def pb2(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/e.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/2.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/2.wav')
    #         pygame.mixer.music.play()
    # def pb3(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/f#.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/3.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/3.wav')
    #         pygame.mixer.music.play()
    # def pb4(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/f.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/4.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/4.wav')
    #         pygame.mixer.music.play()
    # def pb5(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g#.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/5.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/5.wav')
    #         pygame.mixer.music.play()
    # def pb6(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/6.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/6.wav')
    #         pygame.mixer.music.play()
    # def pb7(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g1.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/7.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/7.wav')
    #         pygame.mixer.music.play()
    # def pb8(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g2.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/8.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/8.wav')
    #         pygame.mixer.music.play()
    # def pb9(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g3.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/9.wav') ##unknow wave data format
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/9.wav')
    #         pygame.mixer.music.play()
    # def pb10(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g4.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/10.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/10.wav')
    #         pygame.mixer.music.play()
    # def pb11(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/g5.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex() == 1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/11.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/11.wav')
    #         pygame.mixer.music.play()
    # def pb12(self.ui):
    #      if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Piano/Octave/a#.wav')
    #         pygame.mixer.music.play()
    #      elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Piano/Solo/12.wav')
    #         pygame.mixer.music.play()
    #      else:
    #         pygame.mixer.music.load('instruments/Piano/Spare/12.wav')
    #         pygame.mixer.music.play()

    # def g1(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Guitar/Octave/GTR1.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Guitar/Solo/1.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Guitar/Spare/1.wav')
    #         pygame.mixer.music.play()

    # def g2(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Guitar/Octave/cleanchord-B-02.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Guitar/Solo/5.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Guitar/Spare/2.wav')
    #         pygame.mixer.music.play()

    # def g3(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-B02-slap.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Guitar/Solo/2.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Guitar/Spare/3.wav')
    #         pygame.mixer.music.play()
    # def g4(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Guitar/Octave/cleanmidbass-E01-slap.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Guitar/Solo/3.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Guitar/Spare/4.wav')
    #         pygame.mixer.music.play()
    # def g5(self.ui):
    #     if self.ui.comboBox_for_tunes.currentIndex()==0:
    #         pygame.mixer.music.load('instruments/Guitar/Octave/chord-G.wav')
    #         pygame.mixer.music.play()
    #     elif self.ui.comboBox_for_tunes.currentIndex()==1:
    #         pygame.mixer.music.load('instruments/Guitar/Solo/4.wav')
    #         pygame.mixer.music.play()
    #     else:
    #         pygame.mixer.music.load('instruments/Guitar/Spare/5.wav')
    #         pygame.mixer.music.play()
    

    def Volume_Control(self):
        value = int(self.ui.verticalSlider_For_volume.value())
        self.media.audio_set_volume(value*10)
        logging.info('volume changed')


    def stop_media(self):
        self.media.pause()
        logging.info('media paused')
         
    def play_media(self):
        self.media.play()
        logging.info('media played')


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__=="__main__":
    main()
