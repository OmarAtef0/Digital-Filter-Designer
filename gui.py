# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1488, 865)
        MainWindow.setStyleSheet("#centralwidget {\n"
"    background: #15242d;    \n"
"\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"    background: rgb(37, 38, 49);    \n"
"    color:white;\n"
"}\n"
"QGroupBox {\n"
"    background: #15242d;\n"
"    color:rgb(241, 241, 241);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background: white;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: rgb(0, 24, 36);\n"
"    color:rgb(241, 241, 241);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.grpbx_DigitalFilter = QtWidgets.QGroupBox(self.centralwidget)
        self.grpbx_DigitalFilter.setObjectName("grpbx_DigitalFilter")
        self.gridLayout = QtWidgets.QGridLayout(self.grpbx_DigitalFilter)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plot_magResponse = PlotWidget(self.grpbx_DigitalFilter)
        self.plot_magResponse.setMinimumSize(QtCore.QSize(200, 0))
        self.plot_magResponse.setObjectName("plot_magResponse")
        self.verticalLayout_2.addWidget(self.plot_magResponse)
        self.plot_phaseResponse = PlotWidget(self.grpbx_DigitalFilter)
        self.plot_phaseResponse.setMinimumSize(QtCore.QSize(200, 0))
        self.plot_phaseResponse.setObjectName("plot_phaseResponse")
        self.verticalLayout_2.addWidget(self.plot_phaseResponse)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.wgt_unitCircle = QtWidgets.QWidget(self.grpbx_DigitalFilter)
        self.wgt_unitCircle.setObjectName("wgt_unitCircle")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.wgt_unitCircle)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.wgt_buttons = QtWidgets.QWidget(self.wgt_unitCircle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wgt_buttons.sizePolicy().hasHeightForWidth())
        self.wgt_buttons.setSizePolicy(sizePolicy)
        self.wgt_buttons.setMaximumSize(QtCore.QSize(120, 16777215))
        self.wgt_buttons.setStyleSheet("")
        self.wgt_buttons.setObjectName("wgt_buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wgt_buttons)
        self.verticalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_addPoles = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_addPoles.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_addPoles.setObjectName("btn_addPoles")
        self.btngrp_zerosPoles = QtWidgets.QButtonGroup(MainWindow)
        self.btngrp_zerosPoles.setObjectName("btngrp_zerosPoles")
        self.btngrp_zerosPoles.addButton(self.btn_addPoles)
        self.verticalLayout_3.addWidget(self.btn_addPoles)
        self.btn_addZeros = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_addZeros.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_addZeros.setObjectName("btn_addZeros")
        self.btngrp_zerosPoles.addButton(self.btn_addZeros)
        self.verticalLayout_3.addWidget(self.btn_addZeros)
        self.btn_removePoles = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_removePoles.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_removePoles.setObjectName("btn_removePoles")
        self.btngrp_zerosPoles.addButton(self.btn_removePoles)
        self.verticalLayout_3.addWidget(self.btn_removePoles)
        self.btn_RemoveZeros = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_RemoveZeros.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_RemoveZeros.setStyleSheet("")
        self.btn_RemoveZeros.setObjectName("btn_RemoveZeros")
        self.btngrp_zerosPoles.addButton(self.btn_RemoveZeros)
        self.verticalLayout_3.addWidget(self.btn_RemoveZeros)
        self.btn_Remove = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_Remove.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_Remove.setObjectName("btn_Remove")
        self.btngrp_zerosPoles.addButton(self.btn_Remove)
        self.verticalLayout_3.addWidget(self.btn_Remove)
        self.btn_removeAll = QtWidgets.QPushButton(self.wgt_buttons)
        self.btn_removeAll.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_removeAll.setObjectName("btn_removeAll")
        self.btngrp_zerosPoles.addButton(self.btn_removeAll)
        self.verticalLayout_3.addWidget(self.btn_removeAll)
        self.pair_mode_toggle = QtWidgets.QCheckBox(self.wgt_buttons)
        self.pair_mode_toggle.setObjectName("pair_mode_toggle")
        self.verticalLayout_3.addWidget(self.pair_mode_toggle)
        self.mouse_en = QtWidgets.QCheckBox(self.wgt_buttons)
        self.mouse_en.setObjectName("mouse_en")
        self.verticalLayout_3.addWidget(self.mouse_en)
        self.gridLayout_5.addWidget(self.wgt_buttons, 0, 0, 1, 1)
        self.plot_unitCircle = PlotWidget(self.wgt_unitCircle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_unitCircle.sizePolicy().hasHeightForWidth())
        self.plot_unitCircle.setSizePolicy(sizePolicy)
        self.plot_unitCircle.setMinimumSize(QtCore.QSize(400, 400))
        self.plot_unitCircle.setMaximumSize(QtCore.QSize(400, 400))
        self.plot_unitCircle.setSizeIncrement(QtCore.QSize(1, 1))
        self.plot_unitCircle.setBaseSize(QtCore.QSize(0, 0))
        self.plot_unitCircle.setStyleSheet("")
        self.plot_unitCircle.setObjectName("plot_unitCircle")
        self.gridLayout_5.addWidget(self.plot_unitCircle, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.wgt_unitCircle, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.grpbx_DigitalFilter, 0, 0, 1, 1)
        self.grpbx_AllPassFilter = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpbx_AllPassFilter.sizePolicy().hasHeightForWidth())
        self.grpbx_AllPassFilter.setSizePolicy(sizePolicy)
        self.grpbx_AllPassFilter.setMaximumSize(QtCore.QSize(300, 16777215))
        self.grpbx_AllPassFilter.setObjectName("grpbx_AllPassFilter")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.grpbx_AllPassFilter)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.grpbx_AllPassFilter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.table_coeff = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_coeff.sizePolicy().hasHeightForWidth())
        self.table_coeff.setSizePolicy(sizePolicy)
        self.table_coeff.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.table_coeff.setAlternatingRowColors(False)
        self.table_coeff.setShowGrid(True)
        self.table_coeff.setCornerButtonEnabled(False)
        self.table_coeff.setColumnCount(1)
        self.table_coeff.setObjectName("table_coeff")
        self.table_coeff.setRowCount(0)
        self.table_coeff.horizontalHeader().setVisible(False)
        self.table_coeff.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.table_coeff, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.plot_allPass = PlotWidget(self.grpbx_AllPassFilter)
        self.plot_allPass.setMinimumSize(QtCore.QSize(0, 70))
        self.plot_allPass.setMaximumSize(QtCore.QSize(300, 16777215))
        self.plot_allPass.setObjectName("plot_allPass")
        self.gridLayout_3.addWidget(self.plot_allPass, 2, 0, 1, 1)
        self.wgt_coefficient = QtWidgets.QWidget(self.grpbx_AllPassFilter)
        self.wgt_coefficient.setMinimumSize(QtCore.QSize(0, 70))
        self.wgt_coefficient.setMaximumSize(QtCore.QSize(300, 70))
        self.wgt_coefficient.setObjectName("wgt_coefficient")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.wgt_coefficient)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.all_pass_enable = QtWidgets.QCheckBox(self.wgt_coefficient)
        self.all_pass_enable.setObjectName("all_pass_enable")
        self.gridLayout_6.addWidget(self.all_pass_enable, 1, 0, 1, 2)
        self.btn_addCoeff = QtWidgets.QPushButton(self.wgt_coefficient)
        self.btn_addCoeff.setObjectName("btn_addCoeff")
        self.gridLayout_6.addWidget(self.btn_addCoeff, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.wgt_coefficient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.btn_removeCoeff = QtWidgets.QPushButton(self.wgt_coefficient)
        self.btn_removeCoeff.setObjectName("btn_removeCoeff")
        self.gridLayout_6.addWidget(self.btn_removeCoeff, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.wgt_coefficient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("background:white;\n"
"color:black;\n"
"")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_6.addWidget(self.comboBox, 0, 1, 1, 3)
        self.gridLayout_3.addWidget(self.wgt_coefficient, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.grpbx_AllPassFilter, 0, 1, 1, 1)
        self.grpbx_RealtimeFiltering = QtWidgets.QGroupBox(self.centralwidget)
        self.grpbx_RealtimeFiltering.setMaximumSize(QtCore.QSize(16777215, 300))
        self.grpbx_RealtimeFiltering.setObjectName("grpbx_RealtimeFiltering")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grpbx_RealtimeFiltering)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnClr = QtWidgets.QPushButton(self.grpbx_RealtimeFiltering)
        self.btnClr.setObjectName("btnClr")
        self.gridLayout_2.addWidget(self.btnClr, 1, 4, 1, 1)
        self.plot_realtimeFilter = PlotWidget(self.grpbx_RealtimeFiltering)
        self.plot_realtimeFilter.setObjectName("plot_realtimeFilter")
        self.gridLayout_2.addWidget(self.plot_realtimeFilter, 0, 2, 1, 2)
        self.plot_mouseInput = PlotWidget(self.grpbx_RealtimeFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_mouseInput.sizePolicy().hasHeightForWidth())
        self.plot_mouseInput.setSizePolicy(sizePolicy)
        self.plot_mouseInput.setMinimumSize(QtCore.QSize(200, 200))
        self.plot_mouseInput.setObjectName("plot_mouseInput")
        self.gridLayout_2.addWidget(self.plot_mouseInput, 0, 4, 1, 1)
        self.btn_openFile = QtWidgets.QPushButton(self.grpbx_RealtimeFiltering)
        self.btn_openFile.setStyleSheet("")
        self.btn_openFile.setObjectName("btn_openFile")
        self.gridLayout_2.addWidget(self.btn_openFile, 1, 0, 1, 1)
        self.plot_realtimeInput = PlotWidget(self.grpbx_RealtimeFiltering)
        self.plot_realtimeInput.setObjectName("plot_realtimeInput")
        self.gridLayout_2.addWidget(self.plot_realtimeInput, 0, 0, 1, 2)
        self.speed_slider = QtWidgets.QSlider(self.grpbx_RealtimeFiltering)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(100)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.gridLayout_2.addWidget(self.speed_slider, 1, 3, 1, 1)
        self.lbl_speed = QtWidgets.QLabel(self.grpbx_RealtimeFiltering)
        self.lbl_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_speed.setObjectName("lbl_speed")
        self.gridLayout_2.addWidget(self.lbl_speed, 1, 2, 1, 1)
        self.btn_play = QtWidgets.QPushButton(self.grpbx_RealtimeFiltering)
        self.btn_play.setCheckable(False)
        self.btn_play.setObjectName("btn_play")
        self.gridLayout_2.addWidget(self.btn_play, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.grpbx_RealtimeFiltering, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1488, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.label.setBuddy(self.wgt_coefficient)
        self.lbl_speed.setBuddy(self.speed_slider)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grpbx_DigitalFilter.setTitle(_translate("MainWindow", "Digital Filter Design"))
        self.btn_addPoles.setText(_translate("MainWindow", "Add Poles"))
        self.btn_addZeros.setText(_translate("MainWindow", "Add Zeros"))
        self.btn_removePoles.setText(_translate("MainWindow", "Remove Poles"))
        self.btn_RemoveZeros.setText(_translate("MainWindow", "Remove Zeros"))
        self.btn_Remove.setText(_translate("MainWindow", "Remove"))
        self.btn_removeAll.setText(_translate("MainWindow", "Remove All"))
        self.pair_mode_toggle.setText(_translate("MainWindow", "Pair Mode"))
        self.mouse_en.setText(_translate("MainWindow", "Mouse Enable"))
        self.grpbx_AllPassFilter.setTitle(_translate("MainWindow", "All Pass Filter Design"))
        self.groupBox.setTitle(_translate("MainWindow", "All Pass Filters"))
        self.all_pass_enable.setText(_translate("MainWindow", "All Pass"))
        self.btn_addCoeff.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Coefficient"))
        self.btn_removeCoeff.setText(_translate("MainWindow", "Remove"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "-0.9"))
        self.comboBox.setItemText(3, _translate("MainWindow", "-0.495"))
        self.comboBox.setItemText(4, _translate("MainWindow", "0"))
        self.comboBox.setItemText(5, _translate("MainWindow", "0.99"))
        self.comboBox.setItemText(6, _translate("MainWindow", "0.345"))
        self.grpbx_RealtimeFiltering.setTitle(_translate("MainWindow", "Realtime Filtering"))
        self.btnClr.setText(_translate("MainWindow", "Clear"))
        self.btn_openFile.setText(_translate("MainWindow", "Choose File"))
        self.btn_openFile.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.lbl_speed.setText(_translate("MainWindow", "Speed: 1"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_play.setShortcut(_translate("MainWindow", "Space"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport.setText(_translate("MainWindow", "Import Zeros/Poles"))
        self.actionExport.setText(_translate("MainWindow", "Export Zeros/Poles"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
