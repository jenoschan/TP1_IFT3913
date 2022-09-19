import os
import sys

#class tp_1: that has a jls method that returns hello world
class tp_1:

    path = sys.argv[1]
    #method that prints hello world
    def jls(self, path):

        #create a csv file
        csv_file = open("tp_1.csv", "w")

        path_list = path.split("\\")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        #return a csv file with path, packet name and class name
        csv_file.write(path + "," + packet_name + "," + class_name+"\n")

    
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