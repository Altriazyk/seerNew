import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout
from qfluentwidgets import SimpleCardWidget, ImageLabel


class PetCard(SimpleCardWidget):
    def __init__(self, petId, parent=None):
        super().__init__(parent=parent)
        self.headAddress = "http://seerh5.61.com/resource/assets/pet/head/"
        self.imgWidget = ImageLabel()
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)

        self.load_image_from_url(petId)
        self.imgWidget.setFixedSize(80, 80)
        self.vBoxLayout.addWidget(self.imgWidget)

    def load_image_from_url(self, petId):
        if petId != "NULL":
            url = self.headAddress + petId + ".png"
            try:
                # 从 URL 下载图片
                response = requests.get(url)
                image_data = response.content

                # 将图片数据加载为 QPixmap
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)

                # 设置 QLabel 显示图片
                self.imgWidget.setPixmap(pixmap)
                self.imgWidget.setScaledContents(True)  # 缩放图片以适应 QLabel 大小
                self.imgWidget.setFixedSize(80, 80)
            except Exception as e:
                print("Error loading image:", e)
        else:
            self.imgWidget.setPixmap(None)
            self.imgWidget.setFixedSize(80, 80)