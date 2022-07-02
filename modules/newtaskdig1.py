# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newtaskdig1.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(416, 270)
        Dialog.setModal(False)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 10, 391, 241))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Algerian"])
        font.setPointSize(10)
        self.label_3.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.layoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_2.addWidget(self.checkBox_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_6 = QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_5.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout_5.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.horizontalLayout_5.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.layoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.horizontalLayout_5.addWidget(self.checkBox_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setWrapping(True)
        self.spinBox.setMaximum(23)
        self.spinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spinBox.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setWrapping(True)
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setWrapping(True)
        self.spinBox_3.setMaximum(59)
        self.spinBox_3.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spinBox_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u94c3\u58f0\u540d\u79f0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u94c3\u58f0\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u5e38\u89c4\u94c3\u58f0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u8bfe\u95f4\u6d3b\u52a8", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u5468\u672b\u94c3\u58f0", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u5b89\u5168\u6559\u80b2", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u5176\u4ed6\u94c3\u58f0", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u9009\u62e9", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u9009\u62e9", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u4e00", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u4e8c", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u4e09", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u56db", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u4e94", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u516d", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"\u661f\u671f\u65e5", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"\u5168\u9009", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"\u5de5\u4f5c\u65e5", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e\u65f6\u95f4", None))
    # retranslateUi

