import os
import sys

#class tp_1: that has a jls method that returns hello world
class tp_1:

    path = sys.argv[1]
    #method that prints hello world
    def jls(self, path):

        path_list = path.split("\\")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        print(path +", "+ packet_name +", "+ class_name)

    
    def nvloc(self, path):
        #open file and read it
        file = open(path, "r")
        #count the amount of non-empty lines
        count = 0
        for line in file:
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