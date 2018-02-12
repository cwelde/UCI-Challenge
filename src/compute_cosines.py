import pandas as pd
import numpy as np
import csv

#Short program that reads a csv file, adds a third column and writes it to a new output file.



df = pd.read_csv('angles_UCI_CS.csv')

df['angle_cosine'] = np.cos(df[' angle_degrees'])

df.to_csv('out.csv')
