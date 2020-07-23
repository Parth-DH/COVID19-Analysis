# COVID19-Analysis
There are 3 main analytics that were carried out:
1) Finding out the total number of active COVID-19 cases given daily data from various countries.
2) Finding out the number of cases in a given date range
3) Find the total number of cases per capita given population data (populations.csv)

Task 2 and 3 were carried out using both Spark and Hadoop.

## Timings and Usage 

Here are the various timings as well as the usage directions for the hadoop and spark tasks. I timed both the implementations using the time functionality in the terminal commands by adding time before my commands. I have listed the real times and not the user or system times for these processes. Clearly, Spark processes were running upto 3 times faster as compared to Hadoop processes.

Hadoop 1 - 25.184s
hadoop jar ./libexec/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file /Users/parth/Downloads/Covid19_mapper1.py -mapper '/Users/parth/Downloads/Covid19_mapper1.py "false"' -file /Users/parth/Downloads/Covid19_reducer1.py  -reducer /Users/parth/Downloads/Covid19_reducer1.py  -input hw/covid19_full_data.csv -output hw/output 

Hadoop 2 - 24.096s
hadoop jar ./libexec/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file /Users/parth/Downloads/Covid19_mapper2.py -mapper '/Users/parth/Downloads/Covid19_mapper2.py "2020-03-03" "2020-03-28" ' -file /Users/parth/Downloads/Covid19_reducer2.py  -reducer /Users/parth/Downloads/Covid19_reducer1.py  -input hw/covid19_full_data.csv -output hw/output

Hadoop 3 - 24.243s
hadoop jar ./libexec/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -mapper /Users/parth/Downloads/Covid19_mapper3.py  -reducer /Users/parth/Downloads/Covid19_reducer3.py  -input hw/covid19_full_data.csv -cacheFile 'hw/populations.csv#populations' -output hw/output


Spark 1 - 8.645s
time spark-submit SparkCovid19_1.py /Users/parth/Downloads/covid19_full_data.csv '2020-03-03' ‘2020-03-28'

Spark 2 - 8.338s
time spark-submit SparkCovid19_2.py /Users/parth/Downloads/covid19_full_data.csv /Users/parth/Downloads/populations.csv
