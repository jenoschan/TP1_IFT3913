import os
import sys

def main():
    #get path from command line
    path = sys.argv[1]

    #check if path exists
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)
    
    else:
        path_list = path.split("\\")
        packet_name = ".".join(path_list[1:-1])
        class_name = os.path.basename(path).split(".")[0]

        print(path +", "+ packet_name +", "+ class_name)

if __name__ == "__main__":
    main()
