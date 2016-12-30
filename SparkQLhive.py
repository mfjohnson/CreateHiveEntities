from pyspark import *
from pyspark.sql import *

sc = SparkContext(appName="HiveTest")
hc = HiveContext(sc)
peopleRDD = sc.parallelize(['{"name":"Yin","age":30}'])
peopleDF = hc.jsonRDD(peopleRDD)
peopleDF.printSchema()

peopleDF.saveAsTable("peopleHive")