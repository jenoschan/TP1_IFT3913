from tkinter import W
import sys
import pathlib as pl
import os
import csv
import pandas as pd #pip install pandas 

class lcsec:

    path = sys.argv[1]
    csv_path = sys.argv[2]
    

    def lcsec(self, path, csv_path):
        #Create the lcsec program that takes as input the path of a folder and the path for tp1_1.csv

        #get path of folder and csv file
        path = sys.argv[1]
        csv_path = sys.argv[2]

        #if path doesnt exist
        if not pl.Path(path).exists():
            print("Path given does not exist")
        #if csv file doesnt exist
        elif not pl.Path(csv_path).exists():
            print("CSV file given does not exist")
        else: 
            print("Path and CSV file given exist")

        #get paths and class names of files in csv
        files = []
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                files.append((row[0], row[2][:-5]))
            csv_file.close()
        files.pop(0)

        counts = []
        # get the number of other class mentions inside current class

        for i in range(len(files)):
            count = 0
            f = open(files[i][0], 'r')
            txt = f.read()
            f.close()
            for j in range(len(files)):
                if j != i:
                    count += txt.count(files[j][1])

            # get the number of times the class is mentioned in other classes

            for j in range(len(files)):
                if j != i:
                    f = open(files[j][0], 'r')
                    txt = f.read()
                    f.close()
                    count += txt.count(files[i][1])
            counts.append(count)
        
        # adding the column to the csv

        data = pd.read_csv(csv_path)

        if 'CSEC' in data.columns:
            data.drop('CSEC', axis = 1)
        data['CSEC'] = counts

        data.to_csv('tp_1.csv', index=False)


if __name__ == "__main__":
    Lls = lcsec()

    Lls.lcsec(Lls.path, Lls.csv_path)
