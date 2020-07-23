#! /usr/bin/python

import sys
import os

def main():
    inpfile = sys.stdin
    next(inpfile)
    for line in inpfile:
        line = line.strip()
        columns = line.split(',') 
        try:
            countCases = int(columns[2])
            print ("%s,%s" % (columns[1],countCases))
        except ValueError:
            pass
    for line in open('populations'): 
        line = line.strip()
        columns = line.split(',')
        try:
            totCases = int(columns[4])
            print ("%s\t%s" % (columns[1],columns[4]))
        except ValueError:
            pass

if __name__ == '__main__':
    main()