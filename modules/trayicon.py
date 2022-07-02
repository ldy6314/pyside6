from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QSystemTrayIcon, QMenu


class TrayIcon(QSystemTrayIcon):
    def __init__(self, ui, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = ui
        self.menu = QMenu()
        self.create_menu()
        icon = QIcon(QPixmap(":/pictures/icon.ico"))
        self.setIcon(icon)
        self.icon = self.MessageIcon()

    def create_menu(self):
        show_action2 = QAction("运行信息", self, triggered=self.show_msg)
        show_action3 = QAction("停止音乐", self, triggered=self.ui.stop_music)
        show_quit = QAction("退出", self, triggered=self.quit)
        self.menu.addAction(show_action2)
        self.menu.addAction(show_action3)
        self.menu.addAction(show_quit)
        self.setContextMenu(self.menu)

    def show_msg(self):
        self.showMessage("程序运行信息", "\n".join(self.ui.status_info()), self.icon)

    def show_window(self):
        self.ui.showNormal()
        self.ui.activateWindow()

    def quit(self):
        self.ui.exit()

    def on_icon_clicked(self, reason):
        if reason == 2 or reason == 3:
            if self.ui.isHidden():
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.show()
            else:
                self.ui.hide()