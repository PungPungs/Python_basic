# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled copyVMdlSB.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 426)
        MainWindow.setStyleSheet(u"/* ===== \uae30\ubcf8 \ud3f0\ud2b8 \ubc0f \uacf5\ud1b5 ===== */\n"
"* {\n"
"    font-family: 'Inter', 'Pretendard', 'Segoe UI', 'Noto Sans KR', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #2f2f2f;\n"
"}\n"
"\n"
"/* ===== \uc804\uccb4 \ubc30\uacbd ===== */\n"
"QMainWindow, QWidget {\n"
"    background-color: #e6f2fb;\n"
"}\n"
"\n"
"/* ===== \ud504\ub85c\uadf8\ub7a8 \ud5e4\ub354 \ub77c\ubca8 (\uc81c\uac70 \ud6a8\uacfc) ===== */\n"
"#label_header_title {\n"
"    color: transparent;\n"
"    background-color: transparent;\n"
"    font-size: 0px;\n"
"    height: 0px;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== \uadf8\ub8f9 \ubc15\uc2a4 ===== */\n"
"QGroupBox {\n"
"    border: 1px solid #bcdff1;\n"
"    border-radius: 8px;\n"
"    margin-top: 12px;\n"
"    background-color: #f2f9fd;\n"
"    padding: 12px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 6px 12px;\n"
"    font-weight: 600;\n"
"    fo"
                        "nt-size: 15px;\n"
"    color: #1e4b6d;\n"
"}\n"
"\n"
"/* ===== \ub77c\ubca8 ===== */\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    color: #2f2f2f;\n"
"    background-color: #f2f9fd;\n"
"}\n"
"\n"
"/* ===== \ucf64\ubcf4\ubc15\uc2a4 ===== */\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #c0ddeb;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox:hover {\n"
"    border-color: #96c9e0;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #c0ddeb;\n"
"}\n"
"\n"
"/* ===== \ud14d\uc2a4\ud2b8 \uc5d0\ub514\ud2b8 ===== */\n"
"QTextEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #c0ddeb;\n"
"    border-radius: 6px;\n"
"    padding: 2px 6px;       /* \uc0c1\ud558 padding \ucd95\uc18c (4 \u2192 2px) */\n"
"    color: #2f2f2f;\n"
"    font-size: 13px;\n"
"    min-height: 28px;       /* \uae30\ubcf8 \ub192\uc774 \uc904\uc774\uae30 (\uc608: 60px \u2192 28"
                        "px) */\n"
"    max-height: 32px;       /* \ud544\uc694 \uc2dc \uc81c\ud55c \ub192\uc774 \ucd94\uac00 */\n"
"}\n"
"\n"
"QTextEdit QScrollBar:vertical,\n"
"QTextEdit QScrollBar:horizontal {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* ===== \uae30\ubcf8 \ubc84\ud2bc ===== */\n"
"QPushButton {\n"
"    background-color: #d3ecf9;\n"
"    border: 1px solid #a2cbe3;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    color: #1e4b6d;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c0e2f5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #aad3ea;\n"
"}\n"
"\n"
"/* ===== \uc2dc\uc791 \ubc84\ud2bc (\uc5f0\ud55c \ud558\ub298+\ubbfc\ud2b8\ud1a4) ===== */\n"
"#pb_sss_start, #pb_mag_start, #pb_ss_start {\n"
"    background-color: #a7dff7;\n"
"    color: #ffffff;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"#pb_sss_start:hover, #pb_mag_start:hover, #pb_ss_start:hover {\n"
"    background-c"
                        "olor: #8fd3ee;\n"
"}\n"
"\n"
"/* ===== \uc815\uc9c0 \ubc84\ud2bc (\ud1a4\ub2e4\uc6b4 \ud551\ud06c) ===== */\n"
"#pb_sss_stop, #pb_mag_stop, #pb_ss_stop {\n"
"    background-color: #f2b6b6;\n"
"    color: #ffffff;\n"
"    border-radius: 6px;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"#pb_sss_stop:hover, #pb_mag_stop:hover, #pb_ss_stop:hover {\n"
"    background-color: #e89fa2;\n"
"}\n"
"\n"
"/* ===== \ub77c\ub514\uc624 \ubc84\ud2bc ===== */\n"
"QRadioButton {\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding-left: 4px;\n"
"    color: #2f2f2f;\n"
"    background-color: #f2f9fd;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"    border-radius: 8px;\n"
"    border: 2px solid #79c2f2;\n"
"}\n"
"QRadioButton::indicator::checked {\n"
"    background-color: #79c2f2;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* ===== \uccb4\ud06c\ubc15\uc2a4 ===== */\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    pa"
                        "dding-left: 4px;\n"
"    color: #2f2f2f;\n"
"    background-color: #f2f9fd;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #79c2f2;\n"
"    background: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #79c2f2;\n"
"    image: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.group_sss = QGroupBox(self.centralwidget)
        self.group_sss.setObjectName(u"group_sss")
        self.layout_sss = QVBoxLayout(self.group_sss)
        self.layout_sss.setObjectName(u"layout_sss")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label_port_sss = QLabel(self.group_sss)
        self.label_port_sss.setObjectName(u"label_port_sss")

        self.hboxLayout.addWidget(self.label_port_sss)

        self.cb_sss = QComboBox(self.group_sss)
        self.cb_sss.setObjectName(u"cb_sss")

        self.hboxLayout.addWidget(self.cb_sss)

        self.pb_sss = QPushButton(self.group_sss)
        self.pb_sss.setObjectName(u"pb_sss")

        self.hboxLayout.addWidget(self.pb_sss)


        self.layout_sss.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label_rpm_sss = QLabel(self.group_sss)
        self.label_rpm_sss.setObjectName(u"label_rpm_sss")

        self.hboxLayout1.addWidget(self.label_rpm_sss)

        self.cb_rpm_sss = QComboBox(self.group_sss)
        self.cb_rpm_sss.setObjectName(u"cb_rpm_sss")

        self.hboxLayout1.addWidget(self.cb_rpm_sss)


        self.layout_sss.addLayout(self.hboxLayout1)

        self.label_motor_sss = QLabel(self.group_sss)
        self.label_motor_sss.setObjectName(u"label_motor_sss")

        self.layout_sss.addWidget(self.label_motor_sss)

        self.rb_sss_0 = QRadioButton(self.group_sss)
        self.rb_sss_0.setObjectName(u"rb_sss_0")

        self.layout_sss.addWidget(self.rb_sss_0)

        self.rb_sss_1 = QRadioButton(self.group_sss)
        self.rb_sss_1.setObjectName(u"rb_sss_1")

        self.layout_sss.addWidget(self.rb_sss_1)

        self.rb_sss_2 = QRadioButton(self.group_sss)
        self.rb_sss_2.setObjectName(u"rb_sss_2")

        self.layout_sss.addWidget(self.rb_sss_2)

        self.rb_sss_3 = QRadioButton(self.group_sss)
        self.rb_sss_3.setObjectName(u"rb_sss_3")

        self.layout_sss.addWidget(self.rb_sss_3)

        self.rb_sss_4 = QRadioButton(self.group_sss)
        self.rb_sss_4.setObjectName(u"rb_sss_4")

        self.layout_sss.addWidget(self.rb_sss_4)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label_distance_sss = QLabel(self.group_sss)
        self.label_distance_sss.setObjectName(u"label_distance_sss")

        self.hboxLayout2.addWidget(self.label_distance_sss)

        self.te_sss_distance = QTextEdit(self.group_sss)
        self.te_sss_distance.setObjectName(u"te_sss_distance")

        self.hboxLayout2.addWidget(self.te_sss_distance)


        self.layout_sss.addLayout(self.hboxLayout2)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.label_state_sss = QLabel(self.group_sss)
        self.label_state_sss.setObjectName(u"label_state_sss")

        self.hboxLayout3.addWidget(self.label_state_sss)

        self.te_sss_state = QTextEdit(self.group_sss)
        self.te_sss_state.setObjectName(u"te_sss_state")

        self.hboxLayout3.addWidget(self.te_sss_state)


        self.layout_sss.addLayout(self.hboxLayout3)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.pb_sss_start = QPushButton(self.group_sss)
        self.pb_sss_start.setObjectName(u"pb_sss_start")

        self.hboxLayout4.addWidget(self.pb_sss_start)

        self.pb_sss_stop = QPushButton(self.group_sss)
        self.pb_sss_stop.setObjectName(u"pb_sss_stop")

        self.hboxLayout4.addWidget(self.pb_sss_stop)


        self.layout_sss.addLayout(self.hboxLayout4)


        self.mainLayout.addWidget(self.group_sss)

        self.group_mag = QGroupBox(self.centralwidget)
        self.group_mag.setObjectName(u"group_mag")
        self.layout_mag = QVBoxLayout(self.group_mag)
        self.layout_mag.setObjectName(u"layout_mag")
        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.label_port_mag = QLabel(self.group_mag)
        self.label_port_mag.setObjectName(u"label_port_mag")

        self.hboxLayout5.addWidget(self.label_port_mag)

        self.cb_mag = QComboBox(self.group_mag)
        self.cb_mag.setObjectName(u"cb_mag")

        self.hboxLayout5.addWidget(self.cb_mag)

        self.pb_mag = QPushButton(self.group_mag)
        self.pb_mag.setObjectName(u"pb_mag")

        self.hboxLayout5.addWidget(self.pb_mag)


        self.layout_mag.addLayout(self.hboxLayout5)

        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.label_rpm_mag = QLabel(self.group_mag)
        self.label_rpm_mag.setObjectName(u"label_rpm_mag")

        self.hboxLayout6.addWidget(self.label_rpm_mag)

        self.cb_rpm_mag = QComboBox(self.group_mag)
        self.cb_rpm_mag.setObjectName(u"cb_rpm_mag")

        self.hboxLayout6.addWidget(self.cb_rpm_mag)


        self.layout_mag.addLayout(self.hboxLayout6)

        self.label_motor_mag = QLabel(self.group_mag)
        self.label_motor_mag.setObjectName(u"label_motor_mag")

        self.layout_mag.addWidget(self.label_motor_mag)

        self.rb_mag_0 = QRadioButton(self.group_mag)
        self.rb_mag_0.setObjectName(u"rb_mag_0")

        self.layout_mag.addWidget(self.rb_mag_0)

        self.rb_mag_1 = QRadioButton(self.group_mag)
        self.rb_mag_1.setObjectName(u"rb_mag_1")

        self.layout_mag.addWidget(self.rb_mag_1)

        self.rb_mag_2 = QRadioButton(self.group_mag)
        self.rb_mag_2.setObjectName(u"rb_mag_2")

        self.layout_mag.addWidget(self.rb_mag_2)

        self.rb_mag_3 = QRadioButton(self.group_mag)
        self.rb_mag_3.setObjectName(u"rb_mag_3")

        self.layout_mag.addWidget(self.rb_mag_3)

        self.rb_mag_4 = QRadioButton(self.group_mag)
        self.rb_mag_4.setObjectName(u"rb_mag_4")

        self.layout_mag.addWidget(self.rb_mag_4)

        self.hboxLayout7 = QHBoxLayout()
        self.hboxLayout7.setObjectName(u"hboxLayout7")
        self.label_distance_mag = QLabel(self.group_mag)
        self.label_distance_mag.setObjectName(u"label_distance_mag")

        self.hboxLayout7.addWidget(self.label_distance_mag)

        self.te_mag_distance = QTextEdit(self.group_mag)
        self.te_mag_distance.setObjectName(u"te_mag_distance")

        self.hboxLayout7.addWidget(self.te_mag_distance)


        self.layout_mag.addLayout(self.hboxLayout7)

        self.hboxLayout8 = QHBoxLayout()
        self.hboxLayout8.setObjectName(u"hboxLayout8")
        self.label_state_mag = QLabel(self.group_mag)
        self.label_state_mag.setObjectName(u"label_state_mag")

        self.hboxLayout8.addWidget(self.label_state_mag)

        self.te_mag_state = QTextEdit(self.group_mag)
        self.te_mag_state.setObjectName(u"te_mag_state")

        self.hboxLayout8.addWidget(self.te_mag_state)


        self.layout_mag.addLayout(self.hboxLayout8)

        self.hboxLayout9 = QHBoxLayout()
        self.hboxLayout9.setObjectName(u"hboxLayout9")
        self.pb_mag_start = QPushButton(self.group_mag)
        self.pb_mag_start.setObjectName(u"pb_mag_start")

        self.hboxLayout9.addWidget(self.pb_mag_start)

        self.pb_mag_stop = QPushButton(self.group_mag)
        self.pb_mag_stop.setObjectName(u"pb_mag_stop")

        self.hboxLayout9.addWidget(self.pb_mag_stop)


        self.layout_mag.addLayout(self.hboxLayout9)


        self.mainLayout.addWidget(self.group_mag)

        self.group_ss = QGroupBox(self.centralwidget)
        self.group_ss.setObjectName(u"group_ss")
        self.layout_ss = QVBoxLayout(self.group_ss)
        self.layout_ss.setObjectName(u"layout_ss")
        self.hboxLayout10 = QHBoxLayout()
        self.hboxLayout10.setObjectName(u"hboxLayout10")
        self.label_port_ss = QLabel(self.group_ss)
        self.label_port_ss.setObjectName(u"label_port_ss")

        self.hboxLayout10.addWidget(self.label_port_ss)

        self.cb_ss = QComboBox(self.group_ss)
        self.cb_ss.setObjectName(u"cb_ss")

        self.hboxLayout10.addWidget(self.cb_ss)

        self.pb_ss = QPushButton(self.group_ss)
        self.pb_ss.setObjectName(u"pb_ss")

        self.hboxLayout10.addWidget(self.pb_ss)


        self.layout_ss.addLayout(self.hboxLayout10)

        self.hboxLayout11 = QHBoxLayout()
        self.hboxLayout11.setObjectName(u"hboxLayout11")
        self.label_rpm_ss = QLabel(self.group_ss)
        self.label_rpm_ss.setObjectName(u"label_rpm_ss")

        self.hboxLayout11.addWidget(self.label_rpm_ss)

        self.cb_rpm_ss = QComboBox(self.group_ss)
        self.cb_rpm_ss.setObjectName(u"cb_rpm_ss")

        self.hboxLayout11.addWidget(self.cb_rpm_ss)


        self.layout_ss.addLayout(self.hboxLayout11)

        self.label_motor_ss = QLabel(self.group_ss)
        self.label_motor_ss.setObjectName(u"label_motor_ss")

        self.layout_ss.addWidget(self.label_motor_ss)

        self.rb_ss_0 = QRadioButton(self.group_ss)
        self.rb_ss_0.setObjectName(u"rb_ss_0")

        self.layout_ss.addWidget(self.rb_ss_0)

        self.rb_ss_1 = QRadioButton(self.group_ss)
        self.rb_ss_1.setObjectName(u"rb_ss_1")

        self.layout_ss.addWidget(self.rb_ss_1)

        self.rb_ss_2 = QRadioButton(self.group_ss)
        self.rb_ss_2.setObjectName(u"rb_ss_2")

        self.layout_ss.addWidget(self.rb_ss_2)

        self.rb_ss_3 = QRadioButton(self.group_ss)
        self.rb_ss_3.setObjectName(u"rb_ss_3")

        self.layout_ss.addWidget(self.rb_ss_3)

        self.rb_ss_4 = QRadioButton(self.group_ss)
        self.rb_ss_4.setObjectName(u"rb_ss_4")

        self.layout_ss.addWidget(self.rb_ss_4)

        self.hboxLayout12 = QHBoxLayout()
        self.hboxLayout12.setObjectName(u"hboxLayout12")
        self.label_distance_ss = QLabel(self.group_ss)
        self.label_distance_ss.setObjectName(u"label_distance_ss")

        self.hboxLayout12.addWidget(self.label_distance_ss)

        self.te_ss_distance = QTextEdit(self.group_ss)
        self.te_ss_distance.setObjectName(u"te_ss_distance")

        self.hboxLayout12.addWidget(self.te_ss_distance)


        self.layout_ss.addLayout(self.hboxLayout12)

        self.hboxLayout13 = QHBoxLayout()
        self.hboxLayout13.setObjectName(u"hboxLayout13")
        self.label_state_ss = QLabel(self.group_ss)
        self.label_state_ss.setObjectName(u"label_state_ss")

        self.hboxLayout13.addWidget(self.label_state_ss)

        self.te_ss_state = QTextEdit(self.group_ss)
        self.te_ss_state.setObjectName(u"te_ss_state")

        self.hboxLayout13.addWidget(self.te_ss_state)


        self.layout_ss.addLayout(self.hboxLayout13)

        self.hboxLayout14 = QHBoxLayout()
        self.hboxLayout14.setObjectName(u"hboxLayout14")
        self.pb_ss_start = QPushButton(self.group_ss)
        self.pb_ss_start.setObjectName(u"pb_ss_start")

        self.hboxLayout14.addWidget(self.pb_ss_start)

        self.pb_ss_stop = QPushButton(self.group_ss)
        self.pb_ss_stop.setObjectName(u"pb_ss_stop")

        self.hboxLayout14.addWidget(self.pb_ss_stop)


        self.layout_ss.addLayout(self.hboxLayout14)


        self.mainLayout.addWidget(self.group_ss)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ubaa8\ub358 \ubaa8\ud130 \ucee8\ud2b8\ub864 \ud504\ub85c\uadf8\ub7a8", None))
        self.group_sss.setTitle(QCoreApplication.translate("MainWindow", u"SSS", None))
        self.label_port_sss.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pb_sss.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.label_rpm_sss.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_motor_sss.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc120\ud0dd", None))
        self.rb_sss_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rb_sss_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.rb_sss_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.rb_sss_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.rb_sss_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_distance_sss.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\uac70\ub9ac", None))
        self.label_state_sss.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.pb_sss_start.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #4CAF50; color: white; border-radius: 5px;", None))
        self.pb_sss_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.pb_sss_stop.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #F44336; color: white; border-radius: 5px;", None))
        self.pb_sss_stop.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.group_mag.setTitle(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.label_port_mag.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pb_mag.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.label_rpm_mag.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_motor_mag.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc120\ud0dd", None))
        self.rb_mag_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rb_mag_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.rb_mag_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.rb_mag_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.rb_mag_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_distance_mag.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\uac70\ub9ac", None))
        self.label_state_mag.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.pb_mag_start.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #4CAF50; color: white; border-radius: 5px;", None))
        self.pb_mag_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.pb_mag_stop.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #F44336; color: white; border-radius: 5px;", None))
        self.pb_mag_stop.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.group_ss.setTitle(QCoreApplication.translate("MainWindow", u"SS", None))
        self.label_port_ss.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pb_ss.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.label_rpm_ss.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.label_motor_ss.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc120\ud0dd", None))
        self.rb_ss_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rb_ss_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.rb_ss_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.rb_ss_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.rb_ss_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_distance_ss.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\uac70\ub9ac", None))
        self.label_state_ss.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.pb_ss_start.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #4CAF50; color: white; border-radius: 5px;", None))
        self.pb_ss_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.pb_ss_stop.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #F44336; color: white; border-radius: 5px;", None))
        self.pb_ss_stop.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
    # retranslateUi

