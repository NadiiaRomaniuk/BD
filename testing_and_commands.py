#Команди: 

#start-dfs.sh
#start-yarn.sh
#sudo su - hadoop
#sudo service ssh start
#spark-submit --master local[*] spark_read_scema.py


# тест спарку
"""from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .getOrCreate()
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, schema)
df.show()"""


#Основні імпорти та підключення
"""from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("HDFS Integration Example") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://0.0.0.0:9000") \
    .config("spark.hadoop.fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem") \
    .getOrCreate()

from pyspark.sql.functions import col, explode, split, udf, desc, avg, count, when, expr, sum, max, min
from pyspark.sql.types import StringType, ArrayType, IntegerType, DoubleType
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.recommendation import ALS
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import StandardScaler
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np"""











