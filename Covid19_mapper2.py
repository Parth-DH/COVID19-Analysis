#! /usr/bin/python

import sys
from datetime import datetime

d1 = sys.argv[1]
d2 = sys.argv[2]

start_date = datetime.strptime(d1, '%Y-%m-%d')
end_date = datetime.strptime(d2, '%Y-%m-%d')

start_date = datetime.date(start_date)
end_date = datetime.date(end_date)

min_date = datetime.strptime('2019-12-31', '%Y-%m-%d')
max_date = datetime.strptime('2020-04-08', '%Y-%m-%d')
min_date = datetime.date(min_date)
max_date = datetime.date(max_date)

if start_date < min_date or end_date > max_date:
    print('Check date range!') 
    sys.exit(-1)

if start_date > end_date:
    print ('Start date cannot be greater than end date!') 
    sys.exit(-1)
    
def main():
    inpfile = sys.stdin
    next(inpfile)

    for line in inpfile:
        
        line = line.strip()
        columns = line.split(',')
        curr_date = datetime.strptime(str(columns[0]), '%Y-%m-%d')
        curr_date = datetime.date(curr_date)
        if curr_date < start_date or curr_date > end_date:
            continue
        try:
            countCases = int(columns[2])
            print ("%s to %s\t%s,%s" % (d1, d2, columns[1],countCases))
        except ValueError:
            pass

if __name__ == '__main__':
    main()