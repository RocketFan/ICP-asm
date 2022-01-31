import sys
import platform
import os
import time

import psutil
import utils
import numpy as np

from threading import Thread

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QSlider, QCheckBox
from PyQt5.QtChart import QChart, QChartView, QValueAxis
from PyQt5.QtGui import QPainter, QIntValidator
from PyQt5.QtCore import Qt, QRectF

from icp import ICP
from icp_asm import ICPAsm


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("ICP-asm")
        self.resize(600, 400)

        self.init_chart()
        self.next_button()
        self.reset_button()
        self.config_section()

        self.init_icp()


    def init_chart(self):
        chart = QChart()
        chart.legend().hide()
        chart.setPlotArea(QRectF(0, 0, 300, 300))

        chart.addAxis(QValueAxis(), Qt.AlignBottom)
        chart.addAxis(QValueAxis(), Qt.AlignLeft)
        chart.axisX().setVisible()
        chart.axisY().setVisible()

        self.chart_view = QChartView(chart, self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setGeometry(0, 40, 400, 300)

        self.counter_label = QLabel(self)
        self.counter_label.setText("Iteration: 0")
        self.counter_label.setGeometry(220, 0, 100, 30)

    def next_button(self):
        next_button = QPushButton(self)
        next_button.setText("Next")
        next_button.setGeometry(0, 0, 100, 30)
        
        next_button.clicked.connect(self.next)

    def reset_button(self):
        reset_button = QPushButton(self)
        reset_button.setText("Reset")
        reset_button.setGeometry(110, 0, 100, 30)

        reset_button.clicked.connect(self.reset)

    def config_section(self):
        x = 400
        width = 100
        height = 30
        only_int = QIntValidator()

        self.input_angle = QLineEdit(self)
        self.input_angle.setGeometry(x, 50, width, height)
        self.input_angle.setValidator(only_int)
        self.input_angle.setText("60")
        label_angle = QLabel(self)
        label_angle.setText("Angle:")
        label_angle.setGeometry(self.input_angle.x() - 55, self.input_angle.y(), 50, height)

        self.input_x = QLineEdit(self)
        self.input_x.setGeometry(x, 100, width, height)
        self.input_x.setValidator(only_int)
        self.input_x.setText("100")
        label_x = QLabel(self)
        label_x.setText("X:")
        label_x.setGeometry(self.input_x.x() - 55, self.input_x.y(), 50, height)

        self.input_y = QLineEdit(self)
        self.input_y.setGeometry(x, 150, width, height)
        self.input_y.setValidator(only_int)
        self.input_y.setText("0")
        label_y = QLabel(self)
        label_y.setText("Y:")
        label_y.setGeometry(self.input_y.x() - 55, self.input_y.y(), 50, height)

        self.slider_threads = QSlider(Qt.Horizontal, self)
        self.slider_threads.setGeometry(x - 25, 200, width + 50, height)
        self.slider_threads.setMinimum(1)
        self.slider_threads.setMaximum(61)
        self.slider_threads.setSingleStep(1)
        self.slider_threads.setValue(psutil.cpu_count(logical=False))
        print("Cores: ", self.slider_threads.value())

        label_threads = QLabel(self)
        label_threads.setText(f"Threads: {self.slider_threads.value()}")
        label_threads.setGeometry(self.slider_threads.x() + 10, self.slider_threads.y() + 20, 80, height)
        self.slider_threads.valueChanged.connect(lambda _: label_threads.setText(f"Threads: {self.slider_threads.value()}"))

        self.checkbox_asm = QCheckBox(self)
        self.checkbox_asm.setText("Use ASM")
        self.checkbox_asm.setGeometry(x, 300, width, height)

    def get_config_dict(self):
        config = {
            "angle": int(self.input_angle.text()),
            "x": int(self.input_x.text()),
            "y": int(self.input_y.text()),
            "threads": self.slider_threads.value(),
            "is_asm": self.checkbox_asm.isChecked()
        }

        return config

    def next(self):
        self.icp.next(self.chart_view.chart())
        self.counter_label.setText(f"Iteration: {self.icp.iteration}")

    def reset(self):
        self.init_icp()
        self.counter_label.setText("Iteration: 0")

    def init_icp(self):
        config = self.get_config_dict()
        
        R = utils.get_2D_R(np.radians(config["angle"]))
        T = utils.get_2D_T(config["x"], config["y"])
        func = utils.get_2D_func([0.00003, 0.0002, 0, 0.001, 1])

        pc_1 = np.array([[x, func(x), 1] for x in range(-40, 25, 1)])
        pc_2 = np.dot(np.dot(pc_1, R.transpose()), T.transpose())

        if(config["is_asm"]):
            self.icp = ICPAsm(pc_1[:, :2], pc_2[:, :2], config["threads"])
        else:
            self.icp = ICP(pc_1[:, :2], pc_2[:, :2], config["threads"])

        self.icp.visualize_2D_results(self.chart_view.chart())


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
