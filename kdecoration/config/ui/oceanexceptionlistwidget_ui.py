# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/Lightly/kdecoration/config/ui/oceanexceptionlistwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OceanExceptionListWidget(object):
    def setupUi(self, OceanExceptionListWidget):
        OceanExceptionListWidget.setObjectName("OceanExceptionListWidget")
        OceanExceptionListWidget.resize(473, 182)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OceanExceptionListWidget.sizePolicy().hasHeightForWidth())
        OceanExceptionListWidget.setSizePolicy(sizePolicy)
        OceanExceptionListWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(OceanExceptionListWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.exceptionListView = QtWidgets.QTreeView(OceanExceptionListWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exceptionListView.sizePolicy().hasHeightForWidth())
        self.exceptionListView.setSizePolicy(sizePolicy)
        self.exceptionListView.setMinimumSize(QtCore.QSize(100, 100))
        self.exceptionListView.setObjectName("exceptionListView")
        self.gridLayout.addWidget(self.exceptionListView, 0, 0, 6, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.moveUpButton = QtWidgets.QPushButton(OceanExceptionListWidget)
        self.moveUpButton.setObjectName("moveUpButton")
        self.gridLayout.addWidget(self.moveUpButton, 0, 1, 1, 1)
        self.moveDownButton = QtWidgets.QPushButton(OceanExceptionListWidget)
        self.moveDownButton.setObjectName("moveDownButton")
        self.gridLayout.addWidget(self.moveDownButton, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(OceanExceptionListWidget)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(OceanExceptionListWidget)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 3, 1, 1, 1)
        self.editButton = QtWidgets.QPushButton(OceanExceptionListWidget)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 4, 1, 1, 1)

        self.retranslateUi(OceanExceptionListWidget)
        QtCore.QMetaObject.connectSlotsByName(OceanExceptionListWidget)
        OceanExceptionListWidget.setTabOrder(self.exceptionListView, self.moveUpButton)
        OceanExceptionListWidget.setTabOrder(self.moveUpButton, self.moveDownButton)
        OceanExceptionListWidget.setTabOrder(self.moveDownButton, self.addButton)
        OceanExceptionListWidget.setTabOrder(self.addButton, self.removeButton)
        OceanExceptionListWidget.setTabOrder(self.removeButton, self.editButton)

    def retranslateUi(self, OceanExceptionListWidget):
        _translate = QtCore.QCoreApplication.translate
        self.moveUpButton.setText(_translate("OceanExceptionListWidget", "Move Up"))
        self.moveDownButton.setText(_translate("OceanExceptionListWidget", "Move Down"))
        self.addButton.setText(_translate("OceanExceptionListWidget", "Add"))
        self.removeButton.setText(_translate("OceanExceptionListWidget", "Remove"))
        self.editButton.setText(_translate("OceanExceptionListWidget", "Edit"))
