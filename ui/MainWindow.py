import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QRadioButton,
    QPushButton, QTableWidget
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import Panel
from utils import messages


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычмат Лаба 4")
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # === Заголовок окна ===
        self.lbl_title = QLabel("Вычмат Лаба 4")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.lbl_title)

        top_layout = QHBoxLayout()

        self.table_step = QTableWidget()
        self.table_step.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_step.setMinimumHeight(300)
        self.table_step.setMinimumWidth(400)
        top_layout.addWidget(self.table_step, 1)

        self.resultTable = QTableWidget()
        self.resultTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.resultTable.setMinimumHeight(300)
        self.resultTable.setMinimumWidth(400)
        top_layout.addWidget(self.resultTable, 1)

        main_layout.addLayout(top_layout, stretch=1)


        mid_layout = QHBoxLayout()

        self.dynamic_panel_widget = QWidget()
        self.dynamic_panel_layout = QVBoxLayout()
        self.dynamic_panel_widget.setLayout(self.dynamic_panel_layout)
        mid_layout.addWidget(self.dynamic_panel_widget, 1)

        self.canvas = MplCanvas(self, width=5, height=3, dpi=100)
        self.ax = self.canvas.ax
        mid_layout.addWidget(self.canvas, 2)

        main_layout.addLayout(mid_layout, stretch=2)

        self.lbl_bottom = QLabel(messages.getMessageByCode(0))
        self.lbl_bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_bottom.setMinimumHeight(30)
        main_layout.addWidget(self.lbl_bottom, stretch=0)

        self.dynamic_panel_layout.addWidget(Panel.renderPanel(self))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
