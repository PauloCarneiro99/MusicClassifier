import pandas as pd
import sys

base_name = "full_data"
base_file = pd.read_csv("full_data00000.csv")

cont = 4500
for i in range(9):
    temp = pd.read_csv("{}{:05}.csv".format(base_name, cont))
    cont += 4500
    base_file = base_file.append(temp, ignore_index = True)

base_file.to_csv(r"full_data.csv")