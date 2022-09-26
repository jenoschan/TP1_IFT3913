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
        df = df.sort_values(by=['CSEC'], ascending=False)

        for i in range(len(df)):
            if df['CSEC'][i] >= threshold:
                continue #continue until the first class that has a coupling lower than the threshold
            else:
                print(df.iloc[i-1]) #this is going to print everything that is above the threshold value

