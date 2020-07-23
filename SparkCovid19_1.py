from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession
from datetime import datetime
import csv
from pyspark import SparkContext

if __name__ == "__main__":
    d1 = sys.argv[2]
    d2 = sys.argv[3]

    start_date = datetime.strptime(d1, '%Y-%m-%d')
    end_date = datetime.strptime(d2, '%Y-%m-%d')

    start_date = datetime.date(start_date)
    end_date = datetime.date(end_date)

    min_date = datetime.strptime('2019-12-31', '%Y-%m-%d')
    max_date = datetime.strptime('2020-04-08', '%Y-%m-%d')
    min_date = datetime.date(min_date)
    max_date = datetime.date(max_date)

    if start_date < min_date or end_date > max_date:
        print('Check date range!', file = sys.stderr)
        sys.exit(-1)

    if start_date > end_date:
        print ('Start date cannot be greater than end date!', file = sys.stderr) 
        sys.exit(-1)

    if len(sys.argv) != 4:
        print("Usage: wordcount <start_date> <end_date>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    sc = SparkContext.getOrCreate();
    lines = sc.textFile(sys.argv[1]).mapPartitions(lambda part: csv.reader(part))

    header = lines.first()

    data = lines.filter(lambda row: row != header)

    valid_data = data.filter(lambda row: datetime.date(datetime.strptime(str(row[0]), '%Y-%m-%d')) >= min_date and datetime.date(datetime.strptime(str(row[0]), '%Y-%m-%d')) <=max_date)
    output = valid_data.map(lambda x: (x[1], int(x[2]))).reduceByKey(add).collect()

    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
