import pandas as pd 
import os


pre = os.path.dirname(os.path.realpath(__file__))
filename = "teste.xlsx"
path = pre+'/'+filename

data_frame = pd.read_excel(path)
print(data_frame.to_string())
