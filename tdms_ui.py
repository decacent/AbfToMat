# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tdms_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Read_Tdms(object):
    def setupUi(self, Read_Tdms):
        Read_Tdms.setObjectName("Read_Tdms")
        Read_Tdms.resize(714, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/ui.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Read_Tdms.setWindowIcon(icon)
        Read_Tdms.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Read_Tdms)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_tdms = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tdms.setObjectName("horizontalLayout_tdms")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem)
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setMinimumSize(QtCore.QSize(70, 70))
        self.openfile.setMaximumSize(QtCore.QSize(70, 70))
        self.openfile.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img18.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img17.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.openfile.setText("")
        self.openfile.setObjectName("openfile")
        self.horizontalLayout_tdms.addWidget(self.openfile)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem1)
        self.plotdata = QtWidgets.QPushButton(self.centralwidget)
        self.plotdata.setMinimumSize(QtCore.QSize(70, 70))
        self.plotdata.setMaximumSize(QtCore.QSize(70, 70))
        self.plotdata.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img43.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img43s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.plotdata.setText("")
        self.plotdata.setObjectName("plotdata")
        self.horizontalLayout_tdms.addWidget(self.plotdata)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem2)
        self.savedata = QtWidgets.QPushButton(self.centralwidget)
        self.savedata.setMinimumSize(QtCore.QSize(70, 70))
        self.savedata.setMaximumSize(QtCore.QSize(70, 70))
        self.savedata.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img45.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img45s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}url(:/img/img45s.ico)")
        self.savedata.setText("")
        self.savedata.setObjectName("savedata")
        self.horizontalLayout_tdms.addWidget(self.savedata)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem3)
        self.checkBox_5_tdms = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5_tdms.setMinimumSize(QtCore.QSize(70, 25))
        self.checkBox_5_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.checkBox_5_tdms.setObjectName("checkBox_5_tdms")
        self.horizontalLayout_tdms.addWidget(self.checkBox_5_tdms)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_tdms.addWidget(self.label)
        self.doubleSpinBox_8_tdms = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_8_tdms.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_8_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_8_tdms.setMaximum(1e+23)
        self.doubleSpinBox_8_tdms.setDecimals(4)
        self.doubleSpinBox_8_tdms.setObjectName("doubleSpinBox_8_tdms")
        self.horizontalLayout_tdms.addWidget(self.doubleSpinBox_8_tdms)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_tdms.addWidget(self.label_2)
        self.doubleSpinBox_9_tdms = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_9_tdms.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_9_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_9_tdms.setMaximum(1e+20)
        self.doubleSpinBox_9_tdms.setDecimals(4)
        self.doubleSpinBox_9_tdms.setObjectName("doubleSpinBox_9_tdms")
        self.horizontalLayout_tdms.addWidget(self.doubleSpinBox_9_tdms)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tdms.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_tdms)
        self.verticalLayout_tdms = QtWidgets.QVBoxLayout()
        self.verticalLayout_tdms.setObjectName("verticalLayout_tdms")
        self.verticalLayout_2.addLayout(self.verticalLayout_tdms)
        Read_Tdms.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Read_Tdms)
        self.statusbar.setObjectName("statusbar")
        Read_Tdms.setStatusBar(self.statusbar)

        self.retranslateUi(Read_Tdms)
        QtCore.QMetaObject.connectSlotsByName(Read_Tdms)

    def retranslateUi(self, Read_Tdms):
        _translate = QtCore.QCoreApplication.translate
        Read_Tdms.setWindowTitle(_translate("Read_Tdms", "AbfToMat"))
        self.checkBox_5_tdms.setText(_translate("Read_Tdms", "选择数据"))
        self.label.setText(_translate("Read_Tdms", "起始时间"))
        self.label_2.setText(_translate("Read_Tdms", "终止时间"))

import images
