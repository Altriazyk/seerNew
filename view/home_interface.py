from datetime import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidgetItem, QTableWidgetItem, QHeaderView
from qfluentwidgets import LineEdit, PasswordLineEdit, PushButton, ListWidget, PlainTextEdit, TextEdit, TableWidget

from core.client import webSocketClient
from core.login import loginGame


class HomeInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('homeInterface')
        self.loginBtn = None
        self.layout = None
        self.account = None
        self.password = None
        self.messageList = None
        self.initHomeView()

    def initHomeView(self):
        self.layout = QGridLayout()
        self.account = LineEdit()
        self.password = PasswordLineEdit()
        self.loginBtn = PushButton('开始登录')
        self.messageList = TableWidget()
        self.init_table()

        self.loginBtn.clicked.connect(self.login_btn_clicked)
        webSocketClient.new_message.connect(self.get_new_message)
        self.layout.setContentsMargins(10, 64, 10, 10)
        self.layout.addWidget(self.account, 0, 0)
        self.layout.addWidget(self.password, 1, 0)
        self.layout.addWidget(self.loginBtn, 2, 0)
        self.layout.addWidget(self.messageList, 3, 0)
        self.setLayout(self.layout)

    def login_btn_clicked(self):
        loginGame(self.account.text(), self.password.text())

    def get_new_message(self, message):
        formatted_now = datetime.now().strftime("%m-%d %H:%M:%S")
        parts = message.split('|')
        row_position = self.messageList.rowCount()
        self.messageList.insertRow(row_position)
        self.messageList.setItem(row_position, 0, QTableWidgetItem(formatted_now))
        for i, part in enumerate(parts):
            self.messageList.setItem(row_position, i+1, QTableWidgetItem(part))

    def init_table(self):
        # 启用边框并设置圆角
        self.messageList.setBorderVisible(True)
        self.messageList.setBorderRadius(8)

        self.messageList.setWordWrap(False)
        self.messageList.setColumnCount(4)
        # 固定列宽
        self.messageList.setColumnWidth(0, 100)
        self.messageList.setColumnWidth(1, 100)
        self.messageList.setColumnWidth(2, 100)
        self.messageList.setColumnWidth(3, 500)

        self.messageList.setHorizontalHeaderLabels(['时间','类型', '命令号', '包体'])
        self.messageList.verticalHeader().hide()

