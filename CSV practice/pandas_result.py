import pandas as pd
import numpy as np
import csv


pf = pd.read_csv("random_num.csv")

col_sum = pf.sum()

print(col_sum)



