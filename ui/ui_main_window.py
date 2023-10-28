# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1644, 957)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(460, 340, 601, 311))
        self.graph2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.graph2.setObjectName(u"graph2")
        self.graph2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(460, 10, 601, 321))
        self.graph4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.graph4.setObjectName(u"graph4")
        self.graph4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(1070, 10, 551, 321))
        self.graph5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.graph5.setObjectName(u"graph5")
        self.graph5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(1070, 340, 541, 311))
        self.graph6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.graph6.setObjectName(u"graph6")
        self.graph6.setSizeConstraint(QLayout.SetMaximumSize)
        self.graph6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(460, 660, 601, 271))
        self.graph8 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.graph8.setObjectName(u"graph8")
        self.graph8.setSizeConstraint(QLayout.SetMaximumSize)
        self.graph8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(1070, 660, 541, 271))
        self.graph8_2 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.graph8_2.setObjectName(u"graph8_2")
        self.graph8_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.graph8_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 441, 211))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(14)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.layoutWidget)
        self.btn1.setObjectName(u"btn1")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.btn1.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btn1)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.comboBox)

        self.btn2 = QPushButton(self.layoutWidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.btn2)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_2)

        self.btn3 = QPushButton(self.layoutWidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.btn3)

        self.btn4 = QPushButton(self.layoutWidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.btn4)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 520, 441, 241))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_IP = QLineEdit(self.layoutWidget1)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        self.lineEdit_IP.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_IP, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_port = QLineEdit(self.layoutWidget1)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_port, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_span_millisecond = QLineEdit(self.layoutWidget1)
        self.lineEdit_span_millisecond.setObjectName(u"lineEdit_span_seconds")
        self.lineEdit_span_millisecond.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_span_millisecond, 2, 1, 1, 1)

        self.btn_save_server = QPushButton(self.layoutWidget1)
        self.btn_save_server.setObjectName(u"btn_save_server")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        self.btn_save_server.setFont(font2)

        self.gridLayout.addWidget(self.btn_save_server, 3, 1, 1, 1)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 770, 441, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_start_send = QPushButton(self.layoutWidget2)
        self.btn_start_send.setObjectName(u"btn_start_send")
        self.btn_start_send.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_start_send)

        self.btn_stop_send = QPushButton(self.layoutWidget2)
        self.btn_stop_send.setObjectName(u"btn_stop_send")
        self.btn_stop_send.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_stop_send)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 241, 441, 271))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_T1_2 = QLabel(self.layoutWidget3)
        self.label_T1_2.setObjectName(u"label_T1_2")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_T1_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_T1_2)

        self.label_T2_2 = QLabel(self.layoutWidget3)
        self.label_T2_2.setObjectName(u"label_T2_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_T2_2.sizePolicy().hasHeightForWidth())
        self.label_T2_2.setSizePolicy(sizePolicy)
        self.label_T2_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_T2_2)

        self.label_T2_3 = QLabel(self.layoutWidget3)
        self.label_T2_3.setObjectName(u"label_T2_3")
        sizePolicy.setHeightForWidth(self.label_T2_3.sizePolicy().hasHeightForWidth())
        self.label_T2_3.setSizePolicy(sizePolicy)
        self.label_T2_3.setFont(font3)

        self.verticalLayout.addWidget(self.label_T2_3)

        self.label_T2_4 = QLabel(self.layoutWidget3)
        self.label_T2_4.setObjectName(u"label_T2_4")
        sizePolicy.setHeightForWidth(self.label_T2_4.sizePolicy().hasHeightForWidth())
        self.label_T2_4.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_T2_4.setFont(font4)

        self.verticalLayout.addWidget(self.label_T2_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u7f51\u5361", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u53c2\u6570", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668IP", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("MainWindow", u"192.168.1.101", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.lineEdit_port.setText(QCoreApplication.translate("MainWindow", u"9101", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u65f6\u95f4\u95f4\u9694", None))
        self.lineEdit_span_millisecond.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.btn_save_server.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.btn_start_send.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.btn_stop_send.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u53d1\u9001", None))
        self.label_T1_2.setText(QCoreApplication.translate("MainWindow", u"\u547c\u5438\u9891\u7387:", None))
        self.label_T2_2.setText(QCoreApplication.translate("MainWindow", u"\u5fc3\u7387\uff1a", None))
        self.label_T2_3.setText(QCoreApplication.translate("MainWindow", u"\u59ff\u6001\uff1a", None))
        self.label_T2_4.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e\uff1a", None))
    # retranslateUi

