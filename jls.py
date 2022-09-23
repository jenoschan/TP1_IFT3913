import pathlib as pl
import os
import sys
import csv

class jls:
    def jls(self):
        path = sys.argv[1].replace('"', '')

        if '\\' and '"' in path:
            path = path.replace('\\', '/')

        path_list = path.split("/")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        #return csv file with chemin du fichier, nom du paquet and nom de la classe as headers
        with open('tp_1.csv', 'a', newline='') as csvfile:
            fieldnames = ['chemin du fichier', 'nom du paquet', 'nom de la classe']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #if file is empty, write headers
            if os.stat('tp_1.csv').st_size == 0:
                writer.writeheader()
                writer.writerow({'chemin du fichier': path, 'nom du paquet': packet_name, 'nom de la classe': class_name})
            else:
                writer.writerow({'chemin du fichier': path, 'nom du paquet': packet_name, 'nom de la classe': class_name})
        
        #print(path + "," + packet_name + "," + class_name+"\n")

        #if path doesnt exist
        if not pl.Path(path).exists():
            print("Path is in a valid format, but doesn't exist on this computer")
            return

        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            #print directories
            if level == 0:
                print(root)
            #TODO : fix formatting
            indent = ' ' * 4 * (level) + "|__"
            print('{}{}/'.format(indent, os.path.basename(root)))
            #print files
            subindent = ' ' * 4 * (level) + "|" + " " * 4 + "|__"
            for f in files:
                print('{}{}'.format(subindent, f))

if __name__ == '__main__':
    jls.jls(sys.argv[1])