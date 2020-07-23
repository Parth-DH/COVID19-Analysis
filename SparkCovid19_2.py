from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession
from datetime import datetime
import csv
from pyspark import SparkContext
from collections import defaultdict

if __name__ == "__main__":
    inputfile = sys.argv[1]
    cachefile = sys.argv[2]

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    sc = SparkContext.getOrCreate();
    lines = sc.textFile(inputfile).mapPartitions(lambda part: csv.reader(part))
    header = lines.first()
    data = lines.filter(lambda row: row != header)

    c_lines = sc.textFile(cachefile).mapPartitions(lambda part: csv.reader(part))
    c_header = c_lines.first()
    c_data = c_lines.filter(lambda row: row != c_header)
    filter_data = c_data.filter(lambda row: row[4] != '').map(lambda row: (row[1], int(row[4]))).collect()
    hmap = dict(filter_data)
    ddhmap = defaultdict(int, hmap)
    popmap = sc.broadcast(ddhmap)

    totalcases = data.map(lambda x: (x[1], int(x[2]))).reduceByKey(add)

    
    output = totalcases.filter(lambda row: popmap.value[row[0]]!= 0).map(lambda row: (row[0] ,((row[1]/popmap.value[row[0]]*1000000)))).collect()


    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
