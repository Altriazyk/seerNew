# coding:utf-8
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import (FluentBackgroundTheme, SplitFluentWindow)
from qfluentwidgets import FluentIcon as FIF

from .fight_interface import FightInterface
from .home_interface import HomeInterface


class Window(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.homeInterface = HomeInterface()
        self.fightInterface = FightInterface()
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.WIFI, '主页')
        self.addSubInterface(self.fightInterface, FIF.CALORIES, '巅峰')
        self.navigationInterface.addSeparator()

        self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 700)
        # 获取当前工作目录
        current_dir = os.path.dirname(__file__)
        # 设置窗口图标为绝对路径下的图标
        icon_path = os.path.join(current_dir, '../resource/image/logo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('智能赛尔')
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setCustomBackgroundColor(*FluentBackgroundTheme.DEFAULT_BLUE)
