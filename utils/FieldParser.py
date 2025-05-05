import os
import re

from utils import messages, Handler


def parse_data(main_window, input_file, output_file, x_array, y_array):
    stackTrace = ""
    valid = True

    # === Если задан input_file — читаем оттуда ===
    if input_file.strip():
        parsed_x = []
        parsed_y = []

        # === Проверка существования файла ===
        if os.path.exists(input_file):
            try:
                with open(input_file, "r", encoding="utf-8") as file:
                    lines = [line.strip() for line in file if line.strip()]

                if not (8 <= len(lines) <= 12):
                    stackTrace += "Ошибка: количество строк в файле должно быть от 8 до 12.\n"
                    valid = False
                else:
                    for i, line in enumerate(lines, start=1):
                        parts = re.split(r"\s+", line)
                        if len(parts) != 2:
                            stackTrace += f"Ошибка: строка {i} должна содержать два числа (x y).\n"
                            valid = False
                            break
                        try:
                            x_val = float(parts[0].replace(",", "."))
                            y_val = float(parts[1].replace(",", "."))
                            parsed_x.append(x_val)
                            parsed_y.append(y_val)
                        except ValueError:
                            stackTrace += f"Ошибка: строка {i} содержит недопустимые значения.\n"
                            valid = False
                            break

                    # === Новая проверка: длина x и y должна совпадать ===
                    if valid and len(parsed_x) != len(parsed_y):
                        stackTrace += "пары не образуются\n"
                        valid = False

            except Exception as e:
                stackTrace += f"Ошибка при чтении файла: {str(e)}\n"
                valid = False
        else:
            stackTrace += f"{messages.getMessageByCode(12)}\n"
            valid = False

        if valid:
            x_array[:] = parsed_x
            y_array[:] = parsed_y

    # === Вывод сообщений в интерфейс ===
    if not valid:
        main_window.lbl_bottom.setText(stackTrace)
        return

    print("x =", x_array)
    print("y =", y_array)

    # Вызываем обработку
    Handler.handler(main_window, output_file, x_array, y_array)
