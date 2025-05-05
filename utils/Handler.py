import os
import sys

from PyQt6.QtWidgets import QTableWidgetItem

from methods.CubicApproximation import cubicApproximation
from methods.ExponentialApproximation import exponentialApproximation
from methods.LinearApproximation import linearApproximation
from methods.LogarithmicApproximation import logarithmicApproximations
from methods.PowerApproximation import powerApproximations
from methods.QuadraticApproximation import quadraticApproximation
from methods.auxiliaryMethods.Coefficients import pirson, standardDeviation, determination
from methods.auxiliaryMethods.AddDotsToMatrix import addDotsToMatrix
from utils import messages
from utils.Utils import clear_graph, printGraph


def handler(main_window, output_file, x_array, y_array):
    table = main_window.table_step
    result = main_window.resultTable
    matrix = []
    sigmas = [0, sys.maxsize]
    clear_graph(main_window.ax, main_window.canvas)
    table.setRowCount(0)
    result.setRowCount(0)
    n = len(x_array)
    g = []
    for i in range(n):
        g.append(i+1)
    matrix.append(g)
    matrix.append(x_array)
    matrix.append(y_array)

    if matrix == []:
        main_window.lbl_bottom.setText(messages.getMessageByCode(21))
    else:



        linearCoeffs = linearApproximation( matrix, n)
        quadraticCoeffs = quadraticApproximation( matrix, n)
        cubicCoeffs = cubicApproximation( matrix, n)
        sumS, matrix, validX, validY = addDotsToMatrix(matrix, linearCoeffs, quadraticCoeffs, cubicCoeffs)
        print(sumS)
        print(validX, validY)
        pirsonCode, r = pirson(matrix)
        vitoScaletta = checkS(validX, validY)
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
        sigma = (standardDeviation(sumS[0], len(matrix[0])))
        if sigmas[1] > sigma:
            sigmas[1] = sigma
        result.setItem(row, 3, QTableWidgetItem(str(sigma)))
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
        sigma = (standardDeviation(sumS[1], len(matrix[0])))
        if sigmas[1] > sigma:
            sigmas[0] = 1
            sigmas[1] = sigma
        result.setItem(row, 3, QTableWidgetItem(str(sigma)))
        result.setItem(row, 4, QTableWidgetItem(""))
        result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
        result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
        row += 1

        detCode, r2 = determination(matrix, 3)
        result.insertRow(row)
        result.setItem(row, 0, QTableWidgetItem("Кубическая"))
        result.setItem(row, 1, QTableWidgetItem(str(cubicCoeffs)))
        result.setItem(row, 2, QTableWidgetItem(
            f"{cubicCoeffs[0]} + {cubicCoeffs[1]}x + {cubicCoeffs[2]}x² + {cubicCoeffs[3]}x³"))
        sigma = (standardDeviation(sumS[2], len(matrix[0])))
        if sigmas[1] > sigma:
            sigmas[0] = 2
            sigmas[1] = sigma
        result.setItem(row, 3, QTableWidgetItem(str(sigma)))
        result.setItem(row, 4, QTableWidgetItem(""))
        result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
        result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
        row += 1


        if validX and validY:

            powerCoeffs = powerApproximations(matrix)


            detCode, r2 = determination(matrix, vitoScaletta[0]+1)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Степенная"))
            result.setItem(row, 1, QTableWidgetItem(str(powerCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{powerCoeffs[0]}·x^{powerCoeffs[1]}"))
            sigma = (standardDeviation(sumS[vitoScaletta[0]], len(matrix[0])))
            if sigmas[1] > sigma:
                sigmas[0] = 3
                sigmas[1] = sigma
            result.setItem(row, 3, QTableWidgetItem(str(sigma)))
            result.setItem(row, 4, QTableWidgetItem(""))
            result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
            result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
            row += 1
        if validX:
            logCoeffs = logarithmicApproximations(matrix)
            detCode, r2 = determination(matrix, vitoScaletta[1]+1)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Логарифмическая"))
            result.setItem(row, 1, QTableWidgetItem(str(logCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{logCoeffs[0]}ln(x)+{logCoeffs[1]}"))
            sigma = (standardDeviation(sumS[vitoScaletta[1]], len(matrix[0])))
            if sigmas[1] > sigma:
                sigmas[0] = 4
                sigmas[1] = sigma
            result.setItem(row, 3, QTableWidgetItem(str(sigma)))
            result.setItem(row, 4, QTableWidgetItem(""))
            result.setItem(row, 5, QTableWidgetItem(f"{r2}"))
            result.setItem(row, 6, QTableWidgetItem(messages.getMessageByCode(detCode)))
            row += 1

        if validY:
            expCoeffs = exponentialApproximation(matrix)
            detCode, r2 = determination(matrix, vitoScaletta[2]+1)
            result.insertRow(row)
            result.setItem(row, 0, QTableWidgetItem("Экспоненциальная"))
            result.setItem(row, 1, QTableWidgetItem(str(expCoeffs)))
            result.setItem(row, 2, QTableWidgetItem(
                f"{expCoeffs[0]}·e^({expCoeffs[1]}x)"))
            sigma = (standardDeviation(sumS[vitoScaletta[2]], len(matrix[0])))
            if sigmas[1] > sigma:
                sigmas[0] = 5
                sigmas[1] = sigma
            result.setItem(row, 3, QTableWidgetItem(str(sigma)))
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

        main_window.lbl_bottom.setText(f"Наиболее точная функция {getBestFunction(sigmas[0])}")
        fillTable(table, matrix)


        printGraph(main_window.ax, main_window.canvas, linearCoeffs, quadraticCoeffs, cubicCoeffs, matrix, validX, validY)



def getBestFunction(index):
    if index == 0:
        return "линейная"
    elif index == 1:
        return "квадратичная"
    elif index == 2:
        return "кубическая"
    elif index == 3:
        return "степенная"
    elif index == 4:
        return "логарифмическая"
    elif index == 5:
        return "экспоненциальная"


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


def checkS(validX, validY):
    res = []
    if validX and validY:
        return [3, 4, 5]
    if validX and not validY:
        return [0, 3, 0]
    if validY and not validX:
        return [0, 0, 3]









