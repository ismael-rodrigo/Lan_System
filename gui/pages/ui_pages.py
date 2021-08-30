# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages_uibRFlcX.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(886, 507)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(140, 140, 140);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"\n"
"border:2px solid rgb(45, 45, 45);\n"
"border-top-color: rgb(255, 80, 80);\n"
"border-bottom-color: rgb(255, 80, 80);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border:none;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border:none;")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(250, 16777215))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border:none;")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 886, 467))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_4)

        StackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)

        StackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)

        StackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(550, 0))
        self.frame_8.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_2 = QScrollArea(self.frame_8)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 528, 483))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_15)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea_2)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(500, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(111, 111, 111);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, -1, 20, -1)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border-bottom:2px solid rgb(200,80,80);\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_6)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_7.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"\n"
"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
"border:2px solid rgb(60,60,60);\n"
"border-radius:8px;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(80,80,80);\n"
"}")
        self.lineEdit.setMaxLength(36)

        self.verticalLayout_9.addWidget(self.lineEdit)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_8.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_8)

        self.lineEdit_2 = QLineEdit(self.frame_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
"border:2px solid rgb(60,60,60);\n"
"border-radius:8px;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(80,80,80);\n"
"}")
        self.lineEdit_2.setMaxLength(36)

        self.verticalLayout_10.addWidget(self.lineEdit_2)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, -1)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.frame_12)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 50))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
"border:2px solid rgb(60,60,60);\n"
"border-radius:8px;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(80,80,80);\n"
"}")
        self.lineEdit_3.setMaxLength(36)

        self.verticalLayout_11.addWidget(self.lineEdit_3)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setStyleSheet(u"border:2px solid rgb(60,60,60);\n"
"border-radius:8px;")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(self.frame_13)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"border:none;")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_13)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"border:none;")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_13)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"border:none;")

        self.horizontalLayout_3.addWidget(self.radioButton_3)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.verticalSpacer = QSpacerItem(108, 66, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_14)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame)

        StackedWidget.addWidget(self.page_4)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\">UserName</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\">Tempo</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\">Maquina</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\">Game</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\">Valor</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"Adicionar m\u00e1quina", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"Monitor", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"Perif\u00e9ricos", None))
        self.radioButton.setText(QCoreApplication.translate("StackedWidget", u"Sony", None))
        self.radioButton_2.setText(QCoreApplication.translate("StackedWidget", u"Xbox", None))
        self.radioButton_3.setText(QCoreApplication.translate("StackedWidget", u"PC", None))
    # retranslateUi

