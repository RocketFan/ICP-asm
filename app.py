import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QScatterSeries
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("ICP-asm")
        self.resize(600, 400)

        self.init_chart()
        self.setCentralWidget(self.chart_view)
        chart = self.chart_view.chart()
        series = QLineSeries()
        series.append([QPoint(20, 30), QPoint(100, 200)])
        chart.addSeries(series)

    def init_chart(self):
        series = QLineSeries()

        data = [
            QPoint(0, 6),
            QPoint(9, 4),
            QPoint(15, 20),
            QPoint(9, 12),
            QPoint(20, 25)
        ]

        series.append(data)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)

        self.chart_view = QChartView(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()