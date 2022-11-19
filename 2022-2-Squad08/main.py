import pandas as pd
import os


def get_full_path(filename):
    pre = os.path.dirname(os.path.realpath(__file__))
    return pre + "/" + filename


def xlsx_printer(path):
    data_frame = pd.read_excel(path)
    print(data_frame.to_string())


if __name__ == "__main__":

    filename = "teste.xlsx"

    try:
        xlsx_printer(filename)
    except:
        xlsx_printer(get_full_path(filename))