from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLineEdit,
    QLabel, QPushButton, QButtonGroup
)
from PyQt6.QtGui import QPixmap
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO

from utils import FieldParser
from utils.Utils import predefined_functions


class renderPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # === Левая колонка: Выбор функции ===
        col_left = QVBoxLayout()
        self.eq_group = QButtonGroup(self)

        self.rb_eq1 = QRadioButton()
        self.rb_eq2 = QRadioButton()
        self.rb_eq3 = QRadioButton()
        self.rb_eq4 = QRadioButton()
        self.rb_eq5 = QRadioButton()
        self.rb_eq6 = QRadioButton()
        self.rb_eq1.setChecked(True)

        self.eq_group.addButton(self.rb_eq1)
        self.eq_group.addButton(self.rb_eq2)
        self.eq_group.addButton(self.rb_eq3)
        self.eq_group.addButton(self.rb_eq4)
        self.eq_group.addButton(self.rb_eq5)
        self.eq_group.addButton(self.rb_eq6)

        self.add_formula_row(col_left, self.rb_eq1, predefined_functions[1].text)
        self.add_formula_row(col_left, self.rb_eq2, predefined_functions[2].text)
        self.add_formula_row(col_left, self.rb_eq3, predefined_functions[3].text)
        self.add_formula_row(col_left, self.rb_eq4, predefined_functions[4].text)
        self.add_formula_row(col_left, self.rb_eq5, predefined_functions[5].text)
        self.add_formula_row(col_left, self.rb_eq6, predefined_functions[6].text)

        layout.addLayout(col_left, 3)



        # === Правая колонка: Поля ввода ===
        col_right = QVBoxLayout()

        self.edit_file_input = QLineEdit()
        self.edit_left_bound = QLineEdit()
        self.edit_right_bound = QLineEdit()
        self.edit_h = QLineEdit()
        self.edit_file_output = QLineEdit()

        col_right.addWidget(QLabel("Входной файл:"))
        col_right.addWidget(self.edit_file_input)
        col_right.addWidget(QLabel("Левая граница (a):"))
        col_right.addWidget(self.edit_left_bound)
        col_right.addWidget(QLabel("Правая граница (b):"))
        col_right.addWidget(self.edit_right_bound)
        col_right.addWidget(QLabel("Шаг (h):"))
        col_right.addWidget(self.edit_h)
        col_right.addWidget(QLabel("Выходной файл:"))
        col_right.addWidget(self.edit_file_output)

        self.btn_solve = QPushButton("Решить")
        self.btn_solve.clicked.connect(lambda: self.solve(main_window))
        col_right.addWidget(self.btn_solve)

        layout.addLayout(col_right, 3)

    def add_formula_row(self, layout, radio_button, latex_expr):
        row = QHBoxLayout()
        row.addWidget(radio_button)

        label = QLabel()
        pix = self.render_latex(rf"${latex_expr}$")
        label.setPixmap(pix)
        row.addWidget(label)

        layout.addLayout(row)

    def render_latex(self, latex_str):
        fig, ax = plt.subplots(figsize=(1.75, 0.20), dpi=100)
        ax.axis("off")
        ax.text(0.5, 0.5, latex_str, ha='center', va='center', fontsize=10)

        buffer = BytesIO()
        fig.tight_layout(pad=0)
        canvas = FigureCanvas(fig)
        canvas.print_png(buffer)
        plt.close(fig)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue(), 'PNG')
        return pixmap

    def solve(self, main_window):

        if self.rb_eq1.isChecked():
            eq_num = 1
        elif self.rb_eq2.isChecked():
            eq_num = 2
        elif self.rb_eq3.isChecked():
            eq_num = 3
        elif self.rb_eq4.isChecked():
            eq_num = 4
        elif self.rb_eq5.isChecked():
            eq_num = 5
        else:
            eq_num = 6


        FieldParser.parse_data(
            main_window,
            eq_num,
            self.edit_file_input.text(),
            self.edit_file_output.text(),
            self.edit_left_bound.text(),
            self.edit_right_bound.text(),
            self.edit_h.text(),
        )