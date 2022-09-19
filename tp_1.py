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

    tp.jls(tp.path)
    tp.nvloc(tp.path)