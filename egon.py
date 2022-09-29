import os
import sys
import csv
import pandas as pd #pip install pandas

class egon:
    def egon(self):
        #given a folder with java files with a threshold, print the number of classes that have a coupling higher than the threshold
        #get path of folder and threshold
        path = sys.argv[1]
        threshold = sys.argv[2]

        #if path doesnt exist
        if not path.Path(path).exists():
            print("Path given does not exist")
        else:
            print("Path given exists")

        df = pd.read_csv('tp1_1.csv')
        df = df.sort_values(by=['NVLOC','CSEC'], ascending=False)

        for i in range(len(df)):
            #if NVLOC AND CSEC are lower than threshold remove from csv file
            if df['NVLOC'][i] < threshold and df['CSEC'][i] < threshold:
                df = df.drop(i)
        df.to_csv('tp1_1.csv', index=False)
