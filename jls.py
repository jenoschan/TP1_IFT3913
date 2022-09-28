import os
from queue import Empty
import sys
import csv
from os import listdir
from os.path import isfile, join
from os import walk


#class tp_1: that has a jls method that returns hello world
class jls:

    path = sys.argv[1]

    def jls(self, path):
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
            print(toAdd)
            result += toAdd + '\n'

        with open("tp_1.csv", "w") as file:
            file.write(result)
            file.close()


if __name__ == "__main__":
    Jls = jls()

    Jls.jls(Jls.path)