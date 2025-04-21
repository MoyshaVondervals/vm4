import math
import os
import re
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from math import ceil

from PyQt6.QtWidgets import QTableWidgetItem

from depricatedMethods import RectangleLeftMethod, RectangleRightMethod, RectangleMidMethod, TrapezoidMethod, SimpsonMethod
from utils import messages, Utils
from utils.Handler import handler
from utils.Utils import clear_graph, predefined_functions, checkBrakePoints


def parse_data(main_window, eq_num, input_file, output_file, left_bound, right_bound, h):
    stackTrace = ""
    valid = True

    if input_file == "":
        left_bound = left_bound.replace(",", ".")
        right_bound = right_bound.replace(",", ".")
        h = h.replace(",", ".")
        if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", left_bound) is None:
            stackTrace += f"{messages.getMessageByCode(14)}\n"
            valid =False
        else:
            left_bound = float(left_bound)
        if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", right_bound) is None:
            stackTrace += f"{messages.getMessageByCode(15)}\n"
            valid = False
        else:
            right_bound = float(right_bound)

        if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", h) is None:
            print("1")
            stackTrace += f"{messages.getMessageByCode(16)}\n"
            valid = False
        else:
            h = float(h)
            # lowBound = math.ceil((right_bound-left_bound)*10000/12)/10000
            # highBound = math.floor((right_bound-left_bound)*10000/8)/10000
            lowBound = ((right_bound-left_bound)/12)
            highBound = ((right_bound-left_bound)/7)
            if not(lowBound<=h<=highBound):
                stackTrace += f"{messages.getMessageByCode(16)}\n"
                stackTrace += (f"На выбраном интервале возможны значения:"
                               f" [{lowBound},"
                               f" {highBound}]\n")

                valid = False


    else:
        parsedData = []
        print(os.getcwd())
        if os.path.exists(input_file):
            with open(input_file, "r", encoding="utf-8") as file:
                lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                parsedData.append(line)


            left_bound = parsedData[0].replace(",", ".")
            right_bound = parsedData[1].replace(",", ".")
            h = parsedData[2].replace(",", ".")
            if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", left_bound) is None:
                stackTrace += f"{messages.getMessageByCode(14)}\n"
                valid = False
            else:
                left_bound = float(left_bound)
            if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", right_bound) is None:
                stackTrace += f"{messages.getMessageByCode(15)}\n"
                valid = False
            else:
                right_bound = float(right_bound)
            if re.match("^[+-]?(?:\d+[.,]\d+|\d+)$", h) is None:
                print("1")
                stackTrace += f"{messages.getMessageByCode(16)}\n"
                valid = False
            else:
                h = float(h)
                lowBound = ((right_bound - left_bound) / 12)
                highBound = ((right_bound - left_bound) / 7)
                if not (lowBound <= h <= highBound):
                    stackTrace += f"{messages.getMessageByCode(16)}\n"
                    stackTrace += (f"На выбраном интервале возможны значения:"
                                   f" [{lowBound},"
                                   f" {highBound}]\n")
                    valid = False
        else:
            stackTrace += f"{messages.getMessageByCode(12)}\n"
            valid = False
    if valid!=False and left_bound>right_bound:
        stackTrace += f"{messages.getMessageByCode(17)}\n"
        valid=False



    main_window.lbl_bottom.setText(stackTrace)
    if valid:
        handler(main_window, eq_num, output_file, left_bound, right_bound, h)




