#! /usr/bin/python

import sys

world_info = sys.argv[1]

def main():
    inpfile = sys.stdin
    next(inpfile)
    for line in inpfile:
        line = line.strip()
        columns = line.split(',') 
        if '2019' in columns[0]:
            continue
        if 'World' in columns[1] and world_info == 'false':
            continue
        try:
            countCases = int(columns[2])
            print ("%s,%s" % (columns[1],countCases))
        except ValueError:
            pass

if __name__ == '__main__':
    main()