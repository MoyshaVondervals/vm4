from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QSlider, QPushButton, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt
from utils import FieldParser, messages


class renderPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.x_inputs = []
        self.y_inputs = []

        layout = QVBoxLayout(self)

        # === Поля ввода файлов ===
        self.edit_file_input = QLineEdit()
        self.edit_file_output = QLineEdit()

        layout.addWidget(QLabel("Входной файл:"))
        layout.addWidget(self.edit_file_input)
        layout.addWidget(QLabel("Выходной файл:"))
        layout.addWidget(self.edit_file_output)

        # === Ползунок ===
        slider_layout = QHBoxLayout()
        slider_label = QLabel("Количество точек:")
        self.slider_value_label = QLabel("8")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(8)
        self.slider.setMaximum(12)
        self.slider.setValue(8)
        self.slider.valueChanged.connect(self.update_input_fields)

        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_value_label)
        layout.addLayout(slider_layout)

        # === Контейнер с полями ввода ===
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.inputs_container = QWidget()
        self.inputs_layout = QVBoxLayout(self.inputs_container)
        self.scroll.setWidget(self.inputs_container)

        layout.addWidget(self.scroll)

        # === Кнопка ===
        self.btn_solve = QPushButton("Решить")
        self.btn_solve.clicked.connect(self.solve)
        layout.addWidget(self.btn_solve)

        # === Инициализация полей ввода ===
        self.update_input_fields(8)

    def update_input_fields(self, value):
        self.slider_value_label.setText(str(value))

        old_x_values = [x.text() for x in self.x_inputs]
        old_y_values = [y.text() for y in self.y_inputs]

        for i in reversed(range(self.inputs_layout.count())):
            widget = self.inputs_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.x_inputs = []
        self.y_inputs = []

        for i in range(value):
            row = QHBoxLayout()
            x_input = QLineEdit()
            y_input = QLineEdit()

            if i < len(old_x_values):
                x_input.setText(old_x_values[i])
            if i < len(old_y_values):
                y_input.setText(old_y_values[i])

            x_input.setPlaceholderText(f"x{i + 1}")
            y_input.setPlaceholderText(f"y{i + 1}")

            row.addWidget(QLabel(f"{i + 1}."))
            row.addWidget(x_input)
            row.addWidget(y_input)

            container = QFrame()
            container.setLayout(row)
            self.inputs_layout.addWidget(container)

            self.x_inputs.append(x_input)
            self.y_inputs.append(y_input)

    def solve(self):
        input_file = self.edit_file_input.text().strip()
        output_file = self.edit_file_output.text().strip()

        if input_file:  # Если имя входного файла задано — игнорируем ручной ввод
            FieldParser.parse_data(
                self.main_window,
                input_file,
                output_file,
                [],  # пустые x/y, т.к. они будут загружены из файла
                [],
            )
        else:
            x_array = []
            y_array = []

            for x_edit, y_edit in zip(self.x_inputs, self.y_inputs):
                try:
                    x_val = float(x_edit.text())
                    y_val = float(y_edit.text())
                    x_array.append(x_val)
                    y_array.append(y_val)
                except ValueError:
                    print("Ошибка: некорректный ввод.")
                    self.main_window.lbl_bottom.setText(messages.getMessageByCode(14))
                    return

            # === Новая проверка на разную длину ===
            if len(x_array) != len(y_array):
                self.main_window.lbl_bottom.setText("пары не образуются")
                return

            FieldParser.parse_data(
                self.main_window,
                "",
                output_file,
                x_array,
                y_array,
            )


