import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar
from git import Repo, RemoteProgress
from clonagem import *


class ClonarRepositorio(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnUrl.clicked.connect(self.clone)

    def clone(self):
        url = self.inputUrl.text()
        nome = self.novoNome.text()
        if nome == '':
            nome = url.split('/')[-1]
        Repo.clone_from(url, nome)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cr = ClonarRepositorio()
    cr.show()
    qt.exec_()
