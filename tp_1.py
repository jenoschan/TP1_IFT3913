import os
import sys
import csv

#class tp_1: that has a jls method that returns hello world
class tp_1:

    path = sys.argv[1]
    #method that prints hello world
    def jls(self, path):

        path_list = path.split("\\")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        header_added = False

        #return csv file with chemin du fichier, nom du paquet and nom de la classe as headers
        with open('tp_1.csv', 'a+', newline='') as csvfile:
            fieldnames = ['chemin du fichier', 'nom du paquet', 'nom de la classe']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if header_added == False:
                writer.writeheader()
                header_added = True
            writer.writerow({'chemin du fichier': path, 'nom du paquet': packet_name, 'nom de la classe': class_name})

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

    tp.jls(tp.path)
    tp.nvloc(tp.path)