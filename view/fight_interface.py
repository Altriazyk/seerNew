from PyQt5.QtWidgets import QWidget, QGridLayout
from qfluentwidgets import TextEdit, BodyLabel, SimpleCardWidget, PushButton

from component.PetView import PetCard


class FightInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('fightInterface')
        self.fightDetail = FightView()
        self.startFight = PushButton("开始战斗")
        self.layout = QGridLayout()
        self.layout.addWidget(self.startFight, 0, 0)
        self.layout.addWidget(self.fightDetail, 1, 0, 1, 6)

        self.layout.setContentsMargins(10, 64, 10, 10)

        self.setLayout(self.layout)


class FightView(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QGridLayout()
        self.layout.setSpacing(0)

        self.userDetail = TextEdit()
        self.rivalDetail = TextEdit()
        self.userDetail.setFixedSize(300, 380)
        self.rivalDetail.setFixedSize(300, 380)
        self.rivalUidLabel = BodyLabel("对战赛尔id:")
        self.userPetInfo = ["5000", "NULL", "NULL", "NULL", "NULL", "NULL"]
        self.rivalPetInfo = ["5000", "NULL", "NULL", "NULL", "NULL", "NULL"]
        self.userCurrentPet = PetCard("NULL")
        self.userCurrentPet.imgWidget.setFixedSize(50, 50)
        self.userCurrentPet.setFixedSize(50, 50)
        self.rivalCurrentPet = PetCard("NULL")
        self.rivalCurrentPet.imgWidget.setFixedSize(50, 50)
        self.rivalCurrentPet.setFixedSize(50, 50)

        self.userPetView = QGridLayout()
        self.rivalPetView = QGridLayout()

        self.init_pet_view()

        self.layout.addWidget(self.userCurrentPet, 0, 0, 1, 1)
        self.layout.addWidget(self.rivalCurrentPet, 0, 8, 1, 1)
        self.layout.addLayout(self.userPetView, 2, 0, 1, 4)
        self.layout.addLayout(self.rivalPetView, 2, 5, 1, 4)
        self.layout.addWidget(self.rivalUidLabel, 1, 5)
        self.layout.addWidget(self.userDetail, 3, 0, 5, 6)
        self.layout.addWidget(self.rivalDetail, 3, 5, 5, 6)

        self.setFixedSize(620, 550)
        self.setLayout(self.layout)

    def init_pet_view(self):
        for i in range(6):
            if self.userPetInfo[i] != "NULL":
                _loc1_ = PetCard(self.userPetInfo[i])
                _loc1_.imgWidget.setFixedSize(50, 50)
                _loc1_.setFixedSize(50, 50)
            else:
                _loc1_ = PetCard("NULL")
                _loc1_.imgWidget.setFixedSize(50, 50)
                _loc1_.setFixedSize(50, 50)
            self.userPetView.addWidget(_loc1_, 0, i)
        for i in range(6):
            if self.rivalPetInfo[i] != "NULL":
                _loc1_ = PetCard(self.userPetInfo[i])
                _loc1_.imgWidget.setFixedSize(50, 50)
                _loc1_.setFixedSize(50, 50)
            else:
                _loc1_ = PetCard("NULL")
                _loc1_.imgWidget.setFixedSize(50, 50)
                _loc1_.setFixedSize(50, 50)
            self.rivalPetView.addWidget(_loc1_, 0, i)

    def change_rival_uid(self, data):
        self.rivalUidLabel.setText("对战赛尔id:" + str(int(data.replace(' ', ''), 16)))
