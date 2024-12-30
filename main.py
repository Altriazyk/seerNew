import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


from view.main_windows import Window

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    # setTheme(Theme.DARK)
    w = Window()
    w.show()
    app.exec_()
