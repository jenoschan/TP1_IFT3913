import os
from queue import Empty
import sys
import csv
from os import listdir
from os.path import isfile, join
from os import walk


#class tp_1: that has a jls method that returns hello world
class tp_1:

    path = sys.argv[1]

    def jls2(self, path):
        root = path.split('\\')[-1]
        content = []
        for files in os.walk(path):
            if len(files[2]) > 0:
                for file in files[2]:
                    content.append(files[0] + '\\' + file)

        result = "chemin du ficher,nom du paquet,nom de la classe\n"
        for item in content:
            toAdd = item + ','
            candidate = item.split('\\')
            while candidate[0] != root:
                candidate.pop(0)
            candidate.pop(0)
            while len(candidate) > 1:
                if len(candidate) > 2:
                    toAdd += candidate.pop(0) + '.'
                else: toAdd += candidate.pop(0)
            toAdd += ',' + candidate.pop(0)
            result += toAdd + '\n'

        with open("tp_1.csv", "w") as file:
            file.write(result)
            file.close()


    #method that prints hello world
    def writeFile(self, path):

        path_list = path.split("\\")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        #create a csv file, if it exists:
        if os.path.exists("tp_1.csv"):
            with open("tp_1.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_writer.writerow([path, packet_name, class_name])

        else:
            with open("tp_1.csv", "w") as csv_file:
                fields=["chemin du ficher", "nom du paquet", "nom de la classe"]
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"chemin du ficher": path, "nom du paquet": packet_name, "nom de la classe": class_name})

        print(path + "," + packet_name + "," + class_name+"\n")

    
    def nvloc(self, path):
        #open file and read it
        source_file = open(path, "r")
        #count the amount of non-empty lines
        count = 0
        for line in source_file:
            if line.strip():
                count += 1
        print(count)

    def lcsec(self):
        pass

    def egon(self):
        pass

if __name__ == "__main__":
    tp = tp_1()

    tp.jls2(tp.path)
    #tp.nvloc(tp.path)