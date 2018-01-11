# -*- coding: utf-8 -*-
"""


@author: Wnight
"""
import sys
import scipy.io as sio
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox,QApplication
import numpy as np
from tdms_ui import *

import matplotlib as mpl
mpl.use('Qt5Agg')
mpl.rcParams['agg.path.chunksize'] = 10000
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import gc
from axonio import Abf_io



def abf_to_mat(fn):
    pass

class Tdms_read(QMainWindow, Ui_Read_Tdms):
    def __init__(self, parent=None):
        super(Tdms_read, self).__init__(parent)
        self.setupUi(self)

        self.data=None

        self.figure_tdms = plt.figure(5)
        self.ax_tdms = self.figure_tdms.add_subplot(111)
        self.figure_tdms.subplots_adjust(left=0.1, right=0.9)
        self.canvas_tdms = FigureCanvas(self.figure_tdms)
        self.toolbar_tdms = NavigationToolbar(self.canvas_tdms, self)
        self.verticalLayout_tdms.addWidget(self.toolbar_tdms)
        self.verticalLayout_tdms.addWidget(self.canvas_tdms)
        self.tdms_is_view = False
        #self.axs_tdms = self.ax_tdms.twinx()

        self.openfile.clicked.connect(self.loadtdms)
        self.plotdata.clicked.connect(self.plottdms)
        self.savedata.clicked.connect(self.savetdms)
        self.tdms_span = SpanSelector(self.ax_tdms, self.tdms_onselect, 'horizontal', useblit=True, button=3,
                                      rectprops=dict(alpha=0.3, facecolor='g'))


    def tdms_onselect(self,xmin, xmax):
        if self.tdms_is_view:
            self.checkBox_5_tdms.setChecked(True)
            self.doubleSpinBox_8_tdms.setValue(xmin)
            self.doubleSpinBox_9_tdms.setValue(xmax)
            #self.plottdms()

    def loadtdms(self):
        self.statusBar().showMessage("打开abf文件")
        self.fn = QFileDialog.getOpenFileName(filter='Abf Files (*.abf)')[0]
        if self.fn == '':
            self.statusBar().showMessage("未选择文件")
            pass
        else:
            self.statusBar().showMessage("正在读取ABF数据..")
            try:
                f = Abf_io(self.fn)
                print(f)
                self.data, self.sam, self.sweeps = f.read_abf()
                self.time = np.arange(0, len(self.data[0]) / self.sam, 1 / self.sam)
                self.time = self.time[0:len(self.data[0])]
                self.data=self.data[0][:, 0]
                self.is_read = True
                self.statusBar().showMessage('ABF数据读取完成..' + os.path.basename(self.fn[0]))
                QMessageBox.information(self, "标题", "数据读取完成", QMessageBox.Ok)
                # self.label_6.setText('1/%d' % (self.sweeps))
                # self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                # self.label_sample_rate.setText('%dk' % (self.sam / 1000))
                # self.label_sample_rate.setAlignment(QtCore.Qt.AlignCenter)
            except:
                #self.statusBar().showMessage('文件读取错误')
                QMessageBox.information(self, "标题", "文件错误，Abf版本<2.0 ", QMessageBox.Ok)

            try:
                self.channel = self.data[0].shape[1]
            except:
                self.channel = 0

    def plottdms(self):
        if self.data is None:
            self.statusBar().showMessage('无Tdms数据')
            QMessageBox.information(self, "标题", "无Abf数据", QMessageBox.Ok)
        else:
            if self.checkBox_5_tdms.isChecked():
                self.start = int(self.doubleSpinBox_8_tdms.value() * self.sam)
                self.end = int(self.doubleSpinBox_9_tdms.value() * self.sam)
                if self.start >= self.end:
                    QMessageBox.information(self, "标题", "请正确设置时间范围", QMessageBox.Ok)
                    pass
                else:
                    self.ax_tdms.cla()
                    #self.axs_tdms.cla()
                    gc.collect()
                    self.ax_tdms.plot(self.time[self.start:self.end], self.data[self.start:self.end], 'k')
                    self.ax_tdms.set_xlabel('Time/s')
                    self.ax_tdms.set_ylabel('Current/nA')
                    self.canvas_tdms.draw()
                    self.statusBar().showMessage('绘制Abf')
                    self.tdms_is_view = True
            else:
                self.ax_tdms.cla()
                #self.axs_tdms.cla()
                self.ax_tdms.plot(self.time, self.data[:], 'k')
                self.ax_tdms.set_xlabel('Time/s')
                self.ax_tdms.set_ylabel('Current/pA')
                self.canvas_tdms.draw()
                self.statusBar().showMessage('绘制Abf')
                self.tdms_is_view=True

    def savetdms(self):
        if self.data is None:
            self.statusBar().showMessage('无Abf数据')
            QMessageBox.information(self, "标题", "无Abf数据", QMessageBox.Ok)
            return None
        file_choices = "mat (*.mat)"
        path = QFileDialog.getSaveFileName(self, 'Save file', '', file_choices)
        if path:
            if self.checkBox_5_tdms.isChecked():
                self.start = int(self.doubleSpinBox_8_tdms.value() * self.sam)
                self.end = int(self.doubleSpinBox_9_tdms.value() * self.sam)
                if self.start >= self.end:
                    QMessageBox.information(self, "标题", "请正确设置时间范围", QMessageBox.Ok)
                    return  None
                else:

                    self.part_tdms=np.array((self.time[self.start:self.end],self.data[self.start:self.end]))

                    sio.savemat(path[0], {'f': self.part_tdms.T})

                    self.statusBar().showMessage('Saved to %s' % path[0])
                    self.statusBar().showMessage('数据保存完成')
                    QMessageBox.information(self, "标题", "数据保存完成", QMessageBox.Ok)

            else:
                sio.savemat(path[0], {'f':  np.array((self.time,self.data)).T})
                self.statusBar().showMessage('Saved to %s' % path[0])
                self.statusBar().showMessage('数据保存完成')
                QMessageBox.information(self, "标题", "数据保存完成", QMessageBox.Ok)


        else:
            self.statusBar().showMessage('请选择保存文件位置')
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Tdms_read()
    mainWindow.show()
    sys.exit(app.exec_())