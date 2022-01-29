from email.charset import QP
import sys
import time
import utils
import numpy as np

from threading import Thread

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtGui import QPainter

from icp import ICP
from icp_asm import ICPAsm


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("ICP-asm")
        self.resize(600, 400)

        self.init_icp()

        self.init_chart()
        self.setCentralWidget(self.chart_view)
        self.next_button()


    def init_chart(self):
        chart = QChart()
        chart.legend().hide()

        self.chart_view = QChartView(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

    def next_button(self):
        self.next_button = QPushButton(self)
        self.next_button.setText("Next")
        
        self.next_button.clicked.connect(lambda _: self.icp.next(self.chart_view.chart()))

    def init_icp(self):
        R = utils.get_2D_R(np.radians(60))
        T = utils.get_2D_T(0, 0)
        func = utils.get_2D_func([0.00003, 0.0002, 0, 0.001, 1])

        pc_1 = np.array([[x, func(x), 1] for x in range(-40, 25, 1)])
        pc_2 = np.dot(np.dot(pc_1, R.transpose()), T.transpose())
        self.icp = ICP(pc_1[:, :2], pc_2[:, :2])


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
