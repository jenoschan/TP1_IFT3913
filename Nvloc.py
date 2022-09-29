import sys
import pathlib as pl
import pandas as pd

class nvloc:

    path = sys.argv[1]

    def nvloc(self, path):
        #get file name from path 
        file_name = pl.Path(path).name
        #open file and read it
        source_file = open(path, "r")
        #count the amount of non-empty lines
        count = 0
        for line in source_file:
            if line.strip():
                count += 1
        #if create tp_1.csv if it doesnt exist
        if not pl.Path("tp_1.csv").exists():
            print("tp_1.csv does not exist, create it using jls.py")
        else:
            #if NVLOC column is not in the csv file, create it and add the count to corresponding class
            if "NVLOC" not in open("tp_1.csv").read():
                #make copy of csv file
                df = pd.read_csv("tp_1.csv")
                #add NVLOC column
                df["NVLOC"] = ""
                #add count to corresponding class
                for i in range(len(df)):
                    #get class name from path
                    if df["nom de la classe"][i] == file_name:
                        df["NVLOC"][i] = count	
                        df.at[i, "NVLOC"] = count
                #save changes to csv file
                df.to_csv("tp_1.csv", index=False)
            else:
                df = pd.read_csv("tp_1.csv")
                for i in range(len(df)):
                    if df["nom de la classe"][i] == file_name:
                        df.at[i, "NVLOC"] = count


if __name__ == "__main__":
    instance = nvloc()

    instance.nvloc(instance.path)