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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1701, 924)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(880, 240, 401, 231))
        self.graph2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.graph2.setObjectName(u"graph2")
        self.graph2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(880, 0, 401, 231))
        self.graph4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.graph4.setObjectName(u"graph4")
        self.graph4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(1290, 0, 401, 231))
        self.graph5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.graph5.setObjectName(u"graph5")
        self.graph5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(1290, 240, 401, 231))
        self.graph6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.graph6.setObjectName(u"graph6")
        self.graph6.setSizeConstraint(QLayout.SetMaximumSize)
        self.graph6.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_send = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_send.setObjectName(u"plainTextEdit_send")
        self.plainTextEdit_send.setGeometry(QRect(1100, 480, 591, 461))
        self.plainTextEdit_send.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.listWidget_2 = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(10, 180, 341, 171))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.listWidget_2.setFont(font1)
        self.listWidget_2.setStyleSheet(u"background-color: rgb(177, 177, 177);")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 360, 341, 551))
        self.label_T1_2 = QLabel(self.groupBox)
        self.label_T1_2.setObjectName(u"label_T1_2")
        self.label_T1_2.setGeometry(QRect(10, 20, 321, 34))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_T1_2.setFont(font2)
        self.label_T2_2 = QLabel(self.groupBox)
        self.label_T2_2.setObjectName(u"label_T2_2")
        self.label_T2_2.setGeometry(QRect(10, 70, 321, 34))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_T2_2.sizePolicy().hasHeightForWidth())
        self.label_T2_2.setSizePolicy(sizePolicy)
        self.label_T2_2.setFont(font2)
        self.listWidget_posture = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget_posture)
        QListWidgetItem(self.listWidget_posture)
        self.listWidget_posture.setObjectName(u"listWidget_posture")
        self.listWidget_posture.setGeometry(QRect(10, 130, 331, 461))
        font3 = QFont()
        font3.setPointSize(60)
        font3.setBold(True)
        self.listWidget_posture.setFont(font3)
        self.listWidget_posture.setStyleSheet(u"background-color: rgb(184, 184, 184);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(360, 480, 371, 421))
        self.groupBox_2.setFont(font1)
        self.listWidgetPersonLocation = QListWidget(self.groupBox_2)
        QListWidgetItem(self.listWidgetPersonLocation)
        self.listWidgetPersonLocation.setObjectName(u"listWidgetPersonLocation")
        self.listWidgetPersonLocation.setGeometry(QRect(10, 60, 361, 361))
        self.listWidgetPersonLocation.setFont(font1)
        self.listWidgetPersonLocation.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 91, 31))
        self.label_personNumber = QLabel(self.groupBox_2)
        self.label_personNumber.setObjectName(u"label_personNumber")
        self.label_personNumber.setGeometry(QRect(100, 20, 161, 31))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(740, 480, 351, 461))
        self.layoutWidget = QWidget(self.groupBox_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 331, 301))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_IP = QLineEdit(self.layoutWidget)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.lineEdit_IP.setFont(font4)

        self.gridLayout.addWidget(self.lineEdit_IP, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.btn_save_server = QPushButton(self.layoutWidget)
        self.btn_save_server.setObjectName(u"btn_save_server")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(False)
        self.btn_save_server.setFont(font5)

        self.gridLayout.addWidget(self.btn_save_server, 3, 1, 1, 1)

        self.lineEdit_span_millisecond = QLineEdit(self.layoutWidget)
        self.lineEdit_span_millisecond.setObjectName(u"lineEdit_span_millisecond")
        self.lineEdit_span_millisecond.setFont(font4)

        self.gridLayout.addWidget(self.lineEdit_span_millisecond, 2, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_port = QLineEdit(self.layoutWidget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setFont(font4)

        self.gridLayout.addWidget(self.lineEdit_port, 1, 1, 1, 1)

        self.btn_clear_log = QPushButton(self.groupBox_4)
        self.btn_clear_log.setObjectName(u"btn_clear_log")
        self.btn_clear_log.setGeometry(QRect(220, 20, 121, 34))
        self.btn_clear_log.setFont(font5)
        self.btn_start_send = QPushButton(self.groupBox_4)
        self.btn_start_send.setObjectName(u"btn_start_send")
        self.btn_start_send.setGeometry(QRect(10, 370, 331, 41))
        self.btn_start_send.setFont(font5)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(12, 7, 341, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.layoutWidget1)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setFont(font4)

        self.verticalLayout.addWidget(self.btn1)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font4)

        self.verticalLayout.addWidget(self.comboBox)

        self.btn_open_circle = QPushButton(self.layoutWidget1)
        self.btn_open_circle.setObjectName(u"btn_open_circle")
        self.btn_open_circle.setFont(font4)

        self.verticalLayout.addWidget(self.btn_open_circle)

        self.btn_open_wifi = QPushButton(self.layoutWidget1)
        self.btn_open_wifi.setObjectName(u"btn_open_wifi")
        self.btn_open_wifi.setFont(font4)

        self.verticalLayout.addWidget(self.btn_open_wifi)

        self.verticalLayoutWidget_10 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(360, 0, 511, 471))
        self.graph8 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.graph8.setObjectName(u"graph8")
        self.graph8.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907IP\u5217\u8868", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle("")
        self.label_T1_2.setText(QCoreApplication.translate("MainWindow", u"\u547c\u5438:", None))
        self.label_T2_2.setText(QCoreApplication.translate("MainWindow", u"\u5fc3\u7387\uff1a", None))

        __sortingEnabled1 = self.listWidget_posture.isSortingEnabled()
        self.listWidget_posture.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_posture.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"0\uff1a\u65e0\u4eba", None));
        ___qlistwidgetitem2 = self.listWidget_posture.item(1)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1\uff1a\u65e0\u4eba", None));
        self.listWidget_posture.setSortingEnabled(__sortingEnabled1)

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u4f4d\u7f6e\u5750\u6807", None))

        __sortingEnabled2 = self.listWidgetPersonLocation.isSortingEnabled()
        self.listWidgetPersonLocation.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidgetPersonLocation.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u6570\u636e", None));
        self.listWidgetPersonLocation.setSortingEnabled(__sortingEnabled2)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u623f\u95f4\u4eba\u6570\uff1a", None))
        self.label_personNumber.setText("")
        self.groupBox_4.setTitle("")
        self.lineEdit_IP.setText(QCoreApplication.translate("MainWindow", u"192.168.101.45", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u65f6\u95f4\u95f4\u9694", None))
        self.btn_save_server.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.lineEdit_span_millisecond.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668IP", None))
        self.lineEdit_port.setText(QCoreApplication.translate("MainWindow", u"8104", None))
        self.btn_clear_log.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u65e5\u5fd7", None))
        self.btn_start_send.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u7f51\u5361\u6570\u636e", None))
        self.btn_open_circle.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u7efc\u5408\u63a2\u5934\u8bbe\u5907", None))
        self.btn_open_wifi.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00WIFI\u8bbe\u5907", None))
    # retranslateUi

