# This is a demo to test packaging
from sys import argv

import numpy as np
from PyQt6 import QtGui
from PyQt6.QtCharts import QChart, QChartView, QLineSeries
from PyQt6.QtGui import QPainter, QAction, QColor, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMenuBar,
    QMenu,
    QFrame,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSlider,
    QLabel,
    QComboBox,
)
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication
import sys
from data_handler import Data
from neural_network import NeuralNetwork
from graphics import MainWindow
from variables import Variables
from sklearn.preprocessing import minmax_scale


class MainWindow(QMainWindow):

    # def __init__(self, plot):
    #     self.setup_chart(plot)

    def start(self):
        self.resize(1000, 800)
        self.setup_ui()
        self.setWindowTitle("Whaaale")
        self.show()

    def setup_ui(self):
        layout = QGridLayout()
        upper_panel = QHBoxLayout()
        lower_panel = QHBoxLayout()
        layout.addLayout(upper_panel, 0, 0)
        layout.addLayout(lower_panel, 1, 0)

        # ****** Elements of layout ******

        # ****** Buttons ******

        self.predict_button = QPushButton(self)
        self.predict_button.setText("Predict stock market!")
        self.predict_button.clicked.connect(self.predict_button_click)

        # ******** Image *********

        self.image = QPixmap("plots/AAPL.png")
        self.label_plot = QLabel()
        self.label_plot.setPixmap(self.image)
        self.label_plot.setScaledContents(True)

        # ****** Menu ******

        self.select_mode = QComboBox()
        # self.select_mode.addItem("Google")
        # self.select_mode.addItem("Apple")
        for v in Variables.company_name:
            self.select_mode.addItem(v)

        # self.label_band1 = QLabel("Band #1", self)
        # self.label_band1.setFixedSize(40, 20)
        # frame1 = QFrame(self)
        # frame1.setFrameShape(QFrame.Shape.StyledPanel)
        # frame1.setLineWidth(3)
        # frame1.setFixedSize(30, 30)
        # frame1.setStyleSheet("background-color:red")

        # self.label_band2 = QLabel("Band #2", self)
        # self.label_band2.setFixedSize(40, 20)
        # frame2 = QFrame(self)
        # frame2.setFrameShape(QFrame.Shape.StyledPanel)
        # frame2.setLineWidth(3)
        # frame2.setFixedSize(30, 30)
        # frame2.setStyleSheet("background-color:green")

        # self.label_band3 = QLabel("Band #3", self)
        # self.label_band3.setFixedSize(40, 20)
        # frame3 = QFrame(self)
        # frame3.setFrameShape(QFrame.Shape.StyledPanel)
        # frame3.setLineWidth(3)
        # frame3.setFixedSize(30, 30)
        # frame3.setStyleSheet("background-color:blue")

        # ****** Add elements to layout ******

        """Change the order of toolbars; maybe select_point/area to toolbar1?"""

        lower_panel.addWidget(self.select_mode)
        lower_panel.addWidget(self.predict_button)
        upper_panel.addWidget(self.label_plot)
        # upper_panel.addWidget(self.chart_view)

        # ****** Widget placing ******
        widget = QWidget()
        widget.resize(100, 100)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # ****** Menu bar ******
        self._createMenuBar()

    # def setup_chart(self, plot):
    #     series = QLineSeries()

    #     # series.append(0, 6)
    #     # series.append(2, 4)
    #     # l = np.array(
    #     #     [[1, 3.1], [2, 7.22], [3, 10], [4, 11.12], [5, 13], [6, 17], [7, 18], [8, 20]]
    #     # )
    #     i=1
    #     for p in plot:
    #         series.append(i, p)
    #         i = i + 1

    #     chart = QChart()
    #     chart.legend().hide()
    #     chart.addSeries(series)
    #     chart.createDefaultAxes()
    #     chart.setTitle("Simple line chart example")

    #     self.chart_view = QChartView(chart)
    #     self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

    #     return self.chart_view
    #     # self.chart_view = chart_view
    #     # self.setCentralWidget(self.chart_view)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = menuBar.addMenu("&File")
        editMenu = menuBar.addMenu("&View")
        helpMenu = menuBar.addMenu("&Help")

        # File menu
        action_open = QAction("Open", self)
        action_open.triggered.connect(self.open_click)
        action_exit = QAction("Exit", self)
        action_exit.triggered.connect(self.exit_click)
        fileMenu.addAction(action_open)
        fileMenu.addAction(action_exit)

        # Help menu
        action_help = QAction("Help", self)
        action_help.triggered.connect(self.help_click)
        helpMenu.addAction(action_help)

    """Methods responsible for handling interaction with buttons etc."""

    def predict_button_click(self):
        print("clicked predict button!")
        # future_prices = network.predict_prices(data_prediction)
        # print_results(future_prices, data_result, highest_price)


    def open_click(self):
        print("clicked open in menu bar")

    def help_click(self):
        print("clicked help in menu bar")

    def exit_click(self):
        # Dedicated function cuz there is no possibility
        # to connect sys.exit() directly to button in menu bar
        print("clicked exit in menu bar")
        # sys.exit() to definitely terminate the program
        sys.exit()

def print_results(future_price, data_result, highest_price):
    # print(data_result)
    data_result = minmax_scale(data_result, feature_range=(0,highest_price))
    future_price = minmax_scale(future_price, feature_range=(0,highest_price))
    plt.plot(future_price, 'r', data_result, 'b')
    # plt.title(("Real and predicted price of " + company_name + " stock"))
    plt.title(("Real and predicted price of stock"))
    plt.xlabel('Time [days]')
    plt.ylabel('Price [$]')
    plt.legend(['Predicted price', 'Real price'])
    # plt.figure(dpi=300)
    # plt.plot(data_result)
    # plt.show()
    plt.savefig('plots/'+Variables.company_name)

def main():
    chosen_data = Data()
    highest_price = chosen_data.prepare_arrays()
    data_prediction, data_result = chosen_data.reshape_data()

    network = NeuralNetwork()
    network.build_model(data_prediction)
    network.evaluate_model(data_prediction, data_result)
    network.save_model('model2')
    # network.load_model('model1')
    # future_prices = network.predict_prices(data_prediction)
    # print_results(future_prices, data_result, highest_price)

    a = QApplication(argv)
    main_window = MainWindow()
    main_window.start()
    a.exec()


if __name__ == "__main__":
    main()