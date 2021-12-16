# Author: Md Salman Rahman

import sys 

def main():
    if (len(sys.argv) == 2):
        try:
            infile = open(sys.argv[1], "r")
            print(infile.read())
        except FileNotFoundError as e:
            print("File doesn't found")
    else:
        print("Enter one file name")


# Call the main function.
if __name__ == '__main__':
    main()