import os

from PyQt6.QtWidgets import QTableWidgetItem

from methods.CubicApproximation import cubicApproximation
from methods.LinearApproximation import linearApproximation
from methods.QuadraticApproximation import quadraticApproximation
from methods.auxiliaryMethods.Coefficients import pirson, standardDeviation, determination
from methods.auxiliaryMethods.MatrixIXY import matrixIXY
from methods.auxiliaryMethods.AddDotsToMatrix import addDotsToMatrix
from utils import messages
from utils.Utils import clear_graph, printGraph


def handler(main_window, eq_num, output_file, left_bound, right_bound, h):
    table = main_window.table_step
    result = main_window.resultTable

    clear_graph(main_window.ax, main_window.canvas)
    table.setRowCount(0)
    result.setRowCount(0)

    n, matrix = matrixIXY(eq_num, left_bound, right_bound, h)
    if matrix == []:
        main_window.lbl_bottom.setText(messages.getMessageByCode(21))
    else:



        linearCoeffs = linearApproximation(eq_num, matrix, n)
        quadraticCoeffs = quadraticApproximation(eq_num, matrix, n)
        cubicCoeffs = cubicApproximation(eq_num, matrix, n)
        sumS, matrix, limitation = addDotsToMatrix(matrix, linearCoeffs, quadraticCoeffs, cubicCoeffs)
        pirsonCode, r = pirson(matrix)

        headers = [
            "Тип аппроксимации",
            "Коэффициенты",
            "Уравнение",
            "σ (СКО)",
            "r (Пирсон)",
            "R² (дет.)",
            "Комментарий"
        ]
        result.setColumnCount(len(headers))
        result.setHorizontalHeaderLabels(headers)

        row = 0  # счётчик строк

        detCode, r2 = determination(matrix, 1)
        result.insertRow(row)
        result.setItem(row, 0, QTableWidgetItem("Линейная"))
        result.setItem(row, 1, QTableWidgetItem(str(linearCoeffs)))
        result.setItem(row, 2, QTableWidgetItem(f"{linearCoeffs[0]} + {linearCoeffs[1]}x"))
        result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[0], len(matrix[0])))))
        result.setItem(row, 4, QTableWidgetItem(f"{r} {messages.getMessageByCode(pirsonCode)}"))
        result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
        result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
        row += 1

        detCode, r2 = determination(matrix, 2)
        result.insertRow(row)
        result.setItem(row, 0, QTableWidgetItem("Квадратичная"))
        result.setItem(row, 1, QTableWidgetItem(str(quadraticCoeffs)))
        result.setItem(row, 2, QTableWidgetItem(
            f"{quadraticCoeffs[0]} + {quadraticCoeffs[1]}x + {quadraticCoeffs[2]}x²"))
        result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[1], len(matrix[0])))))
        result.setItem(row, 4, QTableWidgetItem(""))  # r для квадрата не считался
        result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
        result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
        row += 1

        detCode, r2 = determination(matrix, 3)
        result.insertRow(row)
        result.setItem(row, 0, QTableWidgetItem("Кубическая"))
        result.setItem(row, 1, QTableWidgetItem(str(cubicCoeffs)))
        result.setItem(row, 2, QTableWidgetItem(
            f"{cubicCoeffs[0]} + {cubicCoeffs[1]}x + {cubicCoeffs[2]}x² + {cubicCoeffs[3]}x³"))
        result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[2], len(matrix[0])))))
        result.setItem(row, 4, QTableWidgetItem(""))
        result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
        result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
        row += 1

        if not limitation:
            detCode, r2 = determination(matrix, 4)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Экспоненциальная"))
            result.setItem(row, 1, QTableWidgetItem(str(linearCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{linearCoeffs[0]}·e^{linearCoeffs[1]}x"))
            result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[3], len(matrix[0])))))
            result.setItem(row, 4, QTableWidgetItem(""))
            result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
            result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
            row += 1

            detCode, r2 = determination(matrix, 5)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Логарифмическая"))
            result.setItem(row, 1, QTableWidgetItem(str(linearCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{linearCoeffs[0]} + {linearCoeffs[1]}·ln(x)"))
            result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[4], len(matrix[0])))))
            result.setItem(row, 4, QTableWidgetItem(""))
            result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
            result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
            row += 1
            # === СТЕПЕННАЯ ===
            detCode, r2 = determination(matrix, 6)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Степенная"))
            result.setItem(row, 1, QTableWidgetItem(str(linearCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{linearCoeffs[0]}·x^{linearCoeffs[1]}"))
            result.setItem(row, 3, QTableWidgetItem(str(standardDeviation(sumS[5], len(matrix[0])))))
            result.setItem(row, 4, QTableWidgetItem(""))
            result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
            result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
            row += 1

        result.resizeColumnsToContents()
        result.resizeRowsToContents()
        result.setRowCount(row)
        result.resizeRowsToContents()

        if output_file != "" and os.path.exists(output_file):
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("Таблица аппроксимаций\n")
                f.write("\t".join(headers) + "\n")
                for r_idx in range(result.rowCount()):
                    row_text = []
                    for c_idx in range(result.columnCount()):
                        item = result.item(r_idx, c_idx)
                        row_text.append(item.text() if item else "")
                    f.write("\t".join(row_text) + "\n")
                f.write("\n")

            print(f"Результаты сохранены в файл: {output_file}")
        else:
            main_window.lbl_bottom.setText(messages.getMessageByCode(13))
        determination(matrix, 1)


        fillTable(table, matrix)


        printGraph(main_window.ax, main_window.canvas, left_bound, right_bound, linearCoeffs, quadraticCoeffs, cubicCoeffs, matrix, limitation)






def fillTable(table, matrix):
    row_labels = {
        0: "i",
        1: "xi",
        2: "yi",
        3: "Lφ(x)",
        4: "(Lφ(x)-y)^2",
        5: "Qφ(x)",
        6: "(Qφ(x)-y)^2",
        7: "Cφ(x)",
        8: "(Cφ(x)-y)^2",
        9: "Eφ(x)",
        10: "(Eφ(x)-y)^2",
        11: "Lφ(x)",
        12: "(Lφ(x)-y)^2",
        13: "Pφ(x)",
        14: "(Pφ(x)-y)^2",


    }

    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    table.setColumnCount(cols + 1)  # +1 для колонки меток
    table.setRowCount(rows)

    for r in range(rows):
        # Вставляем метку строки из словаря
        label = row_labels.get(r, "")  # если нет — пустая строка
        table.setItem(r, 0, QTableWidgetItem(str(label)))

        # Заполняем остальные ячейки данными из matrix
        for c in range(cols):
            value = matrix[r][c]
            table.setItem(r, c + 1, QTableWidgetItem(str(value)))
    table.resizeColumnsToContents()
    table.resizeRowsToContents()












