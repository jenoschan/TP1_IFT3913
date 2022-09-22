from tkinter import W


class lcsec:
    def lcsec(path, csv_path):
        #Create the lcsec program that takes as input the path of a folder and the path for tp1_1.csv
    
        #import modules
        import pathlib as pl
        import os
        import sys
        import csv

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

        #get last class name from csv
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            last_class = list(reader)[-1][-1]

            
