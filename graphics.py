from sys import argv

import numpy as np
from PyQt6 import QtGui
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
from variables import Variables


class MainWindow(QMainWindow):

    def start(self):
        self.resize(1000, 800)
        self.setup_ui()
        self.setWindowTitle("Stock price prediction")
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
        # self.predict_button.clicked.connect(self.predict_button_click)

        # ******** Image *********

        self.image = QPixmap("plots/AAPL.png")
        self.label_plot = QLabel()
        self.label_plot.setPixmap(self.image)
        self.label_plot.setScaledContents(True)

        # ****** Menu ******

        self.select_mode = QComboBox()
        for v in Variables.company_name:
            self.select_mode.addItem(v)
        self.select_mode.currentIndexChanged.connect(self.update_image)

        # ****** Add elements to layout ******

        """Change the order of toolbars; maybe select_point/area to toolbar1?"""

        lower_panel.addWidget(self.select_mode)
        # lower_panel.addWidget(self.predict_button)
        upper_panel.addWidget(self.label_plot)
        # upper_panel.addWidget(self.chart_view)

        # ****** Widget placing ******
        widget = QWidget()
        widget.resize(100, 100)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # ****** Menu bar ******
        self._createMenuBar()

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = menuBar.addMenu("&File")
        editMenu = menuBar.addMenu("&View")
        helpMenu = menuBar.addMenu("&Help")

        # File menu
        # action_open = QAction("Open", self)
        # action_open.triggered.connect(self.open_click)
        # action_exit = QAction("Exit", self)
        # action_exit.triggered.connect(self.exit_click)
        # fileMenu.addAction(action_open)
        # fileMenu.addAction(action_exit)

        # # Help menu
        # action_help = QAction("Help", self)
        # action_help.triggered.connect(self.help_click)
        # helpMenu.addAction(action_help)

    """Methods responsible for handling interaction with buttons etc."""

    def update_image(self, index):
        # get the text of the selected item
        selected_item_text = self.select_mode.currentText()

        # load the corresponding image and set it to the QLabel
        if selected_item_text == Variables.company_name[0]:
            pixmap = QPixmap('plots/' + Variables.company_name[0] + '.png')
            self.label_plot.setPixmap(pixmap)
        elif selected_item_text == Variables.company_name[1]:
            pixmap = QPixmap('plots/' + Variables.company_name[1] + '.png')
            self.label_plot.setPixmap(pixmap)
        elif selected_item_text == Variables.company_name[2]:
            pixmap = QPixmap('plots/' + Variables.company_name[2] + '.png')
            self.label_plot.setPixmap(pixmap)
        elif selected_item_text == Variables.company_name[3]:
            pixmap = QPixmap('plots/' + Variables.company_name[3] + '.png')
            self.label_plot.setPixmap(pixmap)
        elif selected_item_text == Variables.company_name[4]:
            pixmap = QPixmap('plots/' + Variables.company_name[4] + '.png')
            self.label_plot.setPixmap(pixmap)
        elif selected_item_text == Variables.company_name[5]:
            pixmap = QPixmap('plots/' + Variables.company_name[5] + '.png')
            self.label_plot.setPixmap(pixmap)
