# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/Lightly/kdecoration/config/ui/oceanexceptiondialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OceanExceptionDialog(object):
    def setupUi(self, OceanExceptionDialog):
        OceanExceptionDialog.setObjectName("OceanExceptionDialog")
        OceanExceptionDialog.resize(362, 321)
        self.verticalLayout = QtWidgets.QVBoxLayout(OceanExceptionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(OceanExceptionDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.detectDialogButton = QtWidgets.QPushButton(self.groupBox)
        self.detectDialogButton.setObjectName("detectDialogButton")
        self.gridLayout_2.addWidget(self.detectDialogButton, 2, 2, 1, 1)
        self.exceptionEditor = QtWidgets.QLineEdit(self.groupBox)
        self.exceptionEditor.setProperty("showClearButton", True)
        self.exceptionEditor.setObjectName("exceptionEditor")
        self.gridLayout_2.addWidget(self.exceptionEditor, 1, 1, 1, 2)
        self.exceptionType = QtWidgets.QComboBox(self.groupBox)
        self.exceptionType.setObjectName("exceptionType")
        self.exceptionType.addItem("")
        self.exceptionType.addItem("")
        self.gridLayout_2.addWidget(self.exceptionType, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(OceanExceptionDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.borderSizeCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.borderSizeCheckBox.setObjectName("borderSizeCheckBox")
        self.gridLayout_3.addWidget(self.borderSizeCheckBox, 0, 0, 1, 1)
        self.hideTitleBar = QtWidgets.QCheckBox(self.groupBox_2)
        self.hideTitleBar.setObjectName("hideTitleBar")
        self.gridLayout_3.addWidget(self.hideTitleBar, 2, 0, 1, 2)
        self.borderSizeComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.borderSizeComboBox.setEnabled(False)
        self.borderSizeComboBox.setObjectName("borderSizeComboBox")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.borderSizeComboBox.addItem("")
        self.gridLayout_3.addWidget(self.borderSizeComboBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(OceanExceptionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.exceptionType)
        self.label_2.setBuddy(self.exceptionEditor)

        self.retranslateUi(OceanExceptionDialog)
        self.buttonBox.accepted.connect(OceanExceptionDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(OceanExceptionDialog.reject) # type: ignore
        self.borderSizeCheckBox.toggled['bool'].connect(self.borderSizeComboBox.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OceanExceptionDialog)

    def retranslateUi(self, OceanExceptionDialog):
        _translate = QtCore.QCoreApplication.translate
        OceanExceptionDialog.setWindowTitle(_translate("OceanExceptionDialog", "Dialog"))
        self.groupBox.setTitle(_translate("OceanExceptionDialog", "Window Identification"))
        self.label.setText(_translate("OceanExceptionDialog", "&Matching window property: "))
        self.label_2.setText(_translate("OceanExceptionDialog", "Regular expression &to match: "))
        self.detectDialogButton.setText(_translate("OceanExceptionDialog", "Detect Window Properties"))
        self.exceptionType.setItemText(0, _translate("OceanExceptionDialog", "Window Class Name"))
        self.exceptionType.setItemText(1, _translate("OceanExceptionDialog", "Window Title"))
        self.groupBox_2.setTitle(_translate("OceanExceptionDialog", "Decoration Options"))
        self.borderSizeCheckBox.setText(_translate("OceanExceptionDialog", "Border size:"))
        self.hideTitleBar.setText(_translate("OceanExceptionDialog", "Hide window title bar"))
        self.borderSizeComboBox.setItemText(0, _translate("OceanExceptionDialog", "No Border", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(1, _translate("OceanExceptionDialog", "No Side Borders", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(2, _translate("OceanExceptionDialog", "Tiny", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(3, _translate("OceanExceptionDialog", "Normal", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(4, _translate("OceanExceptionDialog", "Large", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(5, _translate("OceanExceptionDialog", "Very Large", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(6, _translate("OceanExceptionDialog", "Huge", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(7, _translate("OceanExceptionDialog", "Very Huge", "@item:inlistbox Border size:"))
        self.borderSizeComboBox.setItemText(8, _translate("OceanExceptionDialog", "Oversized", "@item:inlistbox Border size:"))