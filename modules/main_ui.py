# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)
from modules.myqslider import MySlider
from modules import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 700)
        icon = QIcon()
        icon.addFile(u":/pictures/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(36)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(17)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(180, 0))
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(240, 16777215))
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.themeChangeBox = QComboBox(self.centralwidget)
        self.themeChangeBox.setObjectName(u"themeChangeBox")

        self.horizontalLayout_2.addWidget(self.themeChangeBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(170, 0))
        self.label_9.setMaximumSize(QSize(200, 16777215))
        self.label_9.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.next_time_label = QLabel(self.centralwidget)
        self.next_time_label.setObjectName(u"next_time_label")
        self.next_time_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.next_time_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.next_name_label = QLabel(self.centralwidget)
        self.next_name_label.setObjectName(u"next_name_label")
        self.next_name_label.setFont(font1)

        self.horizontalLayout_11.addWidget(self.next_name_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(15)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"font: 14pt \"\u65b9\u6b63\u59da\u4f53\";")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.musisc_name_label = QLabel(self.groupBox_4)
        self.musisc_name_label.setObjectName(u"musisc_name_label")

        self.horizontalLayout_6.addWidget(self.musisc_name_label)

        self.pause_play_button = QToolButton(self.groupBox_4)
        self.pause_play_button.setObjectName(u"pause_play_button")
        icon1 = QIcon()
        icon1.addFile(u":/pictures/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_play_button.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.pause_play_button)

        self.current_time_label = QLabel(self.groupBox_4)
        self.current_time_label.setObjectName(u"current_time_label")

        self.horizontalLayout_6.addWidget(self.current_time_label)

        self.music_Slider = MySlider(self.groupBox_4)
        self.music_Slider.setObjectName(u"music_Slider")
        self.music_Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.music_Slider)

        self.totle_time_label = QLabel(self.groupBox_4)
        self.totle_time_label.setObjectName(u"totle_time_label")

        self.horizontalLayout_6.addWidget(self.totle_time_label)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 10, 5, 10)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_1 = QPushButton(self.tab)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.groupBox_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.toolButton_2 = QToolButton(self.groupBox_2)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_4.addWidget(self.toolButton_2)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(15)
        font4.setBold(False)
        self.groupBox_3.setFont(font4)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.groupBox_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_5.addWidget(self.pushButton_10)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser_2 = QTextBrowser(self.tab_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_6.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.verticalLayout_3.setStretch(4, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.statusbar.setFont(font5)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6821\u56ed\u5e7f\u64ad\u64ad\u653e\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u6821\u56ed\u5e7f\u64ad\u64ad\u653e\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4\uff1a", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u72b6\u6001\uff1a", None))
        self.label_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u6b21\u54cd\u94c3\u65f6\u95f4:", None))
        self.next_time_label.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u54cd\u94c3\u540d\u79f0\uff1a", None))
        self.next_name_label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u94c3\u58f0\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u63a7\u5236", None))
        self.musisc_name_label.setText("")
        self.pause_play_button.setText("")
        self.current_time_label.setText("")
        self.totle_time_label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u4efb\u52a1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4efb\u52a1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e34\u65f6\u64ad\u653e", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u64ad\u653e", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u9634\u96e8\u5929\u6a21\u5f0f", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u4f11\u6a21\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u516d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u65e5", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8865", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e00", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e8c", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e09", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u56db", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u661f\u671f\u4e94", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8bfe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5217\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u6539\u97f3\u4e50", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6539\u6210", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u4fee\u6539", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u64cd\u4f5c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6b63\u8def\u5f84", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4efb\u52a1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u64cd\u4f5c", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html ><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body >\n"
"<p><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u65e5\u5fd7", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html style=\"font-size:16px\"><head><meta name=\"qrichtext\" content=\"1\" /></head><body>\n"
"<p ><span >\u8f6f\u4ef6\u4f5c\u8005\uff1a\u86c7\u8c61 </span></p>\n"
"<p ><span >\u4f7f\u7528\u573a\u666f\uff1a\u7ba1\u7406\u6821\u56ed\u94c3\u58f0\uff0c\u53ef\u4ee5\u81ea\u5b9a\u4e49\u65f6\u95f4\u548c\u64ad\u653e\u94c3""\u58f0\uff0c\u4e00\u952e\u9634\u96e8\u5929\u6a21\u5f0f\u5207\u6362\uff0c\u4e00\u952e\u8c03\u4f11\u6a21\u5f0f\u94c3\u58f0\u8c03\u6574\uff0c\u6279\u91cf\u4fee\u6539\u94c3\u58f0\uff0c\u6279\u91cf\u5bfc\u5165\uff0c\u5bfc\u51fa\uff0c\u6821\u56ed\u5e7f\u64ad\u7ba1\u7406\u5458\u7684\u798f\u97f3\uff0c \u4e5f\u53ef\u4ee5\u7528\u4e8e\u5176\u4ed6\u573a\u666f\u7684\u5b9a\u65f6\u64ad\u653e</span>                                                </p>\n"
"<p ><span >\u8054\u7cfb\u65b9\u5f0f\uff1a</span></p>\n"
"<p><span>QQ\uff1a497661660</span>""</p>\n"
"<p><span \u90ae\u7bb1\uff1a497661660@qq.com</span></p>\n"
"<p><span>\u7248\u6743\u7533\u660e\uff1a\u672c\u8f6f\u4ef6\u4ec5\u9650\u975e\u5546\u4e1a\u7528\u9014\u514d\u8d39\u4f7f\u7528\uff0c\u7981\u6b62\u4ed6\u4eba\u4f5c\u4e3a\u5546\u4e1a\u7528\u9014\uff0c\u5982\u6709\u610f\u89c1\u548c\u5efa\u8bae\u53ef\u4ee5\u901a\u8fc7\u4e0a\u9762\u7684\u8054\u7cfb\u65b9\u5f0f\u8054\u7cfb\u4f5c\u8005</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
    # retranslateUi

