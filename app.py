from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from sys import argv, exit
from modules.mainwindow import MainWindow
import os

if __name__ == '__main__':
    for dir_name in ['log', 'music', 'backup']:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    os.environ["PBR_VERSION"] = "4.0.2"
    app = QApplication(argv)
    win = MainWindow()
    serverName = 'ldy'
    socket = QLocalSocket()
    socket.connectToServer(serverName)
    # 如果连接成功，表明server已经存在，当前已有实例在运行
    if socket.waitForConnected(500):
        QMessageBox.warning(win, '警告', '该程序已经启动')
        app.quit()
    else:
        localServer = QLocalServer()  # 没有实例运行，创建服务器
        localServer.listen(serverName)
        win.show()
        exit(app.exec())
