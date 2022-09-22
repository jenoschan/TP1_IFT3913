import sys

class nvloc:

    path = sys.argv[1]

    def nvloc(self, path):
    #open file and read it
        source_file = open(path, "r")
        #count the amount of non-empty lines
        count = 0
        for line in source_file:
            if line.strip():
                count += 1
        print(count)


if __name__ == "__main__":
    instance = nvloc()

    instance.nvloc(instance.path)