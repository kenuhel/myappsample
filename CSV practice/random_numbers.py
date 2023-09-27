import csv
import numpy as np

num_col = 4
num_row = 6

rdn_num = np.random.randint(1,11,(num_row,num_col))

with open("random_num.csv", mode="w") as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in rdn_num:
        csvwriter.writerow(line)