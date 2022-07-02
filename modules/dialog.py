from PySide6.QtWidgets import QDialog, QFileDialog
from modules.newtaskdig1 import Ui_Dialog
from modules.timeparse import *
import os


def get_root_path():
    site_root = os.path.dirname(os.path.realpath(__file__))
    parent_root = os.path.abspath(os.path.join(site_root, os.pardir))
    return parent_root


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.chk_list = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                         self.checkBox_6, self.checkBox_7]
        self.checkBox_8.stateChanged.connect(lambda: self.multi_select(self.checkBox_8, (0, 7)))
        self.checkBox_9.stateChanged.connect(lambda: self.multi_select(self.checkBox_9, (0, 5)))
        self.toolButton.clicked.connect(self.set_file)

    def get_value(self):
        bell_name = self.lineEdit_2.text()
        bell_type = self.comboBox.currentText()
        file = self.lineEdit.text()
        weekdays_value = 0
        time_value = self.spinBox.value() * 3600 + self.spinBox_2.value() * 60 + self.spinBox_3.value()
        for i in zip(self.chk_list, range(7)):
            if i[0].checkState():
                weekdays_value += 1 << i[1]
        return bell_name, bell_type, file, weekdays_value, time_value

    def multi_select(self, checkbox, rg):
        state = checkbox.isChecked()
        for i in range(rg[0], rg[1]):
            self.chk_list[i].setChecked(state)

    def set_value(self, value=("", "常规铃声", "", 0, 0)):
        # bell_name, bell_type, file, weekdays_value, time_value
        self.lineEdit_2.setText(value[0])
        self.comboBox.setCurrentText(value[1])
        self.lineEdit.setText(value[2])
        weekdays = parse_to_weekdays(value[3])
        h, m, s = parse_to_time(value[4])
        for checkbox in self.chk_list:
            checkbox.setChecked(False)
        for i in weekdays:
            self.chk_list[i - 1].setChecked(True)
        self.spinBox.setValue(h)
        self.spinBox_2.setValue(m)
        self.spinBox_3.setValue(s)
        self.checkBox_9.setChecked(False)
        self.checkBox_8.setChecked(False)

    def set_file(self):
        file_name, tp = QFileDialog.getOpenFileName(dir=get_root_path() + '/music', filter=
                                                    "Music Files (*.mp3)")
        self.lineEdit.setText(file_name)
