# encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer
import sys
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 81, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 81, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 10, 81, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 10, 81, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 10, 81, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 10, 81, 91))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 110, 81, 91))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 110, 81, 91))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 110, 81, 91))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 110, 81, 91))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(370, 110, 81, 91))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 110, 81, 91))
        self.pushButton_12.setObjectName("pushButton_12")
        self.im_talked = QtWidgets.QCheckBox(self.centralwidget)
        self.im_talked.setEnabled(False)
        self.im_talked.setGeometry(QtCore.QRect(330, 330, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.im_talked.setFont(font)
        self.im_talked.setObjectName("im_talked")
        self.talk_now = QtWidgets.QLabel(self.centralwidget)
        self.talk_now.setGeometry(QtCore.QRect(10, 280, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.talk_now.setFont(font)
        self.talk_now.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.talk_now.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.talk_now.setObjectName("talk_now")
        self.time_now = QtWidgets.QLabel(self.centralwidget)
        self.time_now.setGeometry(QtCore.QRect(10, 220, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.time_now.setFont(font)
        self.time_now.setAlignment(QtCore.Qt.AlignCenter)
        self.time_now.setObjectName("time_now")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 700, 47, 13))
        self.label.setObjectName("label")
        self.my_role = QtWidgets.QLabel(self.centralwidget)
        self.my_role.setGeometry(QtCore.QRect(10, 530, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.my_role.setFont(font)
        self.my_role.setObjectName("my_role")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 370, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 390, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAFIA"))
        self.pushButton.setText(_translate("MainWindow", "Player1"))
        self.pushButton_2.setText(_translate("MainWindow", "Player2"))
        self.pushButton_3.setText(_translate("MainWindow", "Player3"))
        self.pushButton_4.setText(_translate("MainWindow", "Player4"))
        self.pushButton_5.setText(_translate("MainWindow", "Player5"))
        self.pushButton_6.setText(_translate("MainWindow", "Player6"))
        self.pushButton_7.setText(_translate("MainWindow", "Player7"))
        self.pushButton_8.setText(_translate("MainWindow", "Player8"))
        self.pushButton_9.setText(_translate("MainWindow", "Player9"))
        self.pushButton_10.setText(_translate("MainWindow", "Player10"))
        self.pushButton_11.setText(_translate("MainWindow", "Player11"))
        self.pushButton_12.setText(_translate("MainWindow", "Player12"))
        self.im_talked.setText(_translate("MainWindow", "Я сказал все что хотел"))
        self.talk_now.setText(_translate("MainWindow", "Сейчас говорит: {}"))
        self.time_now.setText(_translate("MainWindow", "ДЕНЬ"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.my_role.setText(_translate("MainWindow", "ВАША РОЛЬ: {}"))
        self.label_2.setText(_translate("MainWindow", "Все граждане говорят по 1 минуте 2 круга"))
        self.label_3.setText(_translate("MainWindow", "ГОВОРИТ ТОТ ТОЛЬКО ТОТ, ЧЕЙ НИК НАПИСАН ВЫШЕ"))


class Ui_ReadyWindow(object):
    def setupUi(self, ReadyWindow):
        ReadyWindow.setObjectName("ReadyWindow")
        ReadyWindow.resize(550, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReadyWindow.sizePolicy().hasHeightForWidth())
        ReadyWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ReadyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.im_ready = QtWidgets.QCheckBox(self.centralwidget)
        self.im_ready.setEnabled(True)
        self.im_ready.setGeometry(QtCore.QRect(410, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.im_ready.setFont(font)
        self.im_ready.setObjectName("im_talked")
        self.players_online = QtWidgets.QLabel(self.centralwidget)
        self.players_online.setGeometry(QtCore.QRect(20, 20, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.players_online.setFont(font)
        self.players_online.setAlignment(QtCore.Qt.AlignCenter)
        self.players_online.setObjectName("label")
        self.nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname.setGeometry(QtCore.QRect(240, 200, 261, 31))
        self.nickname.setInputMask("")
        self.nickname.setObjectName("lineEdit")
        ReadyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReadyWindow)
        QtCore.QMetaObject.connectSlotsByName(ReadyWindow)

    def retranslateUi(self, ReadyWindow):
        _translate = QtCore.QCoreApplication.translate
        ReadyWindow.setWindowTitle(_translate("ReadyWindow", "MAFIA (ready?)"))
        self.im_ready.setText(_translate("ReadyWindow", "Я готов"))
        self.players_online.setText(_translate("ReadyWindow", "Игроков в сети: {}"))
        self.nickname.setPlaceholderText(_translate("ReadyWindow", "ВАШЕ ИМЯ:"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class ReadyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReadyWindow()
        self.ui.setupUi(self)
        self.ui.im_ready.clicked.connect(self.check_ready)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.check_game_situation)

    def check_ready(self):
        if self.ui.nickname.text() != "":
            ans = requests.post(url, json={
                "title": "im ready for game", "id": my_client_id, "nickname": f"{self.ui.nickname.text().strip()}"
            }).json()
            if ans["error"] == "":
                self.ui.im_ready.setEnabled(False)

    def players_online_set(self, n):
        self.ui.players_online.setText(f"Игроков готово: {n}")

    def check_game_situation(self):
        ans = requests.get(url, json={"title": "current situation", "id": my_client_id}).json()["game"]
        game_situation, my_data = ans["game_situation"], ans["you"]
        if game_situation["title"] == "Waiting for start":
            ReadyWindow.players_online_set(game_situation["ready for game"])
        elif game_situation["title"] == "main_game":
            ReadyWindow.close()
            MainWindow.show()


def registration():
    return str(requests.get(url, json={"title": "im new player"}).json()["tech"]["id"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ReadyWindow = ReadyWindow()
    game_situation = {
        "title": "Waiting for start",
        "ready for game": 0
    }
    url = "http://127.0.0.1:5000/"
    my_client_id = registration()
    print(my_client_id)
    ReadyWindow.show()
    ReadyWindow.timer.start()
    sys.exit(app.exec())
